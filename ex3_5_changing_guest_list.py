# 3-5. Changing Guest List
guests = ["Albert Einstein", "Nikola Tesla", "Marie Curie"]
cant_make_it = guests.pop(1)
print(f"Sayangnya, {cant_make_it} tidak dapat hadir.\n")

guests.insert(1, "Isaac Newton")
for guest in guests:
    print(f"Yang terhormat {guest}, saya mengundang Anda untuk makan malam.")
