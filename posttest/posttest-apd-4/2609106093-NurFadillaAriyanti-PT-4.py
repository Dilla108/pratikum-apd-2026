nama = "dila"
nim = "093"
n = 3

uang_bulanan = 2500000
pengeluaran = 0
ulang = "y"                 
pilih = "t" 

while n > 0:
    Nama = str(input("Masukkan Nama: ")).lower()
    Nim = str(input("Masukkan Nim: "))
    n -= 1

    if Nama == nama and Nim == nim:
        print("Selamat Datang", Nama)
        break
    elif n == 0:
        print("Login gagal, silahkan isi form login kembali")
        break
    elif Nama != nama or Nim != nim:
        print(f"Login gagal, sisa percobaan anda: {n}")


while True:
    print("\nMenu:")
    print("1. Catat Pengeluaran")
    print("2. Cek Sisa Uang Bulanan")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        while ulang == "y":
            jumlah_pengeluaran = int(input("Masukkan jumlah pengeluaran: "))
            if uang_bulanan < jumlah_pengeluaran:
                print("Pengeluaran melebihi uang bulanan Anda.")
                break
            pengeluaran += jumlah_pengeluaran
            ulang = str(input("Apakah Anda ingin kembali mencatat pengeluaran? (y/t): ")).lower()
            if ulang == "t":
                print("Terima kasih telah menggunakan aplikasi ini.")
                break
            elif ulang != "y" and ulang != "t":
                print("pilihan tidak terdaftar, silahkan pilih y/t")
        sisa_uang = uang_bulanan - pengeluaran
        print(f"Sisa uang bulanan Anda: {sisa_uang}")  
    elif pilihan == "2":
        sisa_uang = uang_bulanan - pengeluaran
        print(f"Sisa uang bulanan Anda: {sisa_uang}")
    elif pilihan == "3":
        print("Terima kasih telah menggunakan aplikasi ini.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")