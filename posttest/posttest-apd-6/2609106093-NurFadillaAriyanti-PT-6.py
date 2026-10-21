import os

users = {
    "admin": {"password": "admin123", "role": "Admin"}
}

tiket = {}

kendaraan = ("Motor", "Mobil")

layanan = {
    "1": {"nama": "Cuci Biasa", "Motor": 15000, "Mobil": 30000},
    "2": {"nama": "Cuci + Wax", "Motor": 25000, "Mobil": 50000},
    "3": {"nama": "Cuci Interior", "Motor": 30000, "Mobil": 60000},
    "4": {"nama": "Cuci Lengkap", "Motor": 45000, "Mobil": 90000}
}

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
            if username == "":
                print("Username tidak boleh kosong!")
            elif username in users:
                print("Username sudah dipakai!")
            else:
                break
                
        password = input("Password : ")
        while password == "":
            print("Password tidak boleh kosong!")
            password = input("Password : ")
            
        users[username] = {"password": password, "role": "Pengguna"}
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
            
            if username in users and users[username]["password"] == password:
                user = [username, password, users[username]["role"]]
                
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
                        jenis_kendaraan = kendaraan[0]
                    else:
                        jenis_kendaraan = kendaraan[1]

                    print("Daftar layanan:")
                    for k, v in layanan.items():
                        print(k, ".", v["nama"], "- Rp", v[jenis_kendaraan])
                        
                    pilih_l = input("Pilih layanan: ")
                    while pilih_l not in layanan:
                        print("Pilihan tidak valid!")
                        pilih_l = input("Pilih layanan: ")
                        
                    nama_layanan = layanan[pilih_l]["nama"]
                    harga = layanan[pilih_l][jenis_kendaraan]
                    id_tiket_str = str(nomor_tiket)

                    tiket[id_tiket_str] = {
                        "nama": nama,
                        "kendaraan": jenis_kendaraan,
                        "layanan": nama_layanan,
                        "harga": harga,
                        "status": "Menunggu"
                    }
                    
                    print("Tiket #" + id_tiket_str, "berhasil dibuat. Total: Rp", harga)
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
                        for id_t, t in tiket.items():
                            print(id_t, "|", t["nama"], "|", t["kendaraan"], "|", t["layanan"], "| Rp", t["harga"], "|", t["status"])
                            if t["status"] == "Menunggu":
                                menunggu += 1
                            elif t["status"] == "Proses":
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
                        for id_t, t in tiket.items():
                            print(id_t, "|", t["nama"], "|", t["kendaraan"], "|", t["layanan"], "| Rp", t["harga"], "|", t["status"])
                            
                        id_tiket = input("Masukkan ID tiket: ")
                        
                        if id_tiket not in tiket:
                            print("Tiket tidak ditemukan!")
                        elif tiket[id_tiket]["status"] == "Selesai":
                            print("Tiket sudah Selesai, status tidak bisa diubah.")
                        elif tiket[id_tiket]["status"] == "Menunggu":
                            print("1. Proses")
                            print("2. Selesai")
                            pilih_s = input("Pilih status baru: ")
                            while pilih_s != "1" and pilih_s != "2":
                                print("Pilihan tidak valid!")
                                pilih_s = input("Pilih status baru: ")
                            if pilih_s == "1":
                                tiket[id_tiket]["status"] = "Proses"
                            else:
                                tiket[id_tiket]["status"] = "Selesai"
                            print("Status berhasil diubah menjadi", tiket[id_tiket]["status"])
                        else:
                            tiket[id_tiket]["status"] = "Selesai"
                            print("Status berhasil diubah menjadi Selesai")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "4":
                    os.system("cls")
                    print("=== HAPUS TIKET ===")
                    if len(tiket) == 0:
                        print("Belum ada tiket.")
                    else:
                        print("ID | Nama | Kendaraan | Layanan | Harga | Status")
                        for id_t, t in tiket.items():
                            print(id_t, "|", t["nama"], "|", t["kendaraan"], "|", t["layanan"], "| Rp", t["harga"], "|", t["status"])
                            
                        id_tiket = input("Masukkan ID tiket: ")

                        if id_tiket not in tiket:
                            print("Tiket tidak ditemukan!")
                        else:
                            yakin = input("Yakin hapus tiket ini? (y/n): ")
                            while yakin != "y" and yakin != "n":
                                print("Ketik y atau n!")
                                yakin = input("Yakin hapus tiket ini? (y/n): ")
                            if yakin == "y":
                                del tiket[id_tiket]
                                print("Tiket berhasil dihapus.")
                            else:
                                print("Penghapusan dibatalkan.")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "5":
                    os.system("cls")
                    print("=== DAFTAR PENGGUNA ===")
                    for username, data in users.items():
                        print(username, "-", data["role"])
                    input("Tekan Enter untuk melanjutkan...")