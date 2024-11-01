
x = [3, 3, 5, 2, 1, 4, 5, 6, 7, 5, 9, 8, 4, 7, 9, 2, 5, 1, 3, 2]
y = int(input("Masukkan Nilai yang Ingin Dicari: "))

if y % 2 == 0:  # Jika y adalah genap
    indeks_kemunculan = []  

    for i in range(len(x)):
        if x[i] == y: 
            indeks_kemunculan.append(i) 


    if indeks_kemunculan:
        print(f"Nilai {y} ditemukan di indeks: {indeks_kemunculan}")
    else:
        print(f"Nilai {y} tidak ditemukan dalam daftar.")
else:
    print("Tidak ada hasil karena nilai yang dicari adalah ganjil.")
