print("โปรแกรมคำนวณวิชา ")

Thai = int(input("คะแนนวิชาภาษาไทย : "))
Math =  int(input("คะแนนวิชาคณิตศาสตร์ : "))
English =  int(input("คะแนนวิชาภาษาอังกฤษ : "))

print(Thai,Math,English)

full = Thai + Math + English
avg = (Thai + Math + English) /3

print("คะแนนรวม : ", full,)
print("คะแนนเฉลี่ย : ", avg,)

if avg >= 80:
    print("ดีมาก")
elif vavg >= 70:
    print("ดี")    
elif avg >= 60:
    print("พอได้")
elif avg >= 50:
    print("พยายามกว่านี้") 
elif avg < 50:
    print("ควรปรับปรุง")   

print("โปรแกรมคำนวณวิชา โดย: นายกิตติกร ปะวะบุตร เลขที่7")