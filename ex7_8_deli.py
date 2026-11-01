# 7-8. Deli
sandwich_orders = ["tuna", "turkey", "egg salad"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Saya telah membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)
print("\nSandwich yang telah selesai dibuat:", finished_sandwiches)
