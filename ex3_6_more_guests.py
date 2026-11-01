# 3-6. More Guests
guests = ["Albert Einstein", "Isaac Newton", "Marie Curie"]
print("Kabar baik! Saya menemukan meja makan yang lebih besar.\n")

guests.insert(0, "Ada Lovelace")
guests.insert(2, "Alan Turing")
guests.append("Stephen Hawking")

for guest in guests:
    print(f"Yang terhormat {guest}, saya mengundang Anda untuk makan malam.")
