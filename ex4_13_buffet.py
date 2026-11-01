# 4-13. Buffet
menu = ("Nasi Goreng", "Mie Goreng", "Ayam Bakar", "Soto", "Es Teh")
print("Menu awal:")
for food in menu:
    print(food)

# menu[0] = "Nasi Uduk" # TypeError: 'tuple' object does not support item assignment

menu = ("Nasi Uduk", "Mie Goreng", "Ayam Goreng", "Soto", "Es Teh")
print("\nMenu baru:")
for food in menu:
    print(food)
