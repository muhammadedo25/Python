print("1. Menghitung Nilai Rata-rata 5 Variabel")
angka = []
jumlah = int(input("Berapa jumlah angka yang ingin di input: "))
for i in range (jumlah):
    nilai = int(input(f"Masukan angka ke-{i+1}: "))
    angka.append(nilai)
print("Hasil rata-rata adalah : {}".format(sum(angka)/jumlah))