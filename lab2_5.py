csc = float(input("Nhap Vao Chi So Dien Cu: "))
csm = float(input("Nhap Vao Chi So Dien Moi: "))
tieuThu = 0
tongTien = 0
tieuThu = csm-csc

if (csc > 0 and csm > 0 and csc <= csm):
    if tieuThu <= 50:
        tongTien = tieuThu*1000
    else:
        if tieuThu <= 100:
            tongTien = 50*1000 + (tieuThu-50)*2000
        elif tieuThu >= 101:
            tongTien = 50*1000 + 50*2000 + (tieuThu-100)*3500
print("Chi so cu: ", csc)
print("Chi so moi: ", csm)
print("Tieu thu: ", tieuThu, 'kWh')
print('Tong tien: ', int(tongTien))