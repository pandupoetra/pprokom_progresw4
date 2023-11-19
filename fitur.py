# deklarasi array daftar pasien sebagai wadah penyimpan data pasien
daftar_pasien = []  
# fungsi untuk melakukan penambahan pasien

def tambah_pasien():
    #mencetak nilai awal tiap nomor urut
    num_PU=0
    num_PG=0
    num_PA=0
    num_LP=0
    #malakukan import modul datetime
    import datetime
    x = datetime.datetime.now()
    tanggal = x.strftime("%d %B %Y %H:%M:%S")
    while True:
        #mencetak tampilan awal saat amsuk ke fitur
        print("\n-----------------------------------------")
        print("Pilihan fasilitas dapat anda pilih".center(40))
        print("-----------------------------------------")
        print("1. Poli Umum")
        print("2. Poli Gigi")
        print("3. Poli Anak")
        print("4. Layanan Psikologi")
        print("5. Keluar")
        print("-----------------------------------------")
        #membuat varaiable pilihan untuk menyimpan inputan yang dimasukkan pasien
        pilihan = str(input("Pilih menu (1/2/3/4/5): "))
        #memasuki metode percabangan jika memilih salah satu menu
        if pilihan == "5":
            break
        elif pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4":
            while True:
                print("\n---------- Tambah Data Pasien -----------")
                nama = input("Masukkan nama pasien: ")
                try:
                    umur = int(input("Masukkan umur pasien: "))
                except:
                    print("Maaf, data umur harus dalam format angka\n")
                    break
                alamat = input("Masukkan alamat pasien: ")
                try:
                    nomor_telepon=int(input("Masukan nomor telepon pasien: "))
                except:
                    print("Maaf, data nomor telepon harus dalam format angka\n")
                    break
                keluhan = input("Masukkan keluhan pasien: ")
                if pilihan == "1":
                    if num_PU <= 1000:
                        num_PU += 1 
                        kode_PU = str(num_PU).zfill(3)
                        kode = "PU" + kode_PU
                    else:
                        print("Maaf untuk hari ini sudah mencapai batas kuota")
                elif pilihan == "2":
                    if num_PG <= 1000:
                        num_PG += 1
                        kode_PG = str(num_PG).zfill(3)
                        kode = "PG" + kode_PG
                    else:
                        print("Maaf untuk hari ini sudah mencapai batas kuota")
                elif pilihan == "3":
                    if num_PA <= 1000:
                        num_PA += 1
                        kode_PA = str(num_PA).zfill(3)
                        kode = "PA" + kode_PA
                    else:
                        print("Maaf untuk hari ini sudah mencapai batas kuota")
                elif pilihan == "4":
                    if num_LP <= 1000:
                        num_LP += 1
                        kode_LP = str(num_LP).zfill(3)
                        kode = "LP" + kode_LP
                    else:
                        print("Maaf untuk hari ini sudah mencapai batas kuota")
                #mendeklarasikan variabel pasien dalam dictionary
                pasien = {
                    "nama": nama,
                    "umur": umur,
                    "alamat": alamat,
                    "tanggal": tanggal,
                    "keluhan": keluhan,
                    "nomor urutan": kode,
                    "nomor telepon":nomor_telepon
                }
                #menambahkan pasien baru ke dalam variabel daftar pasien 
                if int(kode_PU) < 5 :
                    daftar_pasien.append(pasien)
                    print("\nData pasien", nama, "telah ditambahkan.")
                    print("Nomor urutan pasien", nama + ":", kode)
                    #cek ulang apakah ingin menambahkan lagi atau tidak
                    cek_ulang = input("Tambahkan data pasien lainnya? (ya/tidak): ")
                    if cek_ulang.lower() != "ya":
                        break
                else:
                    break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.\n")

