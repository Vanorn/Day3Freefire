#input

quantity = int(input("ไหนมึงเอาปืนมากี่กระบอก"))
cost = int(input("ทุนเท่าไหร่เนี่ยน้อง"))
sell = int(input("ขายกี่บาทดีวะน้องชาย"))
members = int(input("จะเอาเด็กไปกี่คน"))
whatgum = ((quantity * sell) - (quantity * cost))
Ibosshere = ((whatgum * 1/5))
#output

#cost
print("ต้นทุนราคา",(quantity * cost), "บาท")

#sell
print("รายรับทั้งหมด",(quantity * sell), "บาท")

#margin
print("กำไรสุทธิ",(quantity * sell) - (quantity * cost), "บาท")

#จำนวนเงินที่หักไปให้บอส
print("จำนวนเงินที่หักไปให้บอส",(whatgum * 1/5), "บาท")

#จำนวนเงินที่ลูกน้องแต่ละคนได้
print("จำนวนเงินที่ลูกน้องแต่ละคนได้",((whatgum - Ibosshere) / members) ,"บาท" )
