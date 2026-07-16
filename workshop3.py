shop = int(input("ใส่จำนวนร้านค้าทั้งหมด : "))
total = 0 # กระปุกออมสิน

for i in range(shop):
    money =  int(input(f"เก็บเงินร้านที่ {i + 1} : "))
    total += money

print(f"สรุปมี {shop} ร้าน และ ยอดเงินทั้งหมด {total} บาท " )