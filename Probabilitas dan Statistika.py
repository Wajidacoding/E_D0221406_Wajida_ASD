#mean
data = [0,0,1,2,2,4,6]
n = len(data)
jumlah = 0

for i in data :
    jumlah += i

print("jumlah : ",jumlah)
print("n :",n)
mean = jumlah/n
print("nilai mean adalah :",mean)

#median
data = [0,0,1,2,2,4,6]
if n % 2 == 0 :
    pass
else :
    u = (n +1)/2
    median = data[int(u)]
    print(u)
    print(median)
    print("4.0 karena nilai mean berada pada urutan ke 4")

#modus
data = [0,0,1,2,2,4,6]
counts = []
for i in data:
    counts.append(data.count(i))

max_count = max(counts)

mode = []
for i in data:
    if data.count(i) == max_count and i not in mode:
        mode.append(i)

if len(mode) == 1:
    print("Modus:", mode[0])
elif len(mode) > 1:
    print("Modus:", mode)
else:
    print("Tidak ada modus")


