lemari = ["baju", "celana", 69, 7.2, True, 70, 222, 240]   

print("Sebelum diubah")
print(lemari)

angka1 =[ [1, 2], [3, 4] ] 
print(angka1[0][1])
angka2 = [2, 4, 6]
# gabungan = angka1 + angka2
# print(gabungan)
ulang = angka1 * 3
print(ulang)
lemari.remove ("baju")
lemari [0:2] = ["celana panjang", "Jaket", "Jas hujan"]

print("Sesudah diubah")
print(lemari)
print("Sebelum di Insert")
print(lemari)
lemari.insert(1, "KTP")
print("Sesudah di Insert")
print(lemari)

for item in lemari:
    if type(item) == int:
        jumlah += 1
    print(jumlah)

angka = (1, 2, 3, "halo", True)
angka = list("angka")
any.append("hai")

angka = tuple(any)
print(angka)

lemari = ("baju", "celana", "sepatu")
(atasan, *bawahan) = lemari

print(bawahan)