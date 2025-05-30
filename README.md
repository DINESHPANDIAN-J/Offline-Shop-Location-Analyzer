
# 🛍️ Offline Shop Location Analyzer

A Streamlit-based interactive tool that helps you find the most strategic location for opening an offline shop based on nearby Points of Interest (POIs) and their footfall potential. Powered by OpenStreetMap, OSMnx, and Folium — no paid APIs required!

---

## 🚀 Features

* 🔍 Click anywhere on the map to analyze footfall potential.
* 🎯 Radius-based POI search (customizable from 100m to 2000m).
* 📊 Weighted scoring system based on proximity to high-traffic POIs like malls, colleges, bus stations, etc.
* 📍 Instant visualization of the selected area.
* 📑 POI breakdown table and raw data explorer.
* 🌐 No paid services or tokens needed — open source and free.

---

## 🛠️ Tech Stack

| Layer             | Tech Used                |
| ----------------- | ------------------------ |
| 🧠 Backend Logic  | Python, pandas           |
| 🌍 Geospatial API | OSMnx, OpenStreetMap     |
| 🗺️ Map Interface | folium, streamlit-folium |
| 🖥️ UI Frontend   | Streamlit                |

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/shop-location-analyzer.git
cd shop-location-analyzer
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv hc
source hc/bin/activate  # On Windows: hc\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚦 How to Run

```bash
streamlit run main.py
```

This will launch the app in your browser. Click on any point on the map to evaluate location potential.

---

## ⚙️ Customization

* 🧠 Change the POI weights in the POI\_CATEGORIES dictionary in main.py to match your business domain.
* 📍 Change the map's center location in map\_center = \[latitude, longitude].
* 📐 Adjust the default radius or step in the radius slider.

---

## 📈 Scoring Logic

Each nearby POI category is assigned a custom weight to reflect its potential contribution to footfall. For example:

| Category     | Weight |
| ------------ | ------ |
| mall         | 2.0    |
| university   | 1.2    |
| bus\_station | 1.0    |
| convenience  | 0.6    |
| atm          | 0.2    |

The final location score is a weighted sum of all POIs found within the selected radius.

---

## 🧪 Example Use Cases

* Identify best place to open a food stall near colleges or parks.
* Evaluate commercial potential of a vacant shop.
* Compare footfall scores across different neighborhoods.

---

## 📁 Folder Structure

```
.
├── main.py                  # Streamlit app script
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 💡 Roadmap

* 🔥 Heatmap overlay for POI density.
* 🧭 Add POI category filters (e.g. only educational, only retail).
* 🗺️ Export results to CSV or GeoJSON.
* 🏪 Business type presets (e.g., Clothing Shop, Pharmacy) with optimized weights/radius.

---

## 🤝 Contributing

Pull requests, suggestions, and forks are welcome! Let's improve this together.

---

## 📄 License

MIT License. Free to use and modify.

---

## 🙌 Acknowledgements

* OpenStreetMap contributors
* OSMnx by Geoff Boeing
* Streamlit and streamlit-folium libraries

---
