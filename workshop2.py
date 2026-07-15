#ข้อมูลผู้สมัครงับงื้อเตงเบ๊บ

name = str(input("ไหนเองลองบอกชื่อมาสิ"))
age = int(input("เกิดมากี่ปีแล้ว"))
height = int(input("สูงเท่าไหร่อ่ะ "))
power = int(input("ไหนลองบอกระดับพลังตัวเองจาก1-10"))
money = int(input("ว่าแต่เองมีเงินติดตัวเท่าไหร่"))

if age >= 18 or name == "Fadill":
    print("Congrats you've been a part of Samachik Nigga")
elif power >= 7:
    print("และคุณได้เป็นหัวแถว")
elif height < 160:
    print("แถมมึงยังได้เป็นหัวแถวButเตี้ย")
else:
    print("มึงไม่ผ่านไอ้กาก")