import streamlit as st
import math

# 1. ตั้งค่าหน้าเว็บให้เป็นแบบกว้าง (Wide Layout) และกำหนดชื่อ
st.set_page_config(page_title="PVD Calculator", layout="wide")

# 2. แทรก CSS เพื่อคุมโทนสี ขาว-น้ำตาล (Minimalist Earth Tone)
st.markdown("""
    <style>
    /* พื้นหลังสีขาวอมครีม */
    .stApp {
        background-color: #FAFAF9;
    }
    /* สีตัวอักษรหลักเป็นน้ำตาลเข้ม */
    html, body, [class*="css"]  {
        color: #44403C;
        font-family: 'Prompt', sans-serif;
    }
    /* ปรับแต่งกรอบและปุ่ม */
    div[data-testid="stMetricValue"] {
        color: #57534E;
    }
    .stProgress > div > div > div > div {
        background-color: #78716C; /* สีแถบ Progress Bar เป็นน้ำตาลเทา */
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนหัวของโปรแกรม
st.title("PVD Calculator | Minimalist Edition")
st.markdown("โปรแกรมคำนวณการระบายน้ำแนวรัศมี (Radial Consolidation)")
st.markdown("---")

# แบ่งหน้าจอเป็น 2 ฝั่ง: ซ้าย (Input 60%) และ ขวา (Output 40%)
col1, col2 = st.columns([6, 4])

with col1:
    st.subheader("📥 ข้อมูลการออกแบบ")
    
    # กรอกข้อมูลขนาดแผ่น PVD
    st.markdown("**1. ขนาดแผ่น PVD**")
    c1, c2 = st.columns(2)
    with c1:
        a = st.number_input("ความกว้าง, a (mm)", value=100.0, step=1.0)
    with c2:
        b = st.number_input("ความหนา, b (mm)", value=5.0, step=0.1)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # กรอกข้อมูลรูปแบบการติดตั้ง
    st.markdown("**2. รูปแบบการติดตั้ง**")
    c3, c4 = st.columns(2)
    with c3:
        S = st.number_input("ระยะห่าง, S (m)", value=1.0, step=0.1)
    with c4:
        pattern = st.selectbox("รูปแบบ (Pattern)", ["สามเหลี่ยม (Triangular)", "สี่เหลี่ยม (Square)"])

# 3. ลอจิกการคำนวณ (Glass Box: แสดงค่าระหว่างทาง)
# แปลงหน่วย a, b เป็นเมตร เพื่อความสม่ำเสมอ
a_m = a / 1000
b_m = b / 1000

# คำนวณ dw (Equivalent Diameter)
dw = (2 * (a_m + b_m)) / math.pi

# คำนวณ de (Influence Zone) ตามเงื่อนไข Pattern
if "สามเหลี่ยม" in pattern:
    de = 1.05 * S
else:
    de = 1.13 * S

# คำนวณ F(n)
Fn = math.log(de / dw) - 0.75

with col2:
    st.subheader("📊 ผลลัพธ์การคำนวณ")
    st.info("Step-by-Step Breakdown")
    
    # แสดงผลลัพธ์ทีละบรรทัดแบบคลีนๆ
    st.metric(label="เส้นผ่านศูนย์กลางเทียบเท่า (dw)", value=f"{dw * 1000:.2f} mm")
    st.metric(label="พื้นที่อิทธิพล (de)", value=f"{de:.3f} m")
    st.metric(label="ปัจจัยด้านระยะห่าง (F(n))", value=f"{Fn:.3f}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**ระดับการอัดตัวคายน้ำ ($U_r$) - จำลองที่ 75%**")
    st.progress(75) # แถบจำลองเปอร์เซ็นต์
    st.caption("อ้างอิงสมการ Hansbo (1979)")

st.markdown("---")

# 4. ส่วนแกลลอรีรูปภาพอุปกรณ์ (Equipment Gallery)
st.subheader("🏗️ อุปกรณ์และเครื่องจักรที่เกี่ยวข้อง (PVD Equipment)")
img_cols = st.columns(4)

with img_cols[0]:
    # สามารถเปลี่ยนลิงก์ URL เป็นรูปภาพของจริงได้เลย
    st.image("https://placehold.co/400x300/e7e5e4/57534E?text=Installation+Rig", use_column_width=True)
    st.markdown("**รถติดตั้ง (Installation Rig)**")
    st.caption("เครื่องจักรสำหรับกดท่อเหล็กนำร่องลงสู่ชั้นดินอ่อน")

with img_cols[1]:
    st.image("https://placehold.co/400x300/e7e5e4/57534E?text=Mandrel", use_column_width=True)
    st.markdown("**ท่อเหล็กนำร่อง (Mandrel)**")
    st.caption("ปกป้องแผ่น PVD จากการฉีกขาดและลด Smear Effect")

with img_cols[2]:
    st.image("https://placehold.co/400x300/e7e5e4/57534E?text=Anchor+Shoe", use_column_width=True)
    st.markdown("**แผ่นยึดปลาย (Anchor Shoe)**")
    st.caption("ยึดปลายแผ่น PVD ให้อยู่ในระดับความลึกที่ต้องการ")

with img_cols[3]:
    st.image("https://placehold.co/400x300/e7e5e4/57534E?text=PVD+Roll", use_column_width=True)
    st.markdown("**ม้วนวัสดุ (PVD Roll)**")
    st.caption("ประกอบด้วยแกนพลาสติกหุ้มด้วยแผ่นกรองใยสังเคราะห์")
