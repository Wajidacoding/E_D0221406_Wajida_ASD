brg = []

perintah = 0

while perintah != 7 :
  print('''
  1. menambahkan
  2. menghapus
  3. mengedit
  4. menampilkan
  5. mencari barang
  6. mencari index
  7. keluar 
   ''')
  perintah = int(input("masukkan perintah :"))

  if perintah == 1:
    while True :
      x = input("masukkan barang :")
      brg.append(x)

      print("barang sekarang :",brg)

      stop = input("ketik y untuk berhenti : ")
      if stop == "y":
        break
  elif perintah == 2:
   while True :
     hps = int(input("masukkan index yang akan dihapus :"))
     print(brg.pop(hps),"telah di hapus")
    
     stop = input("ketik y untuk berhenti : ")
     if stop == "y":
       break

  elif perintah == 3:
    while True :
      edit = int(input("masukkan index yang akan di edit :"))
      if edit > (len(brg)):
        print("index tidak ditemukan")
      else :
        brg[edit] = input("masukkan barang baru :")
        
        stop = input("ketik y untuk berhenti : ")
        if stop == "y":
          break


  
  elif perintah == 4:
    for i in range(len(brg)) :
      print("masukkan barang sakarang :",brg[i])

      stop = input("ketik y untuk berhenti : ")
      if stop == "y":
         break

  elif perintah == 5:
    cari = input("masukkan barang yang akan di cek :")
    for i in range(len(brg)) :
      if brg[i] == cari :
        print("barang ada dalam list")
      else :
        print("barang tidak di temukan")
 
  elif perintah == 6:
    cari2 = input("masukkan barang ya di cari :")
    print("berada di index",brg.index(cari2))
    
    stop = input("ketik y untuk berhenti : ")
    if stop == "y":
         break

  elif perintah > 7 :
      print('periksa perintah anda')



