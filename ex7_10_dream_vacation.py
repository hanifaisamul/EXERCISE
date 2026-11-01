# 7-10. Dream Vacation
responses = {}
polling_active = True
while polling_active:
    name = input("Nama Anda: ")
    place = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")
    responses[name] = place
    repeat = input("Apakah ada orang lain yang ingin mengisi survei? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Hasil Survei Liburan Impian ---")
for name, place in responses.items():
    print(f"{name} ingin mengunjungi {place}.")
