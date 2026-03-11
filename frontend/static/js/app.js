/**
 * InflationScanner - Frontend applicatie
 */

const API = "/api";
let priceChart = null;

// --- Volledige landenlijst met vlaggen (ISO 3166-1 alpha-2) ---
// Gesorteerd op naam, gegroepeerd per continent

const COUNTRIES = [
  // Europa
  { code: "AL", name: "Albanië", flag: "\u{1F1E6}\u{1F1F1}" },
  { code: "AD", name: "Andorra", flag: "\u{1F1E6}\u{1F1E9}" },
  { code: "AT", name: "Oostenrijk", flag: "\u{1F1E6}\u{1F1F9}" },
  { code: "BY", name: "Belarus", flag: "\u{1F1E7}\u{1F1FE}" },
  { code: "BE", name: "België", flag: "\u{1F1E7}\u{1F1EA}" },
  { code: "BA", name: "Bosnië en Herzegovina", flag: "\u{1F1E7}\u{1F1E6}" },
  { code: "BG", name: "Bulgarije", flag: "\u{1F1E7}\u{1F1EC}" },
  { code: "HR", name: "Kroatië", flag: "\u{1F1ED}\u{1F1F7}" },
  { code: "CY", name: "Cyprus", flag: "\u{1F1E8}\u{1F1FE}" },
  { code: "CZ", name: "Tsjechië", flag: "\u{1F1E8}\u{1F1FF}" },
  { code: "DK", name: "Denemarken", flag: "\u{1F1E9}\u{1F1F0}" },
  { code: "EE", name: "Estland", flag: "\u{1F1EA}\u{1F1EA}" },
  { code: "FI", name: "Finland", flag: "\u{1F1EB}\u{1F1EE}" },
  { code: "FR", name: "Frankrijk", flag: "\u{1F1EB}\u{1F1F7}" },
  { code: "DE", name: "Duitsland", flag: "\u{1F1E9}\u{1F1EA}" },
  { code: "GR", name: "Griekenland", flag: "\u{1F1EC}\u{1F1F7}" },
  { code: "HU", name: "Hongarije", flag: "\u{1F1ED}\u{1F1FA}" },
  { code: "IS", name: "IJsland", flag: "\u{1F1EE}\u{1F1F8}" },
  { code: "IE", name: "Ierland", flag: "\u{1F1EE}\u{1F1EA}" },
  { code: "IT", name: "Italië", flag: "\u{1F1EE}\u{1F1F9}" },
  { code: "XK", name: "Kosovo", flag: "\u{1F1FD}\u{1F1F0}" },
  { code: "LV", name: "Letland", flag: "\u{1F1F1}\u{1F1FB}" },
  { code: "LI", name: "Liechtenstein", flag: "\u{1F1F1}\u{1F1EE}" },
  { code: "LT", name: "Litouwen", flag: "\u{1F1F1}\u{1F1F9}" },
  { code: "LU", name: "Luxemburg", flag: "\u{1F1F1}\u{1F1FA}" },
  { code: "MT", name: "Malta", flag: "\u{1F1F2}\u{1F1F9}" },
  { code: "MD", name: "Moldavië", flag: "\u{1F1F2}\u{1F1E9}" },
  { code: "MC", name: "Monaco", flag: "\u{1F1F2}\u{1F1E8}" },
  { code: "ME", name: "Montenegro", flag: "\u{1F1F2}\u{1F1EA}" },
  { code: "NL", name: "Nederland", flag: "\u{1F1F3}\u{1F1F1}" },
  { code: "MK", name: "Noord-Macedonië", flag: "\u{1F1F2}\u{1F1F0}" },
  { code: "NO", name: "Noorwegen", flag: "\u{1F1F3}\u{1F1F4}" },
  { code: "PL", name: "Polen", flag: "\u{1F1F5}\u{1F1F1}" },
  { code: "PT", name: "Portugal", flag: "\u{1F1F5}\u{1F1F9}" },
  { code: "RO", name: "Roemenië", flag: "\u{1F1F7}\u{1F1F4}" },
  { code: "RU", name: "Rusland", flag: "\u{1F1F7}\u{1F1FA}" },
  { code: "SM", name: "San Marino", flag: "\u{1F1F8}\u{1F1F2}" },
  { code: "RS", name: "Servië", flag: "\u{1F1F7}\u{1F1F8}" },
  { code: "SK", name: "Slowakije", flag: "\u{1F1F8}\u{1F1F0}" },
  { code: "SI", name: "Slovenië", flag: "\u{1F1F8}\u{1F1EE}" },
  { code: "ES", name: "Spanje", flag: "\u{1F1EA}\u{1F1F8}" },
  { code: "SE", name: "Zweden", flag: "\u{1F1F8}\u{1F1EA}" },
  { code: "CH", name: "Zwitserland", flag: "\u{1F1E8}\u{1F1ED}" },
  { code: "UA", name: "Oekraïne", flag: "\u{1F1FA}\u{1F1E6}" },
  { code: "GB", name: "Verenigd Koninkrijk", flag: "\u{1F1EC}\u{1F1E7}" },

  // Noord-Amerika
  { code: "AG", name: "Antigua en Barbuda", flag: "\u{1F1E6}\u{1F1EC}" },
  { code: "BS", name: "Bahama's", flag: "\u{1F1E7}\u{1F1F8}" },
  { code: "BB", name: "Barbados", flag: "\u{1F1E7}\u{1F1E7}" },
  { code: "BZ", name: "Belize", flag: "\u{1F1E7}\u{1F1FF}" },
  { code: "CA", name: "Canada", flag: "\u{1F1E8}\u{1F1E6}" },
  { code: "CR", name: "Costa Rica", flag: "\u{1F1E8}\u{1F1F7}" },
  { code: "CU", name: "Cuba", flag: "\u{1F1E8}\u{1F1FA}" },
  { code: "DM", name: "Dominica", flag: "\u{1F1E9}\u{1F1F2}" },
  { code: "DO", name: "Dominicaanse Republiek", flag: "\u{1F1E9}\u{1F1F4}" },
  { code: "SV", name: "El Salvador", flag: "\u{1F1F8}\u{1F1FB}" },
  { code: "GD", name: "Grenada", flag: "\u{1F1EC}\u{1F1E9}" },
  { code: "GT", name: "Guatemala", flag: "\u{1F1EC}\u{1F1F9}" },
  { code: "HT", name: "Haïti", flag: "\u{1F1ED}\u{1F1F9}" },
  { code: "HN", name: "Honduras", flag: "\u{1F1ED}\u{1F1F3}" },
  { code: "JM", name: "Jamaica", flag: "\u{1F1EF}\u{1F1F2}" },
  { code: "MX", name: "Mexico", flag: "\u{1F1F2}\u{1F1FD}" },
  { code: "NI", name: "Nicaragua", flag: "\u{1F1F3}\u{1F1EE}" },
  { code: "PA", name: "Panama", flag: "\u{1F1F5}\u{1F1E6}" },
  { code: "KN", name: "Saint Kitts en Nevis", flag: "\u{1F1F0}\u{1F1F3}" },
  { code: "LC", name: "Saint Lucia", flag: "\u{1F1F1}\u{1F1E8}" },
  { code: "VC", name: "Saint Vincent en de Grenadines", flag: "\u{1F1FB}\u{1F1E8}" },
  { code: "TT", name: "Trinidad en Tobago", flag: "\u{1F1F9}\u{1F1F9}" },
  { code: "US", name: "Verenigde Staten", flag: "\u{1F1FA}\u{1F1F8}" },

  // Zuid-Amerika
  { code: "AR", name: "Argentinië", flag: "\u{1F1E6}\u{1F1F7}" },
  { code: "BO", name: "Bolivia", flag: "\u{1F1E7}\u{1F1F4}" },
  { code: "BR", name: "Brazilië", flag: "\u{1F1E7}\u{1F1F7}" },
  { code: "CL", name: "Chili", flag: "\u{1F1E8}\u{1F1F1}" },
  { code: "CO", name: "Colombia", flag: "\u{1F1E8}\u{1F1F4}" },
  { code: "EC", name: "Ecuador", flag: "\u{1F1EA}\u{1F1E8}" },
  { code: "GY", name: "Guyana", flag: "\u{1F1EC}\u{1F1FE}" },
  { code: "PY", name: "Paraguay", flag: "\u{1F1F5}\u{1F1FE}" },
  { code: "PE", name: "Peru", flag: "\u{1F1F5}\u{1F1EA}" },
  { code: "SR", name: "Suriname", flag: "\u{1F1F8}\u{1F1F7}" },
  { code: "UY", name: "Uruguay", flag: "\u{1F1FA}\u{1F1FE}" },
  { code: "VE", name: "Venezuela", flag: "\u{1F1FB}\u{1F1EA}" },

  // Midden-Oosten
  { code: "BH", name: "Bahrein", flag: "\u{1F1E7}\u{1F1ED}" },
  { code: "IQ", name: "Irak", flag: "\u{1F1EE}\u{1F1F6}" },
  { code: "IR", name: "Iran", flag: "\u{1F1EE}\u{1F1F7}" },
  { code: "IL", name: "Israël", flag: "\u{1F1EE}\u{1F1F1}" },
  { code: "JO", name: "Jordanië", flag: "\u{1F1EF}\u{1F1F4}" },
  { code: "KW", name: "Koeweit", flag: "\u{1F1F0}\u{1F1FC}" },
  { code: "LB", name: "Libanon", flag: "\u{1F1F1}\u{1F1E7}" },
  { code: "OM", name: "Oman", flag: "\u{1F1F4}\u{1F1F2}" },
  { code: "PS", name: "Palestina", flag: "\u{1F1F5}\u{1F1F8}" },
  { code: "QA", name: "Qatar", flag: "\u{1F1F6}\u{1F1E6}" },
  { code: "SA", name: "Saoedi-Arabië", flag: "\u{1F1F8}\u{1F1E6}" },
  { code: "SY", name: "Syrië", flag: "\u{1F1F8}\u{1F1FE}" },
  { code: "AE", name: "Verenigde Arabische Emiraten", flag: "\u{1F1E6}\u{1F1EA}" },
  { code: "YE", name: "Jemen", flag: "\u{1F1FE}\u{1F1EA}" },

  // Azië
  { code: "AF", name: "Afghanistan", flag: "\u{1F1E6}\u{1F1EB}" },
  { code: "AM", name: "Armenië", flag: "\u{1F1E6}\u{1F1F2}" },
  { code: "AZ", name: "Azerbeidzjan", flag: "\u{1F1E6}\u{1F1FF}" },
  { code: "BD", name: "Bangladesh", flag: "\u{1F1E7}\u{1F1E9}" },
  { code: "BT", name: "Bhutan", flag: "\u{1F1E7}\u{1F1F9}" },
  { code: "BN", name: "Brunei", flag: "\u{1F1E7}\u{1F1F3}" },
  { code: "KH", name: "Cambodja", flag: "\u{1F1F0}\u{1F1ED}" },
  { code: "CN", name: "China", flag: "\u{1F1E8}\u{1F1F3}" },
  { code: "GE", name: "Georgië", flag: "\u{1F1EC}\u{1F1EA}" },
  { code: "HK", name: "Hongkong", flag: "\u{1F1ED}\u{1F1F0}" },
  { code: "IN", name: "India", flag: "\u{1F1EE}\u{1F1F3}" },
  { code: "ID", name: "Indonesië", flag: "\u{1F1EE}\u{1F1E9}" },
  { code: "JP", name: "Japan", flag: "\u{1F1EF}\u{1F1F5}" },
  { code: "KZ", name: "Kazachstan", flag: "\u{1F1F0}\u{1F1FF}" },
  { code: "KG", name: "Kirgizië", flag: "\u{1F1F0}\u{1F1EC}" },
  { code: "LA", name: "Laos", flag: "\u{1F1F1}\u{1F1E6}" },
  { code: "MO", name: "Macau", flag: "\u{1F1F2}\u{1F1F4}" },
  { code: "MY", name: "Maleisië", flag: "\u{1F1F2}\u{1F1FE}" },
  { code: "MV", name: "Maldiven", flag: "\u{1F1F2}\u{1F1FB}" },
  { code: "MN", name: "Mongolië", flag: "\u{1F1F2}\u{1F1F3}" },
  { code: "MM", name: "Myanmar", flag: "\u{1F1F2}\u{1F1F2}" },
  { code: "NP", name: "Nepal", flag: "\u{1F1F3}\u{1F1F5}" },
  { code: "KP", name: "Noord-Korea", flag: "\u{1F1F0}\u{1F1F5}" },
  { code: "PK", name: "Pakistan", flag: "\u{1F1F5}\u{1F1F0}" },
  { code: "PH", name: "Filipijnen", flag: "\u{1F1F5}\u{1F1ED}" },
  { code: "SG", name: "Singapore", flag: "\u{1F1F8}\u{1F1EC}" },
  { code: "KR", name: "Zuid-Korea", flag: "\u{1F1F0}\u{1F1F7}" },
  { code: "LK", name: "Sri Lanka", flag: "\u{1F1F1}\u{1F1F0}" },
  { code: "TW", name: "Taiwan", flag: "\u{1F1F9}\u{1F1FC}" },
  { code: "TJ", name: "Tadzjikistan", flag: "\u{1F1F9}\u{1F1EF}" },
  { code: "TH", name: "Thailand", flag: "\u{1F1F9}\u{1F1ED}" },
  { code: "TL", name: "Oost-Timor", flag: "\u{1F1F9}\u{1F1F1}" },
  { code: "TM", name: "Turkmenistan", flag: "\u{1F1F9}\u{1F1F2}" },
  { code: "TR", name: "Turkije", flag: "\u{1F1F9}\u{1F1F7}" },
  { code: "UZ", name: "Oezbekistan", flag: "\u{1F1FA}\u{1F1FF}" },
  { code: "VN", name: "Vietnam", flag: "\u{1F1FB}\u{1F1F3}" },

  // Afrika
  { code: "DZ", name: "Algerije", flag: "\u{1F1E9}\u{1F1FF}" },
  { code: "AO", name: "Angola", flag: "\u{1F1E6}\u{1F1F4}" },
  { code: "BJ", name: "Benin", flag: "\u{1F1E7}\u{1F1EF}" },
  { code: "BW", name: "Botswana", flag: "\u{1F1E7}\u{1F1FC}" },
  { code: "BF", name: "Burkina Faso", flag: "\u{1F1E7}\u{1F1EB}" },
  { code: "BI", name: "Burundi", flag: "\u{1F1E7}\u{1F1EE}" },
  { code: "CV", name: "Kaapverdië", flag: "\u{1F1E8}\u{1F1FB}" },
  { code: "CM", name: "Kameroen", flag: "\u{1F1E8}\u{1F1F2}" },
  { code: "CF", name: "Centraal-Afrikaanse Republiek", flag: "\u{1F1E8}\u{1F1EB}" },
  { code: "TD", name: "Tsjaad", flag: "\u{1F1F9}\u{1F1E9}" },
  { code: "KM", name: "Comoren", flag: "\u{1F1F0}\u{1F1F2}" },
  { code: "CD", name: "Congo (DRC)", flag: "\u{1F1E8}\u{1F1E9}" },
  { code: "CG", name: "Congo (Republiek)", flag: "\u{1F1E8}\u{1F1EC}" },
  { code: "CI", name: "Ivoorkust", flag: "\u{1F1E8}\u{1F1EE}" },
  { code: "DJ", name: "Djibouti", flag: "\u{1F1E9}\u{1F1EF}" },
  { code: "EG", name: "Egypte", flag: "\u{1F1EA}\u{1F1EC}" },
  { code: "GQ", name: "Equatoriaal-Guinea", flag: "\u{1F1EC}\u{1F1F6}" },
  { code: "ER", name: "Eritrea", flag: "\u{1F1EA}\u{1F1F7}" },
  { code: "SZ", name: "Eswatini", flag: "\u{1F1F8}\u{1F1FF}" },
  { code: "ET", name: "Ethiopië", flag: "\u{1F1EA}\u{1F1F9}" },
  { code: "GA", name: "Gabon", flag: "\u{1F1EC}\u{1F1E6}" },
  { code: "GM", name: "Gambia", flag: "\u{1F1EC}\u{1F1F2}" },
  { code: "GH", name: "Ghana", flag: "\u{1F1EC}\u{1F1ED}" },
  { code: "GN", name: "Guinee", flag: "\u{1F1EC}\u{1F1F3}" },
  { code: "GW", name: "Guinee-Bissau", flag: "\u{1F1EC}\u{1F1FC}" },
  { code: "KE", name: "Kenia", flag: "\u{1F1F0}\u{1F1EA}" },
  { code: "LS", name: "Lesotho", flag: "\u{1F1F1}\u{1F1F8}" },
  { code: "LR", name: "Liberia", flag: "\u{1F1F1}\u{1F1F7}" },
  { code: "LY", name: "Libië", flag: "\u{1F1F1}\u{1F1FE}" },
  { code: "MG", name: "Madagaskar", flag: "\u{1F1F2}\u{1F1EC}" },
  { code: "MW", name: "Malawi", flag: "\u{1F1F2}\u{1F1FC}" },
  { code: "ML", name: "Mali", flag: "\u{1F1F2}\u{1F1F1}" },
  { code: "MR", name: "Mauritanië", flag: "\u{1F1F2}\u{1F1F7}" },
  { code: "MU", name: "Mauritius", flag: "\u{1F1F2}\u{1F1FA}" },
  { code: "MA", name: "Marokko", flag: "\u{1F1F2}\u{1F1E6}" },
  { code: "MZ", name: "Mozambique", flag: "\u{1F1F2}\u{1F1FF}" },
  { code: "NA", name: "Namibië", flag: "\u{1F1F3}\u{1F1E6}" },
  { code: "NE", name: "Niger", flag: "\u{1F1F3}\u{1F1EA}" },
  { code: "NG", name: "Nigeria", flag: "\u{1F1F3}\u{1F1EC}" },
  { code: "RW", name: "Rwanda", flag: "\u{1F1F7}\u{1F1FC}" },
  { code: "ST", name: "Sao Tomé en Principe", flag: "\u{1F1F8}\u{1F1F9}" },
  { code: "SN", name: "Senegal", flag: "\u{1F1F8}\u{1F1F3}" },
  { code: "SC", name: "Seychellen", flag: "\u{1F1F8}\u{1F1E8}" },
  { code: "SL", name: "Sierra Leone", flag: "\u{1F1F8}\u{1F1F1}" },
  { code: "SO", name: "Somalië", flag: "\u{1F1F8}\u{1F1F4}" },
  { code: "ZA", name: "Zuid-Afrika", flag: "\u{1F1FF}\u{1F1E6}" },
  { code: "SS", name: "Zuid-Soedan", flag: "\u{1F1F8}\u{1F1F8}" },
  { code: "SD", name: "Soedan", flag: "\u{1F1F8}\u{1F1E9}" },
  { code: "TZ", name: "Tanzania", flag: "\u{1F1F9}\u{1F1FF}" },
  { code: "TG", name: "Togo", flag: "\u{1F1F9}\u{1F1EC}" },
  { code: "TN", name: "Tunesië", flag: "\u{1F1F9}\u{1F1F3}" },
  { code: "UG", name: "Oeganda", flag: "\u{1F1FA}\u{1F1EC}" },
  { code: "ZM", name: "Zambia", flag: "\u{1F1FF}\u{1F1F2}" },
  { code: "ZW", name: "Zimbabwe", flag: "\u{1F1FF}\u{1F1FC}" },

  // Oceanië
  { code: "AU", name: "Australië", flag: "\u{1F1E6}\u{1F1FA}" },
  { code: "FJ", name: "Fiji", flag: "\u{1F1EB}\u{1F1EF}" },
  { code: "NZ", name: "Nieuw-Zeeland", flag: "\u{1F1F3}\u{1F1FF}" },
  { code: "PG", name: "Papoea-Nieuw-Guinea", flag: "\u{1F1F5}\u{1F1EC}" },
  { code: "WS", name: "Samoa", flag: "\u{1F1FC}\u{1F1F8}" },
  { code: "TO", name: "Tonga", flag: "\u{1F1F9}\u{1F1F4}" },
  { code: "VU", name: "Vanuatu", flag: "\u{1F1FB}\u{1F1FA}" },
];

