#membuat contoh tuple
warna =('merah', 'kuning', 'hijau', 'biru', 'ungu')
#menampilkan tuple dengan menggunakan perulangan
for i in warna :
    print(i)

b = 0
while b < len(warna) :
    print(warna[b])
    b += 1
#mengapdute salah satu tuple
w = list(warna)
w [2] = "jingga"
warna = tuple (w)
print(warna)
#menghapus salah satu tuple
w = list(warna)
w.remove("biru")
warna = tuple (w)
print(warna)

w = list(warna)
w.pop ()
warna = tuple (w)
print(warna)
#menambahkan tuple
w = list(warna)
w.append("putih")
warna = tuple (w)
print(warna)

w = list(warna)
w.insert(2,"hitam")
warna = tuple(w)
print(warna)


