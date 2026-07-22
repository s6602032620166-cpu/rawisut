import math
import streamlit as st

st.set_page_config(
    page_title="🏗️Ground Improvement",
    layout="wide"
)

st.markdown("""
<style>

/* ==========================
   Background
========================== */
.stApp{
    background-color:#F5F7FA;
}

/* ==========================
   Main Title & Headers
========================== */

h1{
    color:#1E3A5F !important;
    font-weight:700;
}

h2,h3{
    color:#1E3A5F !important;
    font-weight:600;
}

/* ==========================
   Body Text
========================== */

p,
label,
span,
small,
li,
div,
.stMarkdown,
.stCaption{
    color:#6B4F3A !important;
}

/* ==========================
   Input Labels
========================== */

.stSelectbox label,
.stNumberInput label,
.stRadio label{
    color:#6B4F3A !important;
    font-weight:600;
}

/* ==========================
   Metric Card
========================== */

div[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
}

div[data-testid="stMetricLabel"]{
    color:#6B4F3A !important;
}

div[data-testid="stMetricValue"]{
    color:#6B4F3A !important;
}

/* ==========================
   Success / Info / Error
========================== */

div[data-testid="stAlert"]{
    border-radius:10px;
    font-weight:600;
}

/* ==========================
   Sidebar
========================== */

section[data-testid="stSidebar"]{
    background:#1E3A5F;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

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

    Kr = st.number_input("Kr", value=7.0)
    Kv = st.number_input("Kv", value=1.0)
    Cv = st.number_input("Cv (cm²/day)", value=20)

    if Kv != 0:
        Cr = (Kr/Kv)*Cv
    else:
        Cr = 0

    st.info(f"Cr = {Cr:.4f}")

    st.divider()

    t = st.number_input(
        "Time (days)",
        value=90.0
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
        Tr = (Cr * t) / ((De*100)**2)
    else:
        Tr = 0
    
    st.success(f"Tr = {Tr:.4f}")

    Ur = 1 - math.exp(-8 * Tr / Fn)

    st.metric("Degree of Consolidation",
    f"{Ur*100:.2f} %"
    )

    if Ur >= 0.9:
        st.success("✅ Result : PASS (ผ่านเกณฑ์ เนื่องจาก Degree of Consolidation ≥ 90.00%)")
    else:
        st.error("❌ Result : FAIL (ไม่ผ่านเกณฑ์ เนื่องจาก Degree of Consolidation < 90.00%)")

# =====================================================

elif menu == "Dynamic Compaction":

    st.header("Coming Soon")

elif menu == "Geotextile":

    st.header("Coming Soon")
