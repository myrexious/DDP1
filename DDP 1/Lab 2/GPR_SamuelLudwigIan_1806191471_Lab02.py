pengeluaran = int(input("Masukkan jumlah pengeluaran : Rp"))
kembalian = 5000000-pengeluaran
if kembalian >= 0:
    print("Kembaliannya adalah Rp",kembalian, "yang dipecah dalam :")
    #uang 100k
    seratusRibuan = kembalian // 100000
    sisaseratusRibuan = kembalian % 100000
    #uang 50k
    limaplhRibuan = sisaseratusRibuan // 50000
    sisalimaplhRibuan = sisaseratusRibuan % 50000
    #uang 20k
    duaplhRibuan = sisalimaplhRibuan // 20000
    sisaduaplhRibuan = sisalimaplhRibuan % 20000
    #uang 10k
    seplhRibuan = sisaduaplhRibuan // 10000
    sisaseplhRibuan = sisaduaplhRibuan % 10000
    #uang 5k
    limaRibuan = sisaseplhRibuan // 5000
    sisalimaRibuan = sisaseplhRibuan % 5000
    #uang 2k
    duaRibuan = sisalimaRibuan // 2000
    sisaduaRibuan = sisalimaRibuan % 2000
    #SECENG
    seRibuan = sisaduaRibuan // 1000
    sisaseRibuan = sisaduaRibuan % 1000
    print(seratusRibuan, "lembar 100 ribuan,", limaplhRibuan, "lembar 50 ribuan,", duaplhRibuan, "lembar 20 ribuan,\n", seplhRibuan
      , "lembar 10 ribuan,", limaRibuan, "lembar 5 ribuan,", duaRibuan, "lembar 2 ribuan,\n", seRibuan, "lembar 1 ribuan.")
else:
    print('Input tidak valid')
