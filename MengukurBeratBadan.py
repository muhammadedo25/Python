print("3. Menghitung BMI (Body Mass Index)")
berat = int(input("Masukan Berat badan anda (KG): "))
tinggi = int(input("Masukan Tinggi Badan anda (CM): "))
BMI = (berat/((tinggi/100)**2))
print ("Hasil pengukuran BMI anda adalah: ", BMI)
if BMI < 18.5:
    print("Berat badan anda kurang")
elif BMI >= 18.5 and BMI <= 22.9:
    print("Berat badan anda Ideal")
elif BMI >= 23 and BMI <= 29.9:
    print("Berat badan anda berlebih")
else:
    print("Anda mengalami Obesitas")