// Bouw lookup-objecten vanuit de COUNTRIES array
const COUNTRY_MAP = {};
COUNTRIES.forEach((c) => { COUNTRY_MAP[c.code] = c; });

// Valuta symbolen mapping (uitgebreid)
const CURRENCY_SYMBOLS = {
  EUR: "€", USD: "$", GBP: "£", CAD: "C$", INR: "₹",
  JPY: "¥", CNY: "¥", BRL: "R$", AUD: "A$", TRY: "₺",
  IDR: "Rp", MXN: "MX$", CHF: "Fr", SEK: "kr", NOK: "kr",
  DKK: "kr", PLN: "zł", CZK: "Kč", HUF: "Ft", RON: "lei",
  BGN: "лв", HRK: "kn", RUB: "₽", UAH: "₴", GEL: "₾",
  AED: "د.إ", SAR: "﷼", QAR: "﷼", KWD: "د.ك", BHD: "BD",
  OMR: "﷼", JOD: "JD", ILS: "₪", EGP: "E£", MAD: "MAD",
  TND: "DT", NGN: "₦", KES: "KSh", GHS: "GH₵", ZAR: "R",
  KRW: "₩", THB: "฿", VND: "₫", PHP: "₱", MYR: "RM",
  SGD: "S$", TWD: "NT$", PKR: "₨", BDT: "৳", LKR: "Rs",
  NZD: "NZ$", ARS: "AR$", CLP: "CL$", COP: "CO$", PEN: "S/.",
  UYU: "$U", VES: "Bs.", BOB: "Bs", PYG: "₲", CRC: "₡",
  PAB: "B/.", DOP: "RD$", GTQ: "Q", HNL: "L", NIO: "C$",
  JMD: "J$", TTD: "TT$", XAF: "FCFA", XOF: "CFA",
};

