# --- 1. กำหนดชื่อร้านค้า ---
shop_name = "Cinnamon & Satin"
print(f"=== ยินดีต้อนรับสู่ร้าน {shop_name} ===")

# --- 2. กำหนดราคาสินค้าแต่ละรายการ ---
price_bagel = 30
price_cake = 50
price_croissant = 25
price_cookie = 15

print("\n--- รายการสินค้า ---")
print(f"1. เบเกิล ({price_bagel} บาท)")
print(f"2. เค้ก ({price_cake} บาท)")
print(f"3. ครัวซอง ({price_croissant} บาท)")
print(f"4. คุกกี้ ({price_cookie} บาท)")

# --- รับจำนวนสินค้าแต่ละชนิดจากลูกค้า ---
print("\nกรุณากรอกจำนวนสินค้าที่ต้องการซื้อ:")
qty_bagel = int(input("จำนวนเบเกิล (ชิ้น): "))
qty_cake = int(input("จำนวนเค้ก (ชิ้น): "))
qty_croissant = int(input("จำนวนครัวซอง (ชิ้น): "))
qty_cookie = int(input("จำนวนคุกกี้ (ชิ้น): "))

# --- 3. คำนวณราคารวมทั้งหมด ---
total_price = (qty_bagel * price_bagel) + (qty_cake * price_cake) + (qty_croissant * price_croissant) + (qty_cookie * price_cookie)

# --- 4. เช็กเงื่อนไข If-Else เพื่อคำนวณส่วนลด ---
discount = 0

# โปรโมชั่น 1: ซื้ออย่างละอย่างน้อย 1 ชิ้น ลดราคา 20 บาท
if qty_bagel >= 1 and qty_cake >= 1 and qty_croissant >= 1 and qty_cookie >= 1:
    discount += 20
    print("\n* คุณได้รับส่วนลดโปรโมชั่นซื้อครบทุกอย่าง 20 บาท")

# โปรโมชั่น 2: ถ้าทานในร้าน ลดราคา 10 บาท
dine_in = input("ทานในร้านหรือนำกลับบ้าน? (1: ทานในร้าน / 2: นำกลับบ้าน): ").strip()
if dine_in == '1':
    discount += 10
    print("* คุณได้รับส่วนลดทานในร้าน 10 บาท")

# คำนวณราคาสุดธิหลังหักส่วนลด
final_price = total_price - discount
if final_price < 0:
    final_price = 0  # กันกรณีส่วนลดมากกว่าราคาสินค้า

# --- 5. แสดงสรุปยอดและรับเงินจากลูกค้าเพื่อคำนวณเงินทอน ---
print("\n" + "="*35)
print(f"ราคารวมทั้งหมด: {total_price:.2f} บาท")
print(f"ส่วนลดรวมที่ได้รับ: {discount:.2f} บาท")
print(f"ยอดเงินที่ต้องจ่ายจริง: {final_price:.2f} บาท")
print("="*35)

cash = float(input("\nกรอกจำนวนเงินที่รับจากลูกค้า: "))

if cash >= final_price:
    change = cash - final_price
    print(f"เงินทอน: {change:.2f} บาท")
    print(f"\nขอบคุณที่อุดหนุนร้าน {shop_name} ครับ/ค่ะ!")
else:
    print(f"จำนวนเงินไม่พอ! ขาดอีก {final_price - cash:.2f} บาท")
