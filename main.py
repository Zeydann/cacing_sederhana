import random
import sys

welcome_message = "WELCOME TO GAME ANAK ANAK!"
cacing_position = random.randint(1, 4)
yes_user = "y"

print (f''' 
       
{welcome_message}
        
       ''')

nama_user = input("masukan nama kamu: ")

print(f'''
halo selamat datang {nama_user}! Coba perhatikan goa di bawah ini

|1| |2| |3| |4|  

''')

pilihan_user = int(input("Menurut kamu di goa berapa cacing berada? [1/2/3/4]: "))

confirm_user = input(f"apakah kamu yakin dengan pilihan kamu {pilihan_user}? y/n?")

if confirm_user == yes_user:
    print(f"okeee {nama_user} kita lihat apakah pilihan kamu benarrr")
else:
    print(f"okeee {nama_user} game akan berhenti")
    sys.exit()

if pilihan_user == cacing_position:
    print(f"selamat {nama_user} kamu menang! posisi cacing ada di goa {cacing_position} dan plihan goa kamu adalah {pilihan_user}.")
else:
    print(f"tetottt cacing tidak di situu, tapi ada di goa nomor {cacing_position} sedangkan kamu memilih goa nomor {pilihan_user}.")