#membuat contoh set
nama ={"wajida",10,"true"}

#menampilkan set dengan menggunakan perulangan
for i in nama :
    print(i)

#mengupdate salah satu set
#menghapus salah satu set
nama.remove("wajida")
print(nama)

nama.pop()
print(nama)

#menambahkan set
nama.add("false")
print(nama)

nama.update({"mangga","kuda"})
print(nama)

