# batas = 5
# for i in range(batas):
#     print("Perulangan ke-", i)

# for sapa in range (5):
#     print("halo, selamat siang")

# pratikum = ["apd" , "orsikom" , "jarkom", 70, 89, 77]
# for i in pratikum:
#     # print(i)
#     print(i, end=" ")

# for i in range (1,10,2):
#     print("angka ke-i adalah", 1)

# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#          print(f'{i} x {j} = {i * j}')
# print('') #biar ada jarak tiap iterasi

# jawab = "ya"
#      hitung = 0
#     while(jawab == "ya"):
#     hitung += 1
# jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")

# 
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

tinggi = int(input("masukan tinggi yang dimau : "))
for i in range(tinggi):
    print(" " * (tinggi - i -1), end="")
    print("*" * (1+i))