# Nama : Nabila Fitriani
# NIM  : 2509116063


print("------------------------------")
print("| SISTEM PENDAFTARAN ANTRIAN |")
print("|      PUSKESMAS MANTAP      |")
print("------------------------------")
print(" LOGIN ADMIN ")

print("--------------------------------")
username = str(input("USERNAME : "))
password = str(input("PASSWORD : "))

if username=="Nabila" and password=="063":
    print("Login Berhasil")
else:
    print("Username atau Password Salah!")
print("-----------------------------------")

Menu = str(input("pilih option yang tertera: "))

Daftar_Jenis_Layanan = [
    ["1. BPJS"],
    ["2. Umum"]
]

if Menu == "A":
    print("Pilih menggunakan BPJS")
elif Menu == "B":
    print("Pilih menggunakan umum")
else:
    print("Menu tidak tersedia, silahkan ulangi lagi!")

poli = int(input("Pilih layanan yang diinginkan: "))

Daftar_Poli = [
    ["1. Poli Umum"],
    ["2. Poli Gigi"],
    ["3. Poli KIA (Poli Anak)"],
    ["4. Poli Bumil"],
    ["5. Poli Lansia"],
    ["6. Poli Imunisasi"],
    ["7. Apotek"],
    ["8. Exit"]
]

if poli == 1 :
    print("Umum")
elif poli == 2 :
    print("Gigi")
elif poli == 3 :
    print("KIA(Poli Anak)")
elif poli == 4 :
    print("Bumil")
elif poli == 5 :
    print("Lansia")
elif poli == 6 :
    print("Imunisasi")
elif poli == 7 :
    print("Apotek")
elif poli == 8 :
    print("Exit")
else:
    print("Menu tidak tersedia!")


# form():
formulir = input("Lengkapi formulir di bawah ini!")

print("==================Formulir Pendaftaran==================")
nik           = int(input("NIK                              : ")) 
nama          = str(input("Nama                             : "))
tanggal_lahir = int(input("Tanggal Lahir                    : "))
jenis_kelamin = str(input("Jenis Kelamin                    : "))
umur          = int(input("Umur                             : "))
alamat        = str(input("Alamat                           : "))
no_hp         = int(input("No Hp                            : "))
poli          = str(input("Poli                             : "))
print()

# loket():
nomor_antrian = int(input())
print("nomor antrian anda adalah: ", nomor_antrian)
print()

# sruk_antrian():
print("======================================")
print("         PUSKESMAS MANTAP")
print("          KOTA SAMARINDA")
print("======================================")
print()
print("           NOMOR ANTRIAN",nomor_antrian)
print("           POLI", poli)
print()
print("   Terimakasih Atas Kunjungan Anda")
print("        Semoga Lekas sembuh")
print("   Senin, 15 September 2025 07.15")
print()