import time
import datetime

print("=== البوت الاحترافي بدأ العمل بنجاح ===")
# حلقة تكرارية لا نهائية للعمل 24/24 ساعة
while True:
    now = datetime.datetime.now()
    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] السكربت شغال فالسيرفر دابا...")
    time.sleep(60) # ينتظر دقيقة ويعيد المحاولة
