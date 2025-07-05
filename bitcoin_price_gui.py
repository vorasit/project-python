
import tkinter as tk
import requests
import json
from datetime import datetime

# ฟังก์ชันสำหรับดึงข้อมูลราคาและอัตราแลกเปลี่ยน
def get_prices():
    """
    ดึงราคา BTC/USDT จาก Binance และอัตราแลกเปลี่ยน USD/THB
    คืนค่าเป็น tuple (ราคา BTC (float), อัตราแลกเปลี่ยน THB (float)) หรือ (None, None) หากผิดพลาด
    """
    btc_price = None
    thb_rate = None
    error_message = None

    # 1. ดึงราคา BTC/USDT จาก Binance
    try:
        btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(btc_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        btc_price = float(data['price'])
    except Exception as e:
        error_message = f"ผิดพลาด (BTC): {e}"
        print(error_message)
        return None, None, error_message

    # 2. ดึงอัตราแลกเปลี่ยน USD/THB
    try:
        # API นี้ใช้ USD เป็นฐานและดึงเรทของ THB
        rate_url = "https://api.frankfurter.app/latest?from=USD&to=THB"
        response = requests.get(rate_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        thb_rate = float(data['rates']['THB'])
    except Exception as e:
        error_message = f"ผิดพลาด (THB Rate): {e}"
        print(error_message)
        return None, None, error_message

    return btc_price, thb_rate, None

# ฟังก์ชันสำหรับอัปเดตราคาบน GUI
def update_price():
    """
    อัปเดตป้ายราคาทั้ง USD และ THB บนหน้าต่าง GUI
    """
    # แสดงสถานะกำลังโหลด
    price_usd_label.config(text="กำลังโหลด...", fg="black")
    price_thb_label.config(text="", fg="black") # ซ่อนข้อความเก่าไปก่อน
    window.update_idletasks()

    btc_price_usd, thb_rate, error = get_prices()

    if error:
        # หากมีข้อผิดพลาด, แสดงบนบรรทัดแรกและเปลี่ยนเป็นสีแดง
        price_usd_label.config(text=f"ข้อผิดพลาด: {error}", fg="red")
        price_thb_label.config(text="")
    else:
        # คำนวณราคาเป็น THB
        btc_price_thb = btc_price_usd * thb_rate

        # จัดรูปแบบและแสดงผล
        price_usd_label.config(text=f"BTC/USDT: ${btc_price_usd:,.2f}", fg="black")
        price_thb_label.config(text=f"BTC/THB: {btc_price_thb:,.2f} ฿", fg="#007A7A") # สีเขียวอมฟ้า

    # อัปเดตเวลาที่ดึงข้อมูลล่าสุด
    now = datetime.now()
    last_updated_label.config(text=f"อัปเดตล่าสุด: {now.strftime('%H:%M:%S')}")

# --- สร้างหน้าต่าง GUI ---
window = tk.Tk()
window.title("BTC Price | USD & THB (Binance)")
window.geometry("500x250") # ขยายขนาดหน้าต่าง

# สร้าง Label สำหรับแสดงราคา USD
price_usd_label = tk.Label(window, text="กำลังโหลด...", font=("Helvetica", 22, "bold"))
price_usd_label.pack(pady=(20, 0)) # ระยะห่างด้านบน 20, ด้านล่าง 0

# สร้าง Label สำหรับแสดงราคา THB
price_thb_label = tk.Label(window, text="", font=("Helvetica", 22, "bold"))
price_thb_label.pack(pady=(5, 20)) # ระยะห่างด้านบน 5, ด้านล่าง 20

# สร้าง Label สำหรับแสดงเวลาอัปเดตล่าสุด
last_updated_label = tk.Label(window, text="", font=("Helvetica", 10))
last_updated_label.pack()

# สร้างปุ่มสำหรับรีเฟรชราคา
refresh_button = tk.Button(window, text="รีเฟรชราคา", command=update_price, font=("Helvetica", 12))
refresh_button.pack(pady=15)

# --- เริ่มการทำงาน ---
update_price()
window.mainloop()
