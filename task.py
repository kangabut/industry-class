
# Menu Fungsi
while True:
    print("\nMenu:")
    print("1. Operasi Aritmatika & Conditional Statements")
    print("2. Loops, Break & Continue Statements")
    print("3. Fungsi, Conditional Statements & Operator Logika")
    print("4. Operator Perbandingan & Conditional Statements")
    print("5. Penggunaan Fungsi, Loops & Fungsi Bawaan Python")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == '1':
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
        print("Fungsi Sudah Berakhir😉")
        user_input = input("Tekan Q untuk Keluar atau Tekan Enter untuk Kembali!😉👌")
        if user_input.lower() == 'q':
            print("Keluar dari program.")
            break
    elif menu == '2':
        #  Loops, Break & Continue Statements:
        for angka in range(1, 21):
            if angka % 4 == 0:
                print("Buzz")
                continue
            elif angka == 15:
                print(angka)
                break
            else:
                print(angka)
        print("Fungsi Sudah Berakhir😉")
        user_input = input("Tekan Q untuk Keluar atau Tekan Enter untuk Kembali!😉👌")

        if user_input.lower() == 'q':
            print("Keluar dari program.")
            break
    elif menu == '3':
        # Fungsi, Conditional Statements & Operator Logika

        def nilai_terbesar_dan_tambah_lima(nilai1, nilai2, nilai3):
            # Konversi input menjadi tipe data float
            nilai1 = float(nilai1)
            nilai2 = float(nilai2)
            nilai3 = float(nilai3)
            
            nilai_terbesar = max(nilai1, nilai2, nilai3)
            
            if nilai_terbesar % 2 == 1:
                nilai_terbesar += 5
            
            return nilai_terbesar

        # Input nilai sebagai string
        nilai1 = input("Masukkan Nilai1 : ")
        nilai2 = input("Masukkan Nilai2 : ")
        nilai3 = input("Masukkan Nilai3 : ")

        # Panggil fungsi dan cetak hasil
        hasil = nilai_terbesar_dan_tambah_lima(nilai1, nilai2, nilai3)
        print("Nilai terbesar setelah penambahan (jika ganjil):", hasil)

        
        print("Fungsi Sudah Berakhir😉")
        user_input = input("Tekan Q untuk Keluar atau Tekan Enter untuk Kembali!😉👌")
        if user_input.lower() == 'q':
            print("Keluar dari program.")
            break
    elif menu == '4':
        # Operator Perbandingan & Conditional Statements

        def cek_usia(usia):
            if usia > 18:
                print("Anda sudah dewasa")
            elif 13 <= usia <= 18:
                print("Anda remaja")
            else:
                print("Anda masih anak-anak")
        try:
            usia_pengguna = int(input("Masukkan usia Anda: "))
            cek_usia(usia_pengguna)
        except ValueError:
            print("Mohon masukkan angka sebagai usia.")
        print("Fungsi Sudah Berakhir😉")
        user_input = input("Tekan Q untuk Keluar atau Tekan Enter untuk Kembali!😉👌")
        if user_input.lower() == 'q':
            print("Keluar dari program.")
            break
    elif menu == '5':
        # Penggunaan Fungsi, Loops & Fungsi Bawaan Python

        def jumlah_angka_genap(daf_angka):
            angka_genap = [angka for angka in daf_angka if angka % 2 == 0]
            total = sum(angka_genap)
            total_string_length = len(str(total))
            return total_string_length

        # Meminta pengguna untuk memasukkan angka secara manual, dipisahkan dengan koma
        input_angka = input("Masukkan angka-angka dipisahkan dengan koma (contoh: 1,2,3,4,5): ")
        list_angka = [int(angka) for angka in input_angka.split(',')]

        panjang_hasil = jumlah_angka_genap(list_angka)
        print("Panjang hasil penjumlahan angka genap:", panjang_hasil)

        print("Fungsi Sudah Berakhir😉")
        user_input = input("Tekan Q untuk Keluar atau Tekan Enter untuk Kembali!😉👌")
        if user_input.lower() == 'q':
            print("Keluar dari program.")
            break
    elif menu == '6':
        print("Terima kasih! Sampai jumpa lagi😉.")
        break
    else:
        print("Masukkan Pilihan Yang Bener Dong😉 (1/2/3/4/5/6).")

