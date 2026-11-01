# 3-7. Shrinking Guest List
guests = ["Ada Lovelace", "Albert Einstein", "Alan Turing", "Isaac Newton", "Marie Curie", "Stephen Hawking"]
print("Maaf, meja baru belum sampai tepat waktu. Saya hanya bisa mengundang dua orang.\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, saya tidak dapat mengundang Anda ke makan malam.")

print()
for guest in guests:
    print(f"Halo {guest}, Anda masih diundang ke makan malam!")

del guests[0]
del guests[0]
print(f"Daftar tamu akhir: {guests}")