#fungsi untuk melakukan edit data pasien 
def edit_pasien():
    print("\n---------- Edit Data Pasien -----------")
    #deklarasi dan inisialisasi dari nama pasien yang ingin diedit
    nama = input("Masukkan nama pasien: ")
    #melakukan pengecualian jika pasien tidak terdapat di variabel daftar pasien
    ketemu = False

    #melakukan pencetakan data dengan perulangan jika pasien ada didalam variabel daftar pasien
    for pasien in daftar_pasien:
        if pasien['nama'] == nama:
            ketemu = True
            print(f"\nData pasien dengan nama {nama} ditemukan. \nSilakan edit data berikut:")

            nama = input("Nama pasien: ")
            try:
                umur = int(input("Masukkan umur pasien: "))
            except:
                print("Maaf, data umur harus dalam format angka\n")
                break
            alamat  = input("Masukan Alamat pasien: ")
            nomor_telepon=int(input("Masukan nomor telepon pasien: "))
            keluhan = input("Masukan Keluhan pasien: ")

            pasien['nama'] = nama
            pasien['umur'] = umur
            pasien['alamat'] = alamat
            pasien['nomor telepon']=nomor_telepon
            pasien['keluhan'] = keluhan

            print("\nData pasien telah diperbarui.")
            break
    #mencetak opsi output jika data pasien tidak ditemukan dalam variabel daftar pasien 
    if not ketemu:
        print(f"Data pasien dengan nama {nama} tidak ditemukan.")

#fungsi untuk melakuakan hapus data pasien
def hapus_pasien():
    print("\n---------- Hapus Data Pasien -----------")
    #deklarasi dan inisialisasi dari nama pasien yang ingin dihapus
    nama = input("Masukkan nama pasien: ")
    chek_lagi=input(f"Apakah anda yakin ingin menghapus data pasien {nama} ? (ya/tidak): ")
    if chek_lagi=="ya":
        #melakukan pengecualian jika pasien tidak terdapat di variabel daftar pasien
        ketemu = False

        #melakukan pencetakan data dengan perulangan jika pasien ada didalam variabel daftar pasien
        for pasien in daftar_pasien:
            if pasien['nama'] == nama:
                ketemu = True
                daftar_pasien.remove(pasien)
                print(f"\nData pasien dengan nama {nama} telah dihapus.")
                break
        #mencetak opsi output jika data pasien tidak ditemukan dalam variabel daftar pasien
        if not ketemu:
            print(f"Data pasien dengan nama {nama} tidak ditemukan.")
    else:
        print("Proses dibatalakan")

def cari_pasien():
    # membuat informasi awal ketika masuk menu cari pasien
    print("\n---------- Cari Data Pasien -----------")
    # membuat variabel yang menyimpan nama pasien yang dingin dicari oleh user
    nama_cari = input("Masukkan nama pasien: ")
    ditemukan=False 
    #membuat perulangan untuk menyampaikan informasi pasien yang dicari
    for pasien in daftar_pasien:
        if pasien["nama"] == nama_cari:
            print("\n----------------------------------------")
            print("Faskes Sehat".center(40))
            print("----------------------------------------")
            print(f"Data pasien ditemukan:")
            print(f"Nama: {pasien['nama']}")
            print(f"Umur: {pasien['umur']}")
            print(f"Alamat: {pasien['alamat']}")
            print(f"Tanggal: {pasien['tanggal']}")
            print(f"Nomor Telepon: {pasien['nomer telepon']}")
            print(f"Keluhan: {pasien['keluhan']}")
            print(f"Nomor Urut: {pasien['nomor urutan']}")
            print("----------------------------------------")
            ditemukan = True
            break
    # membuat percabangan sebagai opsi jika nama pasien yang dicari tidak ditemukan
    if not ditemukan:
        print(f"Data pasien dengan nama {nama_cari} tidak ditemukan.")

def tampilkan_daftar_pasien():
    # membuat informasi awal ketika masuk menu cari pasien
    print("\n---------- Tampilkan Data Pasien -----------")
    # membuat percabangan sebagai opsi jika nama pasien tidak ada dalam variabel daftar pasien
    if not daftar_pasien:
        print("Daftar pasien kosong.")
    # membuat opsi jika nama pasien ditemukan
    else:
        print("\n----------------------------------------")
        print("Faskes Sehat".center(40))
        print("----------------------------------------")
        for pasien in daftar_pasien:
            print(f"Nama: {pasien['nama']}")
            print(f"Umur: {pasien['umur']}")
            print(f"Alamat: {pasien['alamat']}")
            print(f"Tanggal: {pasien['tanggal']}")
            print(f"Nomor Telepon: {pasien['nomer telepon']}")
            print(f"Keluhan: {pasien['keluhan']}")
            print(f"Nomor urut: {pasien['nomor urutan']}")
            print("----------------------------------------")
