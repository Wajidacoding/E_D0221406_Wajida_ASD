#membuat dictionary dan mengisi value/nilai kedalamnya
data = {'nama' : 'wajida' ,'lahir' : 100602,'alamat' : 'lelupang'}

#menampilkan dictionary menggunakan  perulangan
for i in data :
    print(i,"->",data[i])
    
#mengupdate value/ nilai ke dalam dictionarya
data['lahir'] = 'hari'
print(data)
    
#menghapus salah satu dictionary
data.pop('alamat')
print(data)

#menambahkan dictionary
data['senin'] = 'jam '
print(data)


