import math as m # import module math

def digitAwal(x,y):
    # temporary vairable untuk nomor baru
    new_num = int(m.pow(x,y)) 
    # iterasi untuk transform int menjadi list
    temp_list = list(int(x) for x in str(new_num))
    # return nomor pertama di list
    return temp_list[0]

def digitAkhir(x,y):
    # temporary variable untuk nomor baru
    new_num = int(m.pow(x,y))
    # iterasi untuk transform int menjadi list
    temp_list = list(int(x) for x in str(new_num))
    # return nomor terakhir di list
    return temp_list[-1]

# test set untuk function digitAwal()
print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))
print('\n')
# test set untuk function digitAkhir()
print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))