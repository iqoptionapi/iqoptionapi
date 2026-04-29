"""ตัวอย่างการใช้งาน IQ Option API"""
from iqoptionapi.stable_api import IQ_Option
import time

# ใส่ email และ password ของคุณ
EMAIL = "your_email@example.com"
PASSWORD = "your_password"

print(f"IQ Option API v{IQ_Option.__version__}")
print("กำลัง connect...")

iq = IQ_Option(EMAIL, PASSWORD)
check, reason = iq.connect()

if check:
    print("Connect สำเร็จ!")

    # ดูยอดเงินในบัญชี
    print("Balance (PRACTICE):", iq.get_balance())

    # เปลี่ยนเป็นบัญชี PRACTICE
    iq.change_balance("PRACTICE")
    print("เปลี่ยนเป็น PRACTICE account แล้ว")

    print("Balance:", iq.get_balance())
else:
    print(f"Connect ล้มเหลว: {reason}")
