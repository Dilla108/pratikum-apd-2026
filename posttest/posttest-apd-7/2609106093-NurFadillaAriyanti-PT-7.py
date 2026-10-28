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
MAKS_PERCOBAAN = 3


def buat_id_tiket():
    global nomor_tiket
    id_baru = str(nomor_tiket)
    nomor_tiket += 1
    return id_baru


def pilih_kendaraan():
    print("Jenis kendaraan:")
    print("1.", kendaraan[0])
    print("2.", kendaraan[1])
    nomor = input_pilihan("Pilih jenis kendaraan: ", 1, 2)
    return kendaraan[nomor - 1]


def input_pilihan(teks, minimal, maksimal):
    while True:
        try:
            angka = int(input(teks))
            if angka < minimal or angka > maksimal:
                raise ValueError
            return angka
        except ValueError:
            print("Input harus angka antara", minimal, "sampai", maksimal, "!")


def cek_login(username, password):
    try:
        if users[username]["password"] == password:
            return users[username]["role"]
        return None
    except KeyError:
        return None


def input_teks(label):
    teks = input(label)
    while teks == "":
        print(label.strip(" :"), "tidak boleh kosong!")
        teks = input(label)
    return teks


def hitung_total(daftar_harga, n):
    if n == 0:
        return 0
    return daftar_harga[n - 1] + hitung_total(daftar_harga, n - 1)


def bersihkan_layar():
    os.system("cls")


def jeda():
    input("Tekan Enter untuk melanjutkan...")


def tampil_tiket():
    print("ID | Nama | Kendaraan | Layanan | Harga | Status")
    for id_t, t in tiket.items():
        print(id_t, "|", t["nama"], "|", t["kendaraan"], "|",
              t["layanan"], "| Rp", t["harga"], "|", t["status"])


def register():
    bersihkan_layar()
    print("=== REGISTER ===")
    username = input_teks("Username : ")
    while username in users:
        print("Username sudah dipakai!")
        username = input_teks("Username : ")
    password = input_teks("Password : ")
    users[username] = {"password": password, "role": "Pengguna"}
    print("Registrasi berhasil! Silakan login.")
    jeda()


def buat_tiket():
    bersihkan_layar()
    print("=== BUAT TIKET ===")
    nama = input_teks("Nama pelanggan : ")
    jenis_kendaraan = pilih_kendaraan()

    print("Daftar layanan:")
    for k, v in layanan.items():
        print(k, ".", v["nama"], "- Rp", v[jenis_kendaraan])

    pilih_l = str(input_pilihan("Pilih layanan: ", 1, len(layanan)))
    nama_layanan = layanan[pilih_l]["nama"]
    harga = layanan[pilih_l][jenis_kendaraan]
    id_tiket = buat_id_tiket()

    tiket[id_tiket] = {
        "nama": nama,
        "kendaraan": jenis_kendaraan,
        "layanan": nama_layanan,
        "harga": harga,
        "status": "Menunggu"
    }
    print("Tiket #" + id_tiket, "berhasil dibuat. Total: Rp", harga)
    jeda()


def lihat_tiket():
    bersihkan_layar()
    print("=== DAFTAR TIKET & ANTREAN ===")
    if len(tiket) == 0:
        print("Belum ada tiket.")
    else:
        menunggu = 0
        proses = 0
        selesai = 0
        harga_selesai = []
        tampil_tiket()
        for t in tiket.values():
            if t["status"] == "Menunggu":
                menunggu += 1
            elif t["status"] == "Proses":
                proses += 1
            else:
                selesai += 1
                harga_selesai.append(t["harga"])
        print("Menunggu:", menunggu, "| Proses:", proses, "| Selesai:", selesai)
        total = hitung_total(harga_selesai, len(harga_selesai))
        print("Total pendapatan (tiket Selesai): Rp", total)
    jeda()


def ubah_status():
    bersihkan_layar()
    print("=== UBAH STATUS TIKET ===")
    if len(tiket) == 0:
        print("Belum ada tiket.")
    else:
        tampil_tiket()
        id_tiket = input("Masukkan ID tiket: ")
        try:
            status_lama = tiket[id_tiket]["status"]
        except KeyError:
            print("Tiket tidak ditemukan!")
        else:
            if status_lama == "Selesai":
                print("Tiket sudah Selesai, status tidak bisa diubah.")
            elif status_lama == "Menunggu":
                print("1. Proses")
                print("2. Selesai")
                pilih_s = input_pilihan("Pilih status baru: ", 1, 2)
                if pilih_s == 1:
                    tiket[id_tiket]["status"] = "Proses"
                else:
                    tiket[id_tiket]["status"] = "Selesai"
                print("Status berhasil diubah menjadi", tiket[id_tiket]["status"])
            else:
                tiket[id_tiket]["status"] = "Selesai"
                print("Status berhasil diubah menjadi Selesai")
    jeda()


def hapus_tiket():
    bersihkan_layar()
    print("=== HAPUS TIKET ===")
    if len(tiket) == 0:
        print("Belum ada tiket.")
    else:
        tampil_tiket()
        id_tiket = input("Masukkan ID tiket: ")
        try:
            data = tiket[id_tiket]
        except KeyError:
            print("Tiket tidak ditemukan!")
        else:
            print("Tiket:", data["nama"], "-", data["layanan"])
            yakin = input("Yakin hapus tiket ini? (y/n): ")
            while yakin != "y" and yakin != "n":
                print("Ketik y atau n!")
                yakin = input("Yakin hapus tiket ini? (y/n): ")
            if yakin == "y":
                del tiket[id_tiket]
                print("Tiket berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
    jeda()


def lihat_pengguna():
    bersihkan_layar()
    print("=== DAFTAR PENGGUNA ===")
    for nama, data in users.items():
        print(nama, "-", data["role"])
    jeda()


def menu_utama(username, role):
    while True:
        bersihkan_layar()
        print("=== MENU UTAMA ===")
        print("Login sebagai:", username, "(" + role + ")")
        print("1. Buat Tiket")
        print("2. Lihat Tiket & Antrean")
        print("3. Ubah Status Tiket")
        batas = 3
        if role == "Admin":
            print("4. Hapus Tiket")
            print("5. Lihat Daftar Pengguna")
            batas = 5
        print("0. Logout")

        menu = input_pilihan("Pilih menu: ", 0, batas)

        if menu == 0:
            break
        elif menu == 1:
            buat_tiket()
        elif menu == 2:
            lihat_tiket()
        elif menu == 3:
            ubah_status()
        elif menu == 4:
            hapus_tiket()
        elif menu == 5:
            lihat_pengguna()


def login():
    bersihkan_layar()
    print("=== LOGIN ===")
    role = None
    percobaan = 0
    username = ""
    while role is None and percobaan < MAKS_PERCOBAAN:
        username = input("Username : ")
        password = input("Password : ")
        role = cek_login(username, password)
        if role is None:
            percobaan += 1
            print("Username atau password salah!")

    if role is None:
        print("Percobaan login habis.")
        jeda()
    else:
        menu_utama(username, role)


while True:
    bersihkan_layar()
    print("=== SISTEM TIKET CUCI KENDARAAN ===")
    print("1. Login")
    print("2. Register")
    print("0. Keluar")
    pilih = input_pilihan("Pilih menu: ", 0, 2)

    if pilih == 0:
        bersihkan_layar()
        print("Terima kasih. Program selesai.")
        break
    elif pilih == 1:
        login()
    elif pilih == 2:
        register()