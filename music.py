import pygame
import os
from tabulate import tabulate
import time

"""
Informasi :

Sebelum menggunakan program ada beberapa library yang harus diinstal.

- pygame (pip3 install pygame)
- tabulate (pip3 install tabulate)
- time (pip3 install time)

Penggunannya di command prompt atau terminal Visual Studio Code.

Note : 

Jika ada error tentang FFMPEG maka harus install terlebih dahulu dan memasang ffmpeg ke PATH.
> Cara Install FFMPEG
> 1. Download : https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
> 2. Extract ZIP
> 3. Sebelumnya, buat dulu folder dengan nama "ffmpeg" di drive C: setelah itu masukkan isi dari ZIP yang sudah diextract.
> 4. Setelah itu copy PATH dari folder "ffmpeg" seperti : "C:\ffmpeg" ke PATH Environment.
> 5. Selesai.


Jika ada error ketika menjalankan program maka harus menginstal library yang dibutuhkan terlebih dahulu.



Tentang Program:

Program ini adalah aplikasi pemutar musik sederhana yang dibangun menggunakan Python. Program ini memanfaatkan library pygame untuk memainkan file audio dan library tabulate untuk menampilkan playlist dalam bentuk tabel yang rapi. Pengguna dapat melakukan beberapa operasi dasar seperti memutar, menjeda, melanjutkan, dan menghentikan lagu, serta mengatur volume dan melihat daftar putar.

Program ini juga dilengkapi dengan fitur login dan registrasi pengguna. Pengguna dapat mendaftar dengan username dan password yang unik, dan kemudian login untuk mengakses fitur-fitur pemutar musik.

Sebelum menggunakan program, pengguna disarankan untuk menginstal beberapa library yang diperlukan, yaitu pygame dan tabulate. Selain itu, jika terjadi masalah terkait FFMPEG, pengguna harus menginstal FFMPEG dan menambahkannya ke PATH.

Program ini memiliki tampilan antarmuka yang menarik dengan menggunakan warna dan teks yang kreatif. Pengguna dapat melihat daftar menu, memilih menu yang diinginkan, dan menikmati pengalaman mendengarkan musik dengan mudah.

Selamat menikmati penggunaan program ini!


"""



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class MusicPlayer:
    def __init__(self, file_paths):
        pygame.init()
        pygame.mixer.init()
        self.playlist = [os.path.abspath(file_path) for file_path in file_paths]
        self.current_song_index = 0

    def play(self):
        pygame.mixer.music.load(self.playlist[self.current_song_index])
        pygame.mixer.music.play()
        self.resume()
        while not pygame.mixer.music.get_busy():  
            pygame.time.wait(100)  

    def pause(self):
        pygame.mixer.music.pause()
        while not pygame.mixer.music.get_pos():  
            pygame.time.wait(100)  


    def resume(self):
        pygame.mixer.music.unpause()
        while not pygame.mixer.music.get_busy():  
            pygame.time.wait(100) 
        

    def stop(self):
        pygame.mixer.music.stop()
        while not pygame.mixer.music.get_pos():  
            pygame.time.wait(100)  
        

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.play()
        self.resume()
        while not pygame.mixer.music.get_busy(): 
            pygame.time.wait(100)  

    def set_volume(self, volume):
        volume_normalized = volume / 100.0
        pygame.mixer.music.set_volume(volume_normalized)



    def get_current_volume(self):
        return pygame.mixer.music.get_volume()

    def get_current_volume_percentage(self):
        return int(self.get_current_volume() * 100)

    def print_playlist(self):
        playlist_table = [["No.", "Song"]]
        for i, song_path in enumerate(self.playlist):
            playlist_table.append([i+1, os.path.basename(song_path)])
        print(warna.bold+warna.kuning+tabulate(playlist_table, headers="firstrow", tablefmt="rounded_grid")+warna.reset)
        
        lanjut()






    

