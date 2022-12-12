a = float(input('Nhap vao so a: '))
b = float(input('Nhap vao so b: '))
operator = input('Nhap vao toan tu: ')
c = 0;
if operator == "+":
    c = a + b
elif operator == "-":
    c = a - b
elif operator == "*":
    c = a * b
elif operator == "/":
    if b == 0:
        print('Khong the thuc hien phep chia')
    else:
        c = a / b
else: 
    print('Nhap Lai toan tu ')
    exit()
print(a, operator, b, '=', c)