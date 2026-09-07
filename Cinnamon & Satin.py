import streamlit as st

# --- 1. กำหนดชื่อร้านค้า ---
shop_name = "Cinnamon & Satin"
st.title(f"🥐 ร้าน {shop_name}")
st.subheader("ระบบคิดเงินและคำนวณส่วนลด")

# --- 2. แสดงรายการสินค้าและราคา ---
price_bagel = 30
price_cake = 50
price_croissant = 25
price_cookie = 15

st.markdown("### 📋 เลือกจำนวนสินค้า")
col1, col2 = st.columns(2)

with col1:
    qty_bagel = st.number_input(f"เบเกิล ({price_bagel} บาท)", min_value=0, value=0, step=1)
    qty_cake = st.number_input(f"เค้ก ({price_cake} บาท)", min_value=0, value=0, step=1)

with col2:
    qty_croissant = st.number_input(f"ครัวซอง ({price_croissant} บาท)", min_value=0, value=0, step=1)
    qty_cookie = st.number_input(f"คุกกี้ ({price_cookie} บาท)", min_value=0, value=0, step=1)

# --- 3. คำนวณราคารวม ---
total_price = (qty_bagel * price_bagel) + (qty_cake * price_cake) + (qty_croissant * price_croissant) + (qty_cookie * price_cookie)

# --- 4. เงื่อนไขโปรโมชั่น ---
st.markdown("---")
st.markdown("### 🎁 รูปแบบการทาน")
dine_in = st.radio("เลือกสถานที่ทาน:", ["ทานในร้าน (ลด 10 บาท)", "นำกลับบ้าน"])

discount = 0

# โปรโมชั่น 1: ซื้ออย่างละ 1 ชิ้นขึ้นไป ลด 20 บาท
if qty_bagel >= 1 and qty_cake >= 1 and qty_croissant >= 1 and qty_cookie >= 1:
    discount += 20
    st.success("🎉 คุณได้รับส่วนลดโปรโมชั่นซื้อครบทุกอย่าง 20 บาท!")

# โปรโมชั่น 2: ทานในร้าน ลด 10 บาท
if dine_in == "ทานในร้าน (ลด 10 บาท)":
    discount += 10

final_price = max(0, total_price - discount)

# --- 5. แสดงสรุปและคิดเงินทอน ---
st.markdown("---")
st.markdown("### 💵 สรุปรายการ")
st.write(f"**ราคารวมทั้งหมด:** {total_price:.2f} บาท")
st.write(f"**ส่วนลดรวม:** {discount:.2f} บาท")
st.markdown(f"### **ยอดที่ต้องจ่ายจริง: {final_price:.2f} บาท**")

cash = st.number_input("กรอกจำนวนเงินที่รับจากลูกค้า (บาท):", min_value=0.0, step=10.0)

if st.button("คำนวณเงินทอน"):
    if cash >= final_price:
        change = cash - final_price
        st.balloons()
        st.success(f"💰 เงินทอน: {change:.2f} บาท")
        st.info(f"ขอบคุณที่อุดหนุนร้าน {shop_name} ครับ/ค่ะ!")
    else:
        st.error(f"❌ จำนวนเงินไม่พอ! ขาดอีก {final_price - cash:.2f} บาท")
