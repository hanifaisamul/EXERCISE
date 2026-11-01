# 7-9. No Pastrami
sandwich_orders = ["pastrami", "tuna", "pastrami", "turkey", "pastrami"]
print("Maaf, kedai kehabisan pastrami.\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("Pesanan tersisa:", sandwich_orders)
