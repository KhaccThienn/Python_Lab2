a = float(input('Nhap vao canh a: '))
b = float(input('Nhap vao canh b: '))
c = float(input('Nhap vao canh c: '))

if (a+b > c and a+c > b and b+c > a):
    print("Cac so nhap vao la ba canh cua 1 tam giac: ")
    if (a == b and b == c):
        print("Deu")
    elif (a == b or b == c or c == a):
        print("Can")
    elif (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a):
        print("Vuong")
    else:
        print('Thuong')
else:
    print("Khong phai 3 canh cua 1 tam giac, vui long thu lai !")