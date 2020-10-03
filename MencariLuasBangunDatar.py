def menu():
    print ("<===== Mengukur Luas dan Keliling Bangun Datar ===== >")
    print ()
    print ("Pilih bangun Datar :")
    bangundatar = ["Persegi","Persegi Panjang","Lingkaran","Segitiga Sama Kaki","Trapesium"]
    for i in range (len(bangundatar)):
       print (i+1, bangundatar[i])

    pilih = input("pilih angka sesuai bangun datar yang ingin diukur: ")
    if pilih == "1" :
        print("----- Persegi -----")
        sisi = float(input("Masukan panjang sisi persegi dengan satuan cm: "))
        luas = sisi*sisi
        keliling = 4*sisi
        print ("Luas persegi dengan panjang sisi" , sisi , "adalah" , luas , "cm")
        print ("Keliling persegi dengan panjang sisi" , sisi , "adalah" , keliling , "cm")

    elif pilih == "2" :
        print ("----- Persegi Panjang -----")
        panjang = float(input("Masukan ukuran Panjang Persegi Panjang dengan satuan cm: "))
        lebar = float(input("Masukan ukuran Lebar Persegi Panjang dengan satuan cm: "))
        luas = panjang * lebar
        keliling = 2*(panjang+lebar)
        print("Luas persegi panjang dengan panjang", panjang , "dan lebar", lebar ,"adalah", luas, "cm")
        print("Keliling persegi panjang dengan panjang", panjang, "dan lebar", lebar, "adalah", keliling, "cm")

    elif pilih == "3":
        print("----- Lingkaran -----")
        diamter = float(input("Masukan panjang Diameter lingkaran dengan satuan cm: "))
        luas = 3.14 * ((diamter/2)**2)
        keliling = 3.14 * diameter
        print ("Luas Lingkaran dengan panjang Diameter",diamter,"adalah",luas,"cm")
        print ("Keliling Lingkaran dengan panjang Diameter",diamter,"adalah",keliling,"cm")
    elif pilih == "4":
        print ("----- Segitiga Sama Kaki -----")
        tinggi = float(input("Masukan tinggi segitiga dengan satuan cm: "))
        alas = float(input("Masukan alas segitiga dengan satuan cm: "))
        luas = (alas * tinggi)/2
        pytagoras = ((tinggi**2)+((0.5*alas)**2))**0.5
        keliling = pytagoras + alas + pytagoras
        print ("Luas Segitiga Sama kaki dengan tinggi", tinggi ,"dan alas", alas ,"adalah", luas ,"cm")
        print("Luas Segitiga Sama kaki dengan kedua sisi kanan - kirinya", pytagoras, "dan alas", alas, "adalah", keliling, "cm")
    elif pilih == "5":
        print ("----- Trapesium -----")
        a = float(input("masukan sisi yang sejajar pendek dengan satuan cm: "))
        b = float(input("masukan sisi yang sejajar panjang dengan satuan cm: "))
        tinggi = float(input("masukan tinggi Trapesium dengan satuan cm: "))
        luas = 0.5 * (a+b) * tinggi
        sisimiring = (((b-a)**2) + (tinggi**2))**0.5
        keliling = a + b + tinggi + sisimiring
        print ("Luas Trapesium dengan sisi sejajar",a,"dan",b,"dengan tinggi",tinggi,"adalah",luas,"cm")
        print("Keliling Trapesium dengan sisi sejajar", a, "dan", b, "dengan tinggi", tinggi, "adalah", keliling, "cm")
    else:
        print("Masukan Inputan dengan benar")
        print()
        menu()
menu()