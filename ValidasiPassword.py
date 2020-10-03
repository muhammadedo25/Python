print("5. Validasi Username dan Password")
username = "muhammadedo25"
password = "informatika"
x = 3
for i in range(3):
    user = input("Masukan Username anda: ")
    passw = input("Masukan Password anda: ")
    if user == username and passw == password:
        print ("Anda berhasil masuk")
        break
    else:
        print("Maaf Username atau Password anda salah")