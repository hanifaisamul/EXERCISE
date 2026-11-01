# 7-4. Pizza Toppings
prompt = "\nMasukkan topping pizza pilihan Anda (ketik 'quit' untuk selesai): "
while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"Menambahkan {topping} ke pizza Anda.")
