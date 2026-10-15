import os

users = [["admin", "admin123", "Admin"]]
tiket = []
kendaraan = ("Motor", "Mobil")
layanan = [
    ["Cuci Biasa", 15000, 30000],
    ["Cuci + Wax", 25000, 50000],
    ["Cuci Interior", 30000, 60000],
    ["Cuci Lengkap", 45000, 90000]
]
nomor_tiket = 1

while True:
    os.system("cls")
    print("=== SISTEM TIKET CUCI KENDARAAN ===")
    print("1. Login")
    print("2. Register")
    print("0. Keluar")
    pilih = input("Pilih menu: ")
    while pilih != "0" and pilih != "1" and pilih != "2":
        print("Pilihan tidak valid!")
        pilih = input("Pilih menu: ")

    if pilih == "0":
        os.system("cls")
        print("Terima kasih. Program selesai.")
        break

    elif pilih == "2":
        os.system("cls")
        print("=== REGISTER ===")
        while True:
            username = input("Username : ")
            ada = False
            for u in users:
                if u[0] == username:
                    ada = True
            if username == "":
                print("Username tidak boleh kosong!")
            elif ada == True:
                print("Username sudah dipakai!")
            else:
                break
        password = input("Password : ")
        while password == "":
            print("Password tidak boleh kosong!")
            password = input("Password : ")
        users.append([username, password, "Pengguna"])
        print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk melanjutkan...")

    elif pilih == "1":
        os.system("cls")
        print("=== LOGIN ===")
        user = None
        percobaan = 0
        while user == None and percobaan < 3:
            username = input("Username : ")
            password = input("Password : ")
            for u in users:
                if u[0] == username and u[1] == password:
                    user = u
            if user == None:
                percobaan += 1
                print("Username atau password salah!")

        if user == None:
            print("Percobaan login habis.")
            input("Tekan Enter untuk kembali...")
        else:
            while True:
                os.system("cls")
                print("=== MENU UTAMA ===")
                print("Login sebagai:", user[0], "(" + user[2] + ")")
                print("1. Buat Tiket")
                print("2. Lihat Tiket & Antrean")
                print("3. Ubah Status Tiket")
                if user[2] == "Admin":
                    print("4. Hapus Tiket")
                    print("5. Lihat Daftar Pengguna")
                print("0. Logout")

                while True:
                    menu = input("Pilih menu: ")
                    if menu == "0" or menu == "1" or menu == "2" or menu == "3":
                        break
                    elif user[2] == "Admin" and (menu == "4" or menu == "5"):
                        break
                    print("Pilihan tidak valid!")

                if menu == "0":
                    break

                elif menu == "1":
                    os.system("cls")
                    print("=== BUAT TIKET ===")
                    nama = input("Nama pelanggan : ")
                    while nama == "":
                        print("Nama tidak boleh kosong!")
                        nama = input("Nama pelanggan : ")

                    print("Jenis kendaraan:")
                    print("1.", kendaraan[0])
                    print("2.", kendaraan[1])
                    pilih_k = input("Pilih jenis kendaraan: ")
                    while pilih_k != "1" and pilih_k != "2":
                        print("Pilihan tidak valid!")
                        pilih_k = input("Pilih jenis kendaraan: ")
                    if pilih_k == "1":
                        kolom = 1
                    else:
                        kolom = 2

                    print("Daftar layanan:")
                    nomor = 1
                    for l in layanan:
                        print(nomor, ".", l[0], "- Rp", l[kolom])
                        nomor += 1
                    pilih_l = input("Pilih layanan: ")
                    while pilih_l != "1" and pilih_l != "2" and pilih_l != "3" and pilih_l != "4":
                        print("Pilihan tidak valid!")
                        pilih_l = input("Pilih layanan: ")
                    baris = int(pilih_l) - 1

                    tiket.append([str(nomor_tiket), nama, kendaraan[kolom - 1],
                                  layanan[baris][0], layanan[baris][kolom], "Menunggu"])
                    print("Tiket #" + str(nomor_tiket), "berhasil dibuat. Total: Rp", layanan[baris][kolom])
                    nomor_tiket += 1
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "2":
                    os.system("cls")
                    print("=== DAFTAR TIKET & ANTREAN ===")
                    if len(tiket) == 0:
                        print("Belum ada tiket.")
                    else:
                        menunggu = 0
                        proses = 0
                        selesai = 0
                        print("ID | Nama | Kendaraan | Layanan | Harga | Status")
                        for t in tiket:
                            print(t[0], "|", t[1], "|", t[2], "|", t[3], "| Rp", t[4], "|", t[5])
                            if t[5] == "Menunggu":
                                menunggu += 1
                            elif t[5] == "Proses":
                                proses += 1
                            else:
                                selesai += 1
                        print("Menunggu:", menunggu, "| Proses:", proses, "| Selesai:", selesai)
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "3":
                    os.system("cls")
                    print("=== UBAH STATUS TIKET ===")
                    if len(tiket) == 0:
                        print("Belum ada tiket.")
                    else:
                        print("ID | Nama | Kendaraan | Layanan | Harga | Status")
                        for t in tiket:
                            print(t[0], "|", t[1], "|", t[2], "|", t[3], "| Rp", t[4], "|", t[5])
                        id_tiket = input("Masukkan ID tiket: ")
                        ditemukan = None
                        for t in tiket:
                            if t[0] == id_tiket:
                                ditemukan = t

                        if ditemukan == None:
                            print("Tiket tidak ditemukan!")
                        elif ditemukan[5] == "Selesai":
                            print("Tiket sudah Selesai, status tidak bisa diubah.")
                        elif ditemukan[5] == "Menunggu":
                            print("1. Proses")
                            print("2. Selesai")
                            pilih_s = input("Pilih status baru: ")
                            while pilih_s != "1" and pilih_s != "2":
                                print("Pilihan tidak valid!")
                                pilih_s = input("Pilih status baru: ")
                            if pilih_s == "1":
                                ditemukan[5] = "Proses"
                            else:
                                ditemukan[5] = "Selesai"
                            print("Status berhasil diubah menjadi", ditemukan[5])
                        else:
                            ditemukan[5] = "Selesai"
                            print("Status berhasil diubah menjadi Selesai")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "4":
                    os.system("cls")
                    print("=== HAPUS TIKET ===")
                    if len(tiket) == 0:
                        print("Belum ada tiket.")
                    else:
                        print("ID | Nama | Kendaraan | Layanan | Harga | Status")
                        for t in tiket:
                            print(t[0], "|", t[1], "|", t[2], "|", t[3], "| Rp", t[4], "|", t[5])
                        id_tiket = input("Masukkan ID tiket: ")
                        ditemukan = None
                        for t in tiket:
                            if t[0] == id_tiket:
                                ditemukan = t

                        if ditemukan == None:
                            print("Tiket tidak ditemukan!")
                        else:
                            yakin = input("Yakin hapus tiket ini? (y/n): ")
                            while yakin != "y" and yakin != "n":
                                print("Ketik y atau n!")
                                yakin = input("Yakin hapus tiket ini? (y/n): ")
                            if yakin == "y":
                                tiket.remove(ditemukan)
                                print("Tiket berhasil dihapus.")
                            else:
                                print("Penghapusan dibatalkan.")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "5":
                    os.system("cls")
                    print("=== DAFTAR PENGGUNA ===")
                    for u in users:
                        print(u[0], "-", u[2])
                    input("Tekan Enter untuk melanjutkan...") 