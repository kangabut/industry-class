def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Gabisa Dibagi 0"

first_run = True

while True:
    if first_run:
        input("Welcome to Kalkulator Low Budget😉👌. Tekan Enter untuk lanjut!")
        first_run = False
    else:
        user_input = input("Tekan Enter untuk lanjut, atau 'q' untuk quit: ")
        if user_input.lower() == 'q':
            print("Terima kasih! Sampai jumpa lagi😉.")
            break
        
        
    print("Kalkulator Low Budget:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Mau Yang Mana? : ")

    if pilihan == '5':
        print("Terima kasih! Sampai jumpa lagi😉.")
        break

    if pilihan in ['1', '2', '3', '4']:
        bilangan1 = int(input("Masukkan Bilangan Pertama: "))
        bilangan2 = int(input("Masukkan Bilangan Kedua: "))

        if pilihan == '1':
            hasil = tambah(bilangan1, bilangan2)
            print(f"Hasil penjumlahan: {hasil}")
        elif pilihan == '2':
            hasil = kurang(bilangan1, bilangan2)
            print(f"Hasil pengurangan: {hasil}")
        elif pilihan == '3':
            hasil = kali(bilangan1, bilangan2)
            print(f"Hasil perkalian: {hasil}")
        elif pilihan == '4':
            hasil = bagi(bilangan1, bilangan2)
            print(f"Hasil pembagian: {hasil}")
    else:
        print("Masukkan Pilihan Yang Bener Dong😉 (1/2/3/4/5/q/quit).")
