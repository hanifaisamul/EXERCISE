# 4-11. My Pizzas, Your Pizzas
pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]
friend_pizzas = pizzas[:]

pizzas.append("Meat Lover")
friend_pizzas.append("Hawaiian")

print("Pizza favorit saya:")
for p in pizzas:
    print(f"- {p}")

print("\nPizza favorit teman saya:")
for p in friend_pizzas:
    print(f"- {p}")
