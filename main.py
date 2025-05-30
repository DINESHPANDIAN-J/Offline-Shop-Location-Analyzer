# shop_location_analyzer.py

import streamlit as st
st.set_page_config(page_title="Best Shop Location Finder", layout="wide")  # ✅ MUST BE FIRST STREAMLIT COMMAND

import osmnx as ox
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- CONFIGURATION ---
POI_CATEGORIES = {
    "school": 0.8, "college": 1.2, "university": 1.2, "kindergarten": 0.5,
    "bus_station": 1.0, "bus_stop": 0.7, "taxi": 0.4, "parking": 0.3,
    "pharmacy": 0.6, "clinic": 0.7, "hospital": 1.0,
    "supermarket": 1.0, "mall": 2.0, "convenience": 0.6, "department_store": 1.5,
    "clothes": 1.0, "bakery": 0.8, "beauty": 0.7, "hairdresser": 0.6,
    "marketplace": 1.8, "jewelry": 1.0,
    "bank": 0.6, "atm": 0.2, "post_office": 0.4, "internet_cafe": 0.3,
    "cinema": 1.5, "theatre": 1.2, "museum": 1.2, "place_of_worship": 0.6,
    "monument": 0.6, "viewpoint": 0.5,
    "park": 0.4, "beach_resort": 1.5, "beach": 1.2, "zoo": 1.2
}

# --- SIDEBAR INPUT ---
radius = st.sidebar.slider(
    "📏 Select radius for analysis (in meters)",
    min_value=100,
    max_value=2000,
    value=500,
    step=100,
    help="Defines how far out POIs will be considered from the clicked point."
)

# --- FUNCTIONS ---
def get_pois(lat, lon, radius):
    tags = {
        "amenity": list(POI_CATEGORIES.keys()),
        "shop": True,
        "building": ["retail"]
    }
    return ox.features_from_point((lat, lon), tags=tags, dist=radius)

def score_location(pois):
    score = 0.0
    for cat, weight in POI_CATEGORIES.items():
        count = len(pois[pois["amenity"] == cat])
        score += count * weight
    return round(score, 2)

# --- SESSION STATE SETUP ---
if "selected_lat" not in st.session_state:
    st.session_state["selected_lat"] = None
    st.session_state["selected_lon"] = None

# --- UI SETUP ---
st.title("📍 Offline Shop Location Analyzer")
st.markdown("### 👉 Click anywhere on the map to evaluate location potential")

# --- MAP SETUP ---
map_center = [11.936, 79.835]
folium_map = folium.Map(location=map_center, zoom_start=14)

# Draw circle if previous location exists
if st.session_state["selected_lat"] is not None:
    folium.Circle(
        location=(st.session_state["selected_lat"], st.session_state["selected_lon"]),
        radius=radius,
        color='red',
        fill=True,
        fill_opacity=0.2,
        tooltip=f"Selected Area ({radius}m)"
    ).add_to(folium_map)

# Render map
st_data = st_folium(folium_map, width=1000, height=500)

# --- HANDLE CLICK ---
if st_data and st_data.get("last_clicked"):
    lat = st_data["last_clicked"]["lat"]
    lon = st_data["last_clicked"]["lng"]

    # Update session state
    st.session_state["selected_lat"] = lat
    st.session_state["selected_lon"] = lon

    st.rerun()  # ✅ this is correct now — do not use experimental_rerun

# --- ANALYSIS ---
if st.session_state["selected_lat"] is not None:
    lat = st.session_state["selected_lat"]
    lon = st.session_state["selected_lon"]

    st.markdown(f"**Latitude:** `{lat:.5f}` &nbsp;&nbsp;&nbsp;&nbsp; **Longitude:** `{lon:.5f}`")

    try:
        pois = get_pois(lat, lon, radius)
        score = score_location(pois)
        st.success(f"✅ Footfall Score: `{score}` (within {radius} meters)")

        breakdown = []
        for cat, weight in POI_CATEGORIES.items():
            count = len(pois[pois["amenity"] == cat])
            if count > 0:
                breakdown.append({
                    "Category": cat,
                    "Count": count,
                    "Weight": weight,
                    "Weighted Score": round(count * weight, 2)
                })

        st.markdown("### 🧾 Nearby POIs by Category")
        st.dataframe(pd.DataFrame(breakdown).sort_values("Weighted Score", ascending=False))

        if st.sidebar.checkbox("Show raw POI data"):
            st.dataframe(pois[["amenity", "name"]].dropna())

    except Exception as e:
        st.error(f"⚠️ Failed to analyze location: {e}")

st.caption("🔍 Powered by OpenStreetMap, OSMnx, and Streamlit. No paid APIs used.")