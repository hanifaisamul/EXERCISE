# 7-5. Movie Tickets
while True:
    age_input = input("Masukkan umur Anda (ketik 'quit' untuk keluar): ")
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    if age < 3:
        print("Tiket gratis!")
    elif age <= 12:
        print("Harga tiket $10.")
    else:
        print("Harga tiket $15.")