function currencySymbol(code) {
  return CURRENCY_SYMBOLS[code] || code;
}

function countryFlag(code) {
  const c = COUNTRY_MAP[code];
  return c ? c.flag : "";
}

function countryName(code) {
  if (!code) return "";
  const c = COUNTRY_MAP[code];
  return c ? `${c.flag} ${c.name}` : code;
}

function countryNameOnly(code) {
  if (!code) return "";
  const c = COUNTRY_MAP[code];
  return c ? c.name : code;
}

// --- Vul de land-dropdowns dynamisch ---
function populateCountrySelects() {
  const selects = document.querySelectorAll("#originCountry, #storeCountry");
  // Sorteer op naam voor de dropdown
  const sorted = [...COUNTRIES].sort((a, b) => a.name.localeCompare(b.name, "nl"));

  selects.forEach((select) => {
    // Bewaar de eerste "Selecteer..." optie
    const placeholder = select.querySelector("option");
    select.innerHTML = "";
    select.appendChild(placeholder);

    sorted.forEach((c) => {
      const opt = document.createElement("option");
      opt.value = c.code;
      opt.textContent = `${c.flag} ${c.name}`;
      select.appendChild(opt);
    });
  });
}

populateCountrySelects();

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
        <span class="name">${p.origin_country ? countryFlag(p.origin_country) + " " : ""}${p.name}</span>
        ${p.brand ? `<span class="meta"> &mdash; ${p.brand}</span>` : ""}
        ${p.origin_country ? `<span class="meta country-tag">${countryNameOnly(p.origin_country)}</span>` : ""}
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

  const sym = currencySymbol(data.currency);
  const flag = data.product.origin_country ? countryFlag(data.product.origin_country) + " " : "";
  const countryInfo = data.product.origin_country
    ? ` — ${countryName(data.product.origin_country)}`
    : "";

  document.getElementById("productTitle").textContent =
    `${flag}${data.product.name}${data.product.brand ? " (" + data.product.brand + ")" : ""}${countryInfo}`;

  document.getElementById("currentPrice").textContent = data.current_price
    ? `${sym}${data.current_price.toFixed(2)}`
    : "-";

  document.getElementById("oldestPrice").textContent = data.oldest_price
    ? `${sym}${data.oldest_price.toFixed(2)}`
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
  drawChart(data.history, data.currency);

  // Scroll naar de grafiek
  section.scrollIntoView({ behavior: "smooth" });
}

