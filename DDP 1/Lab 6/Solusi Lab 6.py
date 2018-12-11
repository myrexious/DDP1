"""
Menghitung jumlah dari bilangan-bilangan dalam list yang kelipatan 3.
Dapat digunakan pada nested list
"""
def jumlah_kelipatan_3(arr):
    # base case, jika panjang arr hanya 1
    if len(arr) == 1:
        if type(arr[0]) == list:
            # Rekursi terus, jaga-jaga jika elemen ke-0
            # masih berupa list
            return jumlah_kelipatan_3(arr[0]) 
        elif type(arr[0]) == int:
            if arr[0]%3 == 0:
                # Ambil elemennya
                return arr[0]
            else:
                # Anggap saja 0 (tidak diambil)
                return 0

    # jika panjangnya lebih dari 1
    else:
        if type(arr[0]) == list:
            # Ambil elemen ke-0 sampai pasti integer (lihat base case)
            # Jumlahkan dengan elemen-elemen sisanya
            return jumlah_kelipatan_3(arr[0]) + jumlah_kelipatan_3(arr[1:])

        elif type(arr[0]) == int:
            # Langsung ambil saja elemen ke-0
            # dan jumlahkan dengan elemen-elemen sisanya
            if (arr[0]%3 == 0):
                return arr[0] + jumlah_kelipatan_3(arr[1:])

            else:
            # Anggap saja 0 (tidak diambil), lalu
            # jumlahkan dengan elemen-elemen sisanya
                return 0 + jumlah_kelipatan_3(arr[1:])

def main():
    masukan = eval(input("Masukkan list: "))
    ans = jumlah_kelipatan_3(masukan)
    print('Hasil penjumlahan bilangannya adalah', ans)

if __name__ == "__main__":
    main()
