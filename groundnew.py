import streamlit as st
from pathlib import Path

# ==========================
# Page Config
# ==========================
st.set_page_config(
    page_title="Ground Improvement Design",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Load CSS
# ==========================
css_file = Path("styles/style.css")

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================
# Header
# ==========================

st.title("🏗️ Ground Improvement Design")
st.caption("ASTM • AASHTO • Soil Improvement Engineering")

st.divider()

# ==========================
# Sidebar
# ==========================

st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

st.sidebar.markdown("## Ground Improvement")

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏗️ Home",
        "📍 PVD",
        "⚒️ Dynamic Compaction",
        "🧱 Geotextile",
        "ℹ️ About"
    ]
)

# ==========================
# HOME
# ==========================

if menu == "🏗️ Home":

    st.image(
        "assets/background.jpg",
        use_container_width=True
    )

    st.markdown(
        """
        ## Welcome

        Ground Improvement Design Program

        This software is developed for geotechnical engineers based on ASTM and AASHTO standards.

        ### Available Modules

        - Prefabricated Vertical Drain (PVD)
        - Dynamic Compaction
        - Geotextile Design
        """
    )

# ==========================
# PVD
# ==========================

elif menu == "📍 PVD":

    from modules.pvd import pvd_page

    pvd_page()

# ==========================
# Dynamic
# ==========================

elif menu == "⚒️ Dynamic Compaction":

    from modules.dynamic_compaction import dynamic_page

    dynamic_page()

# ==========================
# Geotextile
# ==========================

elif menu == "🧱 Geotextile":

    from modules.geotextile import geotextile_page

    geotextile_page()

# ==========================
# About
# ==========================

elif menu == "ℹ️ About":

    st.header("About")

    st.write("""
Ground Improvement Design

Version 1.0

Developed by Rawisu Lhekka

Based on ASTM / AASHTO

Python + Streamlit
""")