function drawChart(history, currency) {
  const ctx = document.getElementById("priceChart").getContext("2d");
  const sym = currencySymbol(currency);

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
          label: `Prijs (${sym})`,
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
              const pointSym = currencySymbol(point.currency);
              let label = `${pointSym}${ctx.parsed.y.toFixed(2)}`;
              if (point.store_name) label += ` (${point.store_name})`;
              if (point.country_code) label += ` [${countryFlag(point.country_code)} ${countryNameOnly(point.country_code)}]`;
              return label;
            },
          },
        },
      },
      scales: {
        y: {
          beginAtZero: false,
          ticks: {
            callback: (value) => `${sym}${value.toFixed(2)}`,
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
  const originCountry = document.getElementById("originCountry").value || null;
  const storeName = document.getElementById("storeName").value.trim();
  const storeCountry = document.getElementById("storeCountry").value || null;
  const price = parseFloat(document.getElementById("productPrice").value);
  const currency = document.getElementById("priceCurrency").value;
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
        body: JSON.stringify({ name, barcode, category, origin_country: originCountry }),
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
          body: JSON.stringify({ name: storeName, country_code: storeCountry }),
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
      currency: currency,
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

    const savedSym = currencySymbol(currency);
    msgEl.textContent = `Prijs van ${savedSym}${price.toFixed(2)} opgeslagen voor ${name}!`;
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
      (item) => {
        const sym = currencySymbol(item.currency || "EUR");
        const flag = item.country ? countryFlag(item.country) + " " : "";
        const country = item.country ? ` (${countryNameOnly(item.country)})` : "";
        return `
    <div class="inflation-item" onclick="showPriceHistory(${item.product_id})">
      <div>
        <span class="name">${flag}${item.product_name}${country}</span>
        <span class="prices">${sym}${item.oldest_price.toFixed(2)} → ${sym}${item.current_price.toFixed(2)}</span>
      </div>
      <span class="change-badge ${item.change_percent < 0 ? "deflation" : ""}">
        ${item.change_percent > 0 ? "+" : ""}${item.change_percent}%
      </span>
    </div>
  `;
      }
    )
    .join("");
}

// Laad top inflatie bij pagina-laden
loadTopInflation();
