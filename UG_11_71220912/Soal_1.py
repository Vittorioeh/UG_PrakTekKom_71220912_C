print ("="*40)
print ("Operasi Matematika")
print ("" , "1. Jumlah     [+]")
print ("" , "2. Kurang     [-]")
print ("" , "3. Kali       [*]")
print ("" , "4. Bagi       [/]")
print ("="*40)
pilih = str(input("Pilih operasi (1/2/3/4): "))
print ("="*40)
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

def penjumlahan ():
    Jumlah = (bil1 + bil2)
    return Jumlah
def pengurangan ():
    Kurang = (bil1 - bil2)
    return Kurang
def perkalian ():
    Kali = (bil1 * bil2)
    return Kali
def pembagian ():
    Bagi = (bil1 / bil2)
    return Bagi

if pilih == '1':
    print("Hasil operasi dari" , bil1 , "+" , bil2 , "=" , penjumlahan ())
elif pilih == '2':
    print ("Hasil operasi dari" , bil1 , "-" , bil2 , "=" , pengurangan ())
elif pilih == '3':
    print ("Hasil operasi dari" , bil1 , "*" , bil2 , "=" , perkalian ())
elif pilih == '4':
    print ("Hasil operasi dari" , bil1 , "/" , bil2 , "=" , pembagian ())
else:
    print ('Menu Tidak Tersedia')