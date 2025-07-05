

import random
from collections import Counter

# --- ข้อมูลตัวอย่าง ---
# สมมติว่าเป็นข้อมูลเลขท้าย 2 ตัวจากงวดก่อนๆ
# ในการใช้งานจริง คุณอาจจะต้องหาข้อมูลจริงมาใส่ใน list นี้
past_results = [
    "14", "58", "47", "91", "85", "61", "09", "99", "50", "30",
    "16", "62", "11", "67", "91", "58", "73", "82", "46", "69"
]

def analyze_numbers(history: list[str]) -> Counter:
    """
    วิเคราะห์ความถี่ของเลขแต่ละตัว (0-9) จากประวัติผลหวย
    """
    all_digits = []
    for number in history:
        all_digits.extend(list(number)) # แยก "14" เป็น "1" และ "4"
    
    # นับความถี่ของเลขแต่ละตัว
    frequency = Counter(all_digits)
    return frequency

def generate_lucky_numbers(count: int) -> list[str]:
    """
    สุ่มสร้างเลขท้าย 2 ตัวตามจำนวนที่ต้องการ
    """
    lucky_numbers = []
    for _ in range(count):
        # สุ่มเลข 0-99 แล้วจัดรูปแบบให้เป็น 2 หลัก (เช่น 5 -> "05")
        number = random.randint(0, 99)
        lucky_numbers.append(f"{number:02d}")
    return lucky_numbers

def main():
    """
    ฟังก์ชันหลักสำหรับรันโปรแกรม
    """
    print("--- โปรแกรมวิเคราะห์และสุ่มเลขหวย (เพื่อความบันเทิง) ---")
    print("\n*** คำเตือน: โปรแกรมนี้ไม่สามารถทำนายผลรางวัลได้จริง การลงทุนมีความเสี่ยง ***\n")

    # 1. วิเคราะห์ความถี่
    print("--- สถิติความถี่ของตัวเลขจากข้อมูลตัวอย่าง ---")
    freq_counter = analyze_numbers(past_results)
    # แสดงผลเลขที่ออกบ่อยที่สุด 5 อันดับแรก
    for digit, count in freq_counter.most_common(5):
        print(f"เลข {digit} ออกมาแล้ว {count} ครั้ง")

    # 2. สร้างเลขนำโชค
    print("\n--- เลขนำโชคที่สุ่มได้ ---")
    lucky_picks = generate_lucky_numbers(5) # สุ่มมา 5 เลข
    print(" ".join(lucky_picks))
    
    print("\nขอให้โชคดีครับ!")

# รันฟังก์ชัน main เมื่อสคริปต์ถูกเรียกใช้งานโดยตรง
if __name__ == "__main__":
    main()

