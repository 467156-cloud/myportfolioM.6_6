# "โปรแกรมคำนวณพื้นที่รูปสี่เหลี่ยมมุมฉาก เวอร์ใหม่"   
while True:
    try:
        width = float(input("กรอกความกว้าง: "))
        length = float(input("กรอกความยาว: "))

        if width <= 0 or length <= 0:
            print("กรุณากรอกค่าที่มากกว่า 0")
            continue

        area = width * length
        print("พื้นที่คือ", area)

        break
    except:
        print("กรุณากรอกตัวเลขเท่านั้น")

