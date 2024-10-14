import os
from prettytable import PrettyTable

os.system("cls" if os.name == "nt" else "clear")

anime = []

#login
def login():
    print("\n===+++++=== Selamat datang kembali di AniTracker: Manajemen Koleksi Anime ===+++++===")
    print("1. Admin")
    print("2. User")
    role = input("Masukkan pilihan (1/2): ")
    if role == '1':
        return 'admin'
    elif role == '2':
        return 'user'
    else:
        print("Pilihan tidak sesuai! Kembali login!")
        return login()
    
#menambahkan koleksi anime (atmin/user)
def tambah():
    print("\n>>>>>>>>>>>>>>>=========+++++++#$#+++++++=========<<<<<<<<<<<<<<<")
    print("=======================+++ Judul anime +++=======================")
    print(">>>>>>>>>>>>>>>=========+++++++#$#+++++++=========<<<<<<<<<<<<<<<")
    judul = input("Masukkan judul anime: ")
    status = input("Apakah anata sudah menonton anime tersebut? (ya/tidak): ")
    anime.append({'judul': judul, 'status': status})

    #table judul
    table_tambah = PrettyTable()
    table_tambah.field_names = ["Judul anime", "Status tontonan"]
    table_tambah.add_row([judul, status])
    print(f"Anime dengan {judul} berhasil anata tambahkan ke koleksi!")
    print(table_tambah)

#melihat koleksi anime (atmin/user)
def lihat():
    if not anime:
        print("Koleksi anime kosong.")
    else:
        print("\n>>>>>>>>>>>>>>>=========+++++++#$#+++++++=========<<<<<<<<<<<<<<<")
        print("======================+++ Koleksi anime +++======================")
        print(">>>>>>>>>>>>>>>=========+++++++#$#+++++++=========<<<<<<<<<<<<<<<")

        #table melihat koleksi
        table_lihat_koleksi = PrettyTable()
        table_lihat_koleksi.field_names = ["No", "Judul Anime", "Status tontonan"]
        for index, item in enumerate(anime, 1):
            table_lihat_koleksi.add_row([index, item['judul'], item['status']])
        print(table_lihat_koleksi)

#update status koleksi anime (atmin)
def update():
    lihat() 
    print("\n>>>>>>>>>>>>>>>=========+++++++#$#+++++++=========<<<<<<<<<<<<<<<")
    print("===================+++ Update status anime +++===================")
    print(">>>>>>>>>>>>>>>=========+++++++#$#+++++++=========<<<<<<<<<<<<<<<")
    index = int(input("Masukkan nomer anime yang ingin anata update: "))
    if 1 <= index <= len(anime):
        status_baru = input("Apakah sudah anata tonton? (ya/tidak?): ")
        anime[index - 1]['status'] = status_baru
        print(f"Status anime anata {anime[index - 1]['judul']} berhasil diperbaharui!")
    
        #table update anime
        table_update = PrettyTable()
        table_update.field_names = ["Judul anime", "Status tontonan baru"]
        table_update.add_row([anime[index - 1]['judul'], status_baru])
        print("\nStatus berhasil diperbaharui di koleksi!")
        print(table_update)
    else: 
        print("Anime tidak ada dikoleksi!")

#hapus koleksi anime (user)
def hapus():
    lihat() 
    print("\n>>>>>>>>>>>>>>>=========+++++++#$#+++++++=========<<<<<<<<<<<<<<<")
    print("================+++ Hapus anime dari koleksi +++=================")
    print(">>>>>>>>>>>>>>>=========+++++++#$#+++++++=========<<<<<<<<<<<<<<<")
    index = int(input("Masukkan nomer anime yang ingin anata hapus: "))
    if 1 <= index <= len(anime):
        hapus = anime.pop(index - 1)

        #table hapus
        table_hapus = PrettyTable()
        table_hapus.field_names = ["Judul anime", "Status tontonan"]
        table_hapus.add_row([hapus['judul'], hapus['status']])
        print("\n Anime berhasil anata hapus dari koleksi!")
        print(table_hapus)
    else:
        print("Anime tidak ada dikoleksi!")

#menu atmin
def menu_admin():
    while True:
        print("\n===+***+ Menu Admin +***+===")
        print("1. Tambah koleksi anime")
        print("2. Lihat koleksi anime")
        print("3. Update koleksi anime")
        print("4. Hapus koleksi anime")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1-5): ")
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            lihat()
        elif pilihan == '3':
            update()
        elif pilihan == '4':
            hapus()
        elif pilihan == '5':
            break
        else:
            print("Tidak ada pilihan")

#menu user
def menu_user():
    while True:
        print("\n===+***+ Menu User +***+===")
        print("1. Tambah koleksi anime")
        print("2. Lihat koleksi anime")
        print("3. Hapus koleksi anime")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            lihat()
        elif pilihan == '3':
            hapus()
        elif pilihan == '4':
            break
    else:
        print("Tidak ada pilihan")

#main
def main():
    role = login()
    if role == 'admin':
            role = menu_admin()
    elif role == 'user':
            role = menu_user()

while True:
    main()