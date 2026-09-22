merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000

merchandise = [merchandise_1, merchandise_2, merchandise_3, merchandise_4, merchandise_5, merchandise_6]

total_harga = merchandise[0] + merchandise[1] + merchandise[2] + merchandise[3] + merchandise[4] + merchandise[5] + 7500

rata_rata = total_harga / len(merchandise)

nim = 93 
bolean = nim > rata_rata 

kurs_usd = 17835
total_harga_usd = total_harga / kurs_usd

barang_2_sampai_4 = merchandise[-5:-2]
print("merchandise 1: Rp" , merchandise_1)

print("merchandise 2: Rp" , merchandise_2)
print("merchandise 3: Rp" , merchandise_3)
print("merchandise 4: Rp" , merchandise_4)
print("merchandise 5: Rp" , merchandise_5)
print("merchandise 6: Rp" , merchandise_6)

print("Data merchandise: ", merchandise)

print("Total Harga: Rp", total_harga)


print("Rata rata: Rp", rata_rata)

print("NIM: ", nim)
print("Hasil Perbandingan: ", bolean)

print("Total Harga USD: ", "USD", total_harga_usd)
print("Barang 2 sampai Barang 4: ", barang_2_sampai_4)