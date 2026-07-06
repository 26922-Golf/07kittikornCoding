print("โปรแกรมแม่สูตรคูณ")

start = int(input("ตัวเลขเริ่มต้น"))
end = int(input("ตัวเลขสิ้นสุด"))

for i in range (start,end):
    print(f"แม่สูตรคูณของ {i} คือ")
    for y in range(1,13):
        print(f"{i} x {i} ={i} * {y}")

print("ทำโดย กิตติกร ปะวะบุตร")