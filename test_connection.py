"""ตัวอย่างการใช้งาน IQ Option API"""
from iqoptionapi.stable_api import IQ_Option
import time

# ใส่ email และ password ของคุณ
EMAIL = "your_email@example.com"
PASSWORD = "your_password"

print(f"IQ Option API v{IQ_Option.__version__}")
print("Connecting...")

iq = IQ_Option(EMAIL, PASSWORD)
check, reason = iq.connect()

if check:
    print("Connected!")
    print("Balance (PRACTICE):", iq.get_balance())
    iq.change_balance("PRACTICE")
    print("Switched to PRACTICE account")
    print("Balance:", iq.get_balance())
else:
    print(f"Connect failed: {reason}")
