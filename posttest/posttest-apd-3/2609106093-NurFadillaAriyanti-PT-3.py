nama = "dila"
nim = 93

Nama = str(input("Masukkan nama anda : "))
NIM = int(input("Masukkan NIM anda : "))
if Nama == nama and NIM == nim:
    print('''
    Daftar Penyewaan PS:
    1. PS4 : Rp. 10.000/jam
    2. PS4 Pro : Rp. 15.000/jam
    3. PS5 : Rp. 20.000/jam
    ''')
    pilihan = int(input("Pilih Jenis Sewa yang Anda Pilih : ")) 
    if pilihan == 1:
        jam = int(input("Masukkan Jumlah Jam Sewa : "))
        harga = 10000*jam
        if jam >= 5:
            diskon = 0.08*harga
        elif jam >= 3:
            diskon = 0.05*harga
        else:   
            diskon = 0*harga
        waktu = str(input("apakah sewa dilakukan saat weekend atau weekdays : "))
        if waktu == "weekend":
            hari = 0.1*harga
            total_harga = harga - diskon + hari
            print(f"Total yang anda bayar adalah:{total_harga}")
        else:
            total_harga = harga - diskon
            print(f"Total yang anda bayar adalah:{total_harga}")
            
    elif pilihan == 2:
        jam = int(input("Masukkan Jumlah Jam Sewa : "))
        harga = 15000*jam
        if jam >= 5:
            diskon = 0.08*harga
        elif jam >= 3:
            diskon = 0.05*harga
        else:
            diskon = 0*harga
        waktu = str(input("apakah sewa dilakukan saat weekend atau weekdays : "))
        if waktu == "weekend":
            hari = 0.1*harga
            total_harga = harga - diskon + hari
            print(f"Total yang anda bayar adalah:{total_harga}")
        else:
            total_harga = harga - diskon
            print(f"Total yang anda bayar adalah:{total_harga}")    
            
    elif pilihan == 3:
        jam = int(input("Masukkan Jumlah Jam Sewa : "))
        harga = 20000*jam
        if jam >= 5:
            diskon = 0.08*harga
        elif jam >= 3:
            diskon = 0.05*harga
        else:
            diskon = 0*harga
        waktu = str(input("apakah sewa dilakukan saat weekend atau weekdays : "))
        if waktu == "weekend":
            hari = 0.1*harga
            total_harga = harga - diskon + hari
            print(f"Total yang anda bayar adalah:{total_harga}")
        else:
            total_harga = harga - diskon
            print(f"Total yang anda bayar adalah:{total_harga}")
    else:
        print("daftar sewa tidak ada")
else:
    print("ERROR!")