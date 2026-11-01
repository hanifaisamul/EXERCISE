# 7-6. Three Exits
# Menggunakan flag active
active = True
while active:
    inp = input("Ketik 'quit' untuk keluar: ")
    if inp == 'quit':
        active = False
    else:
        print(f"Input: {inp}")
