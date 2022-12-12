n = int(input('Nhap vao so n: '))

if n > 0:
    if n % 2 == 0:
        print(n,'la so chan')
    else: 
        print(n, 'la so le')
    
    if n % 3 == 0 and n % 5 == 0:
        print(n, 'chia het cho 3 va 5')
    else:
        print(n, 'ko chia het cho 3 va 5')
else:
    print('Vui long nhap lai n !')