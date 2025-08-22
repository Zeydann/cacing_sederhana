import random

welcome_message = "WELCOME TO GAME ANAK ANAK!"
cacing_position = random.randint(1, 4)

print (f''' 
       
{welcome_message}
        
       ''')

nama_user = input("masukan nama kamu: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 # INI TETAP HARUS KOSONG

goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU SI CACING

goa[cacing_position - 1] = "|0_0|"

print(f'''
halo selamat datang {nama_user}! Coba perhatikan goa di bawah ini

{goa_kosong}  

''')

pilihan_user = int(input("Menurut kamu di goa berapa cacing berada? [1/2/3/4]: "))

confirm_user = input(f"apakah kamu yakin dengan pilihan kamu {pilihan_user}? y/n?")

if confirm_user == "n":
    print("Program dihentikan")
    exit()
elif confirm_user == "y":
    if pilihan_user == cacing_position:
        print(f"{goa}, \n Selamat Kamu Menang!")
    else:
        print(f"{goa}, \n Maaf Anda Salah!")
else:
    print("Silahkan ulangi programnya!")
    exit()