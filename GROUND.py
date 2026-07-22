import math
import streamlit as st

st.set_page_config(
    page_title="Ground Improvement",
    layout="wide"
)

st.title("Ground Improvement Design")
st.write("ASTM / AASHTO")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Dynamic Compaction",
        "PVD",
        "Geotextile"
    ]
)

# =====================================================
# PVD
# =====================================================

if menu == "PVD":

    st.header("Prefabricated Vertical Drain")

    pattern = st.selectbox(
        "Installation Pattern",
        [
            "Square (De = 1.13S)",
            "Triangular (De = 1.05S)"
        ]
    )

    S = st.number_input(
        "Drain Spacing S (m)",
        value=1.20
    )

    if pattern == "Square (De = 1.13S)":
        De = 1.13*S
    else:
        De = 1.05*S

    st.success(f"Equivalent Diameter De = {De:.3f} m")

    st.divider()

    st.subheader("Soil Parameters")

    Kr = st.number_input("Kr", value=1.0)
    Kv = st.number_input("Kv", value=1.0)
    Cv = st.number_input("Cv (m²/day)", value=0.01)

    if Kv != 0:
        Cr = Kr/Kv
    else:
        Cr = 0

    st.info(f"Cr = {Cr:.4f}")

    st.divider()

    t = st.number_input(
        "Time (days)",
        value=30.0
    )

    Hdr = st.number_input(
        "Drainage Path Hdr (m)",
        value=5.0
    )

    if Hdr > 0:
        Tr = Cv*t/(Hdr**2)
    else:
        Tr = 0

    st.success(f"Time Factor Tv = {Tr:.4f}")

    st.divider()

    st.subheader("Drain Dimension")

    a = st.number_input("Drain Width a (mm)", value=100.0)
    b = st.number_input("Drain Thickness b (mm)", value=4.0)

    Dw = (a+b)/2

    st.success(f"Dw = {Dw:.2f} mm")

    Dw_m = Dw/1000

    if Dw_m > 0:
        n = De/Dw_m
    else:
        n = 0

    st.success(f"n = {n:.3f}")

    if n > 1:
        Fn = math.log(n)-0.75
    else:
        Fn = 0

    st.success(f"Fn = {Fn:.4f}")

    if De > 0:
        Tr = (Cr * t) / (De**2)
    else:
        Tr = 0
    
    st.success(f"Tr = {Tr:.4f}")

    Ur = 1 - math.exp(-8 * Tr / Fn)

    st.success(f"Degree of Consolidation = {Ur:.2f}%")

# =====================================================

elif menu == "Dynamic Compaction":

    st.header("Coming Soon")

elif menu == "Geotextile":

    st.header("Coming Soon")
