toan = float(input('Nhap vao diem toan: '))
ly = float(input('Nhap vao diem ly: '))
hoa = float(input('Nhap vao diem hoa: '))

dtb = 0

dtb = (toan + ly + hoa) / 3

print("Diem Toan: ", toan)
print("Diem Ly: ", ly)
print("Diem Hoa: ", hoa)

if toan < 0 or ly < 0 or hoa < 0:
    print('Nhap lai diem toan, ly, hoa')
else:
    print('Dien trung binh cua ban la: ', dtb)
    if dtb <= 5:
        print('Can co gang !')
    elif 5 < dtb <= 6:
        print('Xep loai trung binh')
    elif 6 < dtb <= 7:
        print('Xep Loai Kha')
    elif 7 < dtb <= 8:
        print('Xep loai gioi')
    elif dtb > 8:
        print('Xep loai xuat sac')