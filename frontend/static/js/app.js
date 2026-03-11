/**
 * InflationScanner - Frontend applicatie
 */

const API = "/api";
let priceChart = null;

// --- Zoekfunctionaliteit ---

document.getElementById("searchBtn").addEventListener("click", searchProducts);
document.getElementById("searchInput").addEventListener("keypress", (e) => {
  if (e.key === "Enter") searchProducts();
});

async function searchProducts() {
  const query = document.getElementById("searchInput").value.trim();
  if (!query) return;

  const res = await fetch(`${API}/products?search=${encodeURIComponent(query)}`);
  const products = await res.json();

  const container = document.getElementById("searchResults");
  if (products.length === 0) {
    container.innerHTML =
      '<p class="empty-state">Geen producten gevonden. Voeg het product hieronder toe!</p>';
    return;
  }

  container.innerHTML = products
    .map(
      (p) => `
    <div class="result-item" onclick="showPriceHistory(${p.id})">
      <div>
        <span class="name">${p.name}</span>
        ${p.brand ? `<span class="meta"> &mdash; ${p.brand}</span>` : ""}
      </div>
      <span class="meta">${p.category || ""} ${p.barcode ? `| ${p.barcode}` : ""}</span>
    </div>
  `
    )
    .join("");
}

// --- Prijsgeschiedenis ---

async function showPriceHistory(productId) {
  const res = await fetch(`${API}/prices/${productId}/history`);
  const data = await res.json();

  const section = document.getElementById("priceHistorySection");
  section.classList.remove("hidden");

  document.getElementById("productTitle").textContent =
    `${data.product.name}${data.product.brand ? " (" + data.product.brand + ")" : ""}`;

  document.getElementById("currentPrice").textContent = data.current_price
    ? `€${data.current_price.toFixed(2)}`
    : "-";

  document.getElementById("oldestPrice").textContent = data.oldest_price
    ? `€${data.oldest_price.toFixed(2)}`
    : "-";

  const changeEl = document.getElementById("priceChange");
  if (data.price_change_percent !== null) {
    const sign = data.price_change_percent > 0 ? "+" : "";
    changeEl.textContent = `${sign}${data.price_change_percent}%`;
    changeEl.className =
      "price change " +
      (data.price_change_percent > 0 ? "positive" : "negative");
  } else {
    changeEl.textContent = "-";
    changeEl.className = "price change";
  }

  // Grafiek tekenen
  drawChart(data.history);

  // Scroll naar de grafiek
  section.scrollIntoView({ behavior: "smooth" });
}

function drawChart(history) {
  const ctx = document.getElementById("priceChart").getContext("2d");

  if (priceChart) {
    priceChart.destroy();
  }

  const labels = history.map((h) => {
    const d = new Date(h.recorded_at);
    return d.toLocaleDateString("nl-NL", {
      year: "numeric",
      month: "short",
      day: "numeric",
    });
  });

  const prices = history.map((h) => h.price);

  priceChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Prijs (€)",
          data: prices,
          borderColor: "#3498db",
          backgroundColor: "rgba(52, 152, 219, 0.1)",
          fill: true,
          tension: 0.3,
          pointRadius: 5,
          pointHoverRadius: 8,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          callbacks: {
            label: (ctx) => {
              const point = history[ctx.dataIndex];
              let label = `€${ctx.parsed.y.toFixed(2)}`;
              if (point.store_name) label += ` (${point.store_name})`;
              return label;
            },
          },
        },
      },
      scales: {
        y: {
          beginAtZero: false,
          ticks: {
            callback: (value) => `€${value.toFixed(2)}`,
          },
        },
      },
    },
  });
}

// --- Barcode scanner ---

document.getElementById("scanBtn").addEventListener("click", startScanner);
document
  .getElementById("closeScannerBtn")
  .addEventListener("click", stopScanner);

