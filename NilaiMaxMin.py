print("4. Menentukan Nilai Maksimal dan minimal")
angka =[]
jumlah = int(input("Berapa jumlah angka yang ingin di input: "))
for i in range (jumlah):
    nilai = int(input(f"Masukan angka ke-{i+1}: "))
    angka.append(nilai)
nilaiterbesar = max(angka)
nilaiterkecil = min(angka)
print ("list: ", angka)
print('nilai terbesar pada list:',nilaiterbesar)
print('nilai terkecil pada list:',nilaiterkecil)