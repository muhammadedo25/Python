bilangan1 = []
bilangan2 = []

def menu() :
    # pemilihan cara penghitungan
    print("<=====Penjumlahan dan Pengurangan bilangan pecahan=====>")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    pilih = int(input("Masukan pilihan: "))
    if pilih == 1:
        penjumlahan()
    elif pilih == 2:
        pengurangan()
    else:
        "masukan angka yang ada di menu"
        menu()

def penginputan():
    a = []
    b = []
    # penginputan data bilangan
    pembilang1 = int(input("Masukan Angka pembilang bilangan pertama: "))
    penyebut1 = int(input("Masukan Angka penyebut bilangan pertama: "))
    if penyebut1 == 0 :
        print ("Penyebut tidak boleh angka 0, Silahkan ulangi")
        print("<============================================>")
        penginputan()
    else:
        a.append(pembilang1)
        a.append(penyebut1)
        satu =  ("Bilangan pertama:  {0}/{1}")
        print (satu.format(pembilang1,penyebut1))
        pembilang2 = int(input("Masukan Angka pembilang bilangan kedua: "))
        penyebut2 = int(input("Masukan Angka penyebut bilangan kedua: "))
        if penyebut2 == 0 :
            print ("Penyebut tidak boleh angka 0, Silahkan ulangi")
            print("<============================================>")
            penginputan()
        else:
            b.append(pembilang2)
            b.append(penyebut2)
            dua = ("Bilangan kedua:  {0}/{1}")
            print(dua.format(pembilang2, penyebut2))
            bilangan1.append(a)
            bilangan2.append(b)

def penjumlahan():
    penginputan()
    if bilangan1[0][1] == bilangan2[0][1]:
        hasil_pembilang = bilangan1[0][0] + bilangan2[0][0]
        hasil_penyebut = bilangan2[0][1]
        hasil= ("hasil dari pemjumlahannya: {0}/{1}")
        print (hasil.format(hasil_pembilang,hasil_penyebut))
    elif bilangan1[0][1] != bilangan2[0][1]:
        hasil_penyebut = kpk(bilangan1[0][1] , bilangan2[0][1])
        hasil_pembilang = (hasil_penyebut/bilangan1[0][1]*bilangan1[0][0]) + (hasil_penyebut/bilangan2[0][1]*bilangan2[0][0])
        hasil = ("hasil dari pemjumlahannya: {0}/{1}")
        print(hasil.format(hasil_pembilang, hasil_penyebut))

def pengurangan():
    penginputan()
    if bilangan1[0][1] == bilangan2[0][1]:
        hasil_pembilang = bilangan1[0][0] - bilangan2[0][0]
        hasil_penyebut = bilangan2[0][1]
        hasil= ("hasil dari Pengurangannya: {0}/{1}")
        print (hasil.format(hasil_pembilang,hasil_penyebut))
    elif bilangan1[0][1] != bilangan2[0][1]:
        hasil_penyebut = kpk(bilangan1[0][1] , bilangan2[0][1])
        hasil_pembilang = (hasil_penyebut/bilangan1[0][1]*bilangan1[0][0]) - (hasil_penyebut/bilangan2[0][1]*bilangan2[0][0])
        hasil = ("hasil dari Pengurangannya: {0}/{1}")
        print(hasil.format(hasil_pembilang, hasil_penyebut))

def kpk(a,b):
    x = 1
    y = 1
    p = a * x
    j = b * y
    while p != j:
        while p > j :
            y = y+1
            j = b * y
        while p < j :
            x = x+1
            p = a * x
    if p == j:
        return (p)

menu()
print ("<=============penghitungan selesai=============>")