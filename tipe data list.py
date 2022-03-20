#membuat contoh list
angka = ["1","2","3","4","5"]
#menampilkan list dengan perulangan
for i in angka :
    print(i)

b = 0
while b < len(angka) :
    print(angka[b])
    b += 1
#mengupdate salah satu list
angka [2] = "6"
print(angka)
#menghapus salah satu list
angka.remove("1")
print(angka)

del angka[1]
print(angka)

angka.pop ()
print(angka)
#menambahkan list
angka.append("8")
print(angka)

angka.insert(1,"9")
print(angka)


                                                                                            