def register(users):
    while True:
        try:
            username = input(warna.bold + warna.hijau + "Masukkan Username >> "+warna.reset)
            while not username:  
                error("Username tidak boleh kosong. Silakan coba lagi.")
                username = input(warna.bold + warna.hijau + "Masukkan Username >> "+warna.reset)
            while any(user.username == username for user in users):
                error("Username sudah digunakan. Silakan coba lagi.")
                username = input(warna.bold + warna.hijau + "Masukkan Username >> "+warna.reset)
            password = input(warna.bold + warna.kuning + "Masukkan Password >> " + warna.reset)
            while not password:  
                error("Password tidak boleh kosong. Silakan coba lagi.")
                password = input(warna.bold + warna.kuning + "Masukkan Password >> " + warna.reset)
            users.append(User(username, password))
            berhasil("Registrasi berhasil. Silakan login.")
            lanjut()
            return
        except Exception as e:
            error("Terjadi kesalahan:", str(e))

def login(users):
    while True:
        try:
            username = input(warna.bold + warna.hijau+"Masukkan Username >> "+warna.reset)
            while not username:  
                error("Username tidak boleh kosong. Silakan coba lagi.")
                username = input(warna.bold + warna.hijau+"Masukkan Username >> "+warna.reset)
            password = input(warna.bold + warna.kuning+"Masukkan Password >> "+warna.reset)
            while not password:  
                error("Password tidak boleh kosong. Silakan coba lagi.")
                password = input(warna.bold + warna.kuning+"Masukkan Password >> "+warna.reset)
            # Validasi login
            for user in users:
                if user.username == username and user.password == password:
                    berhasil("Login berhasil!")
                    lanjut()
                    return True
            error("Login gagal. Username atau password salah.")
            lanjut()
            return False
        except Exception as e:
            error("Terjadi kesalahan:", str(e))