function startScanner() {
  const container = document.getElementById("scannerContainer");
  container.classList.remove("hidden");

  Quagga.init(
    {
      inputStream: {
        name: "Live",
        type: "LiveStream",
        target: document.getElementById("scanner"),
        constraints: {
          facingMode: "environment",
        },
      },
      decoder: {
        readers: [
          "ean_reader",
          "ean_8_reader",
          "upc_reader",
          "upc_e_reader",
        ],
      },
    },
    (err) => {
      if (err) {
        alert(
          "Camera niet beschikbaar. Controleer of je toestemming hebt gegeven."
        );
        container.classList.add("hidden");
        return;
      }
      Quagga.start();
    }
  );

  Quagga.onDetected(async (result) => {
    const barcode = result.codeResult.code;
    stopScanner();

    // Zoek product op barcode
    document.getElementById("searchInput").value = barcode;
    try {
      const res = await fetch(`${API}/products/barcode/${barcode}`);
      if (res.ok) {
        const product = await res.json();
        showPriceHistory(product.id);
      } else {
        // Product niet gevonden, vul barcode in bij formulier
        document.getElementById("productBarcode").value = barcode;
        alert(
          `Barcode ${barcode} is nog niet bekend. Voeg het product hieronder toe!`
        );
      }
    } catch {
      searchProducts();
    }
  });
}

function stopScanner() {
  Quagga.stop();
  document.getElementById("scannerContainer").classList.add("hidden");
}

// --- Prijs toevoegen ---

document.getElementById("addPriceForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("productName").value.trim();
  const barcode = document.getElementById("productBarcode").value.trim() || null;
  const category = document.getElementById("productCategory").value || null;
  const storeName = document.getElementById("storeName").value.trim();
  const price = parseFloat(document.getElementById("productPrice").value);
  const dateStr = document.getElementById("priceDate").value;

  const msgEl = document.getElementById("formMessage");

  try {
    // 1. Zoek of maak product
    let product;
    if (barcode) {
      const searchRes = await fetch(`${API}/products/barcode/${barcode}`);
      if (searchRes.ok) {
        product = await searchRes.json();
      }
    }

    if (!product) {
      const createRes = await fetch(`${API}/products`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, barcode, category }),
      });
      if (!createRes.ok) {
        // Product met barcode bestaat al, zoek het op
        const existing = await fetch(`${API}/products/barcode/${barcode}`);
        if (existing.ok) {
          product = await existing.json();
        } else {
          throw new Error("Kon product niet aanmaken");
        }
      } else {
        product = await createRes.json();
      }
    }

    // 2. Zoek of maak winkel
    let storeId = null;
    if (storeName) {
      const storesRes = await fetch(`${API}/stores`);
      const stores = await storesRes.json();
      const existing = stores.find(
        (s) => s.name.toLowerCase() === storeName.toLowerCase()
      );

      if (existing) {
        storeId = existing.id;
      } else {
        const storeRes = await fetch(`${API}/stores`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name: storeName }),
        });
        const store = await storeRes.json();
        storeId = store.id;
      }
    }

    // 3. Voeg prijs toe
    const priceData = {
      product_id: product.id,
      store_id: storeId,
      price: price,
      source: "manual",
    };
    if (dateStr) {
      priceData.recorded_at = new Date(dateStr).toISOString();
    }

    const priceRes = await fetch(`${API}/prices`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(priceData),
    });

    if (!priceRes.ok) throw new Error("Kon prijs niet opslaan");

    msgEl.textContent = `Prijs van €${price.toFixed(2)} opgeslagen voor ${name}!`;
    msgEl.className = "form-message success";
    msgEl.classList.remove("hidden");

    // Reset formulier en laad data opnieuw
    e.target.reset();
    loadTopInflation();

    // Toon prijsgeschiedenis
    showPriceHistory(product.id);
  } catch (err) {
    msgEl.textContent = `Fout: ${err.message}`;
    msgEl.className = "form-message error";
    msgEl.classList.remove("hidden");
  }

  setTimeout(() => msgEl.classList.add("hidden"), 5000);
});

// --- Top inflatie producten laden ---

async function loadTopInflation() {
  const res = await fetch(`${API}/stats/top-inflation`);
  const data = await res.json();

  const container = document.getElementById("topInflation");
  if (data.length === 0) {
    container.innerHTML =
      '<p class="empty-state">Voeg prijzen toe om de grootste stijgingen te zien.</p>';
    return;
  }

  container.innerHTML = data
    .map(
      (item) => `
    <div class="inflation-item" onclick="showPriceHistory(${item.product_id})">
      <div>
        <span class="name">${item.product_name}</span>
        <span class="prices">€${item.oldest_price.toFixed(2)} → €${item.current_price.toFixed(2)}</span>
      </div>
      <span class="change-badge ${item.change_percent < 0 ? "deflation" : ""}">
        ${item.change_percent > 0 ? "+" : ""}${item.change_percent}%
      </span>
    </div>
  `
    )
    .join("");
}

// Laad top inflatie bij pagina-laden
loadTopInflation();