def print_status(player):
    # print(warna.bold+"================================================================")
    print(warna.hijau+'''
█▀ ▀█▀ ▄▀█ ▀█▀ █░█ █▀   ▀
▄█ ░█░ █▀█ ░█░ █▄█ ▄█   ▄
    '''+warna.reset)
    if pygame.mixer.music.get_busy():
        print(warna.bold+">> \tNow Playing :", os.path.basename(player.playlist[player.current_song_index]))
        print(">> \tVolume :", player.get_current_volume_percentage(), "%" + warna.reset)
    else:
        info("\tTidak ada lagu yang sedang diputar")
    print(warna.bold+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"+warna.reset)



def menuUtama():
    
    file_paths = ["wte bad.wav", "geazy.mp3"]  
    player = MusicPlayer(file_paths)
    
    while True:
        bersihkan_layar() 
        headerUtama()    
        
        print_status(player)
        print_menu()
        choice = input(warna.bold+"Masukkan Pilihan >> "+warna.reset)

        if choice == "1":
            player.play()
        elif choice == "2":
            player.pause()
        elif choice == "3":
            player.resume()
        elif choice == "4":
            player.stop()
        elif choice == "5":
            player.next_song()
        elif choice == "6":
            volume = float(input(warna.bold + warna.kuning + "[INFO] >> " +"Masukkan Volume (0 - 100): "+warna.reset))
            player.set_volume(volume)
        elif choice == "7":
            player.print_playlist()
        elif choice == "8":
            bersihkan_layar()
            senyum()
            player.stop()
            lanjut()
            bersihkan_layar()
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang valid.")




def main():
    users = []
    headerAwal()
    time.sleep(3)
    while True:
        
        bersihkan_layar()
        print(warna.bold+warna.kuning+tabulate([["Selamat Datang Pendengar Spotube Setia!"], ["1. Login"], ["2. Register"], ["3. Quit"]], tablefmt="rounded_grid")+warna.reset)
        choice = input(warna.bold+"Pilih Menu >> ")

        if choice == "1":
            if login(users):
                menuUtama()
        elif choice == "2":
            register(users)
        elif choice == "3":
            bersihkan_layar()
            senyum()
            lanjut()
            break
        else:
            error("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
            lanjut()

def error(p):
    print(warna.merah + "[ERROR] >> " + p + warna.reset)

def berhasil(p):
    print(warna.hijau + "[BERHASIL] >> " + p + warna.reset)

def info(p):
    print(warna.bold + warna.kuning + "[INFO] >> " + p + warna.reset)

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

class warna:
    ungu = "\033[95m"
    hijau = "\033[92m"
    kuning = "\033[93m"
    bold = "\033[1m"
    underline = "\033[4m" 
    merah = "\033[91m"
    reset = "\033[0m"

def senyum():
    print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⠿⣿⣿⣿⣿⡿⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⡈⠻⣦⣤⣿⣿⣧⣤⣶⠏⢀⣦⣄⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣷⣤⣈⠙⠛⠛⠛⢉⣠⣴⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢠⣿⣿⣿⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⣿⣆⠀⠀⠀⠀
        ⠀⠀⠀⢀⣿⣿⣿⣿⠃⣰⣿⣿⡿⠛⠋⠉⠛⠻⣿⣿⣷⡀⠹⣿⣿⣿⡆⠀⠀⠀
        ⠀⠀⠀⣸⣿⣿⣿⠃⣰⣿⣿⠋⣠⣾⡇⢸⣷⣦⠈⣿⣿⣿⡄⢹⣿⣿⣿⠀⠀⠀
        ⠀⠀⠀⣿⣿⣿⠋⠀⠉⠉⠉⠀⣿⣿⡇⢸⣿⣿⡇⠉⠉⠉⠁⠀⢻⣿⣿⡆⠀⠀
        ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
        ⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀
          
    ▀█▀ █▀▀ █▀█ █ █▀▄▀█ ▄▀█   █▄▀ ▄▀█ █▀ █ █░█
    ░█░ ██▄ █▀▄ █ █░▀░█ █▀█   █░█ █▀█ ▄█ █ █▀█
''')

def garis():
    print("━"*65)

def lanjut():
    print("\n")
    garis()
    print(warna.bold + warna.kuning + "Press ENTER "+warna.reset + warna.bold +"untuk melanjutkan..." + warna.reset)
    garis()
    input()

def headerAwal():
    print(warna.bold + warna.kuning+'''

░██████╗████████╗░█████╗░██████╗░████████╗  ██╗░░░██╗░█████╗░██╗░░░██╗██████╗░
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗
╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░  ░╚████╔╝░██║░░██║██║░░░██║██████╔╝
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░  ░░╚██╔╝░░██║░░██║██║░░░██║██╔══██╗
██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░  ░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝

░░░░░██╗░█████╗░██╗░░░██╗██████╗░███╗░░██╗███████╗██╗░░░██╗  ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░██╗
░░░░░██║██╔══██╗██║░░░██║██╔══██╗████╗░██║██╔════╝╚██╗░██╔╝  ████╗░████║██║░░░██║██╔════╝██║██╔══██╗██║
░░░░░██║██║░░██║██║░░░██║██████╔╝██╔██╗██║█████╗░░░╚████╔╝░  ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝██║
██╗░░██║██║░░██║██║░░░██║██╔══██╗██║╚████║██╔══╝░░░░╚██╔╝░░  ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗╚═╝
╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░╚███║███████╗░░░██║░░░  ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝██╗
░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝
'''+warna.reset)

def headerUtama():
    print(warna.bold + warna.kuning +'''
████████████████████████████████████████████████████████████████████████████
█─▄▄▄▄█▄─▄▄─█─▄▄─█─▄─▄─█▄─██─▄█▄─▄─▀█▄─▄▄─███▄─▀█▀─▄█▄─██─▄█─▄▄▄▄█▄─▄█─▄▄▄─█
█▄▄▄▄─██─▄▄▄█─██─███─████─██─███─▄─▀██─▄█▀████─█▄█─███─██─██▄▄▄▄─██─██─███▀█
▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀
'''+warna.reset)

def print_menu():
    print(warna.bold+"\n\nDaftar Menu : ")
    menu = [
        ["1. Play", "2. Pause", "3. Resume", "4. Stop"],
        ["5. Next Song", "6. Set Volume", "7. Show Playlist", "8. Logout"]
    ]
    print(warna.kuning+warna.bold+tabulate(menu, tablefmt="rounded_grid")+warna.reset)


if __name__ == "__main__":
    main()
