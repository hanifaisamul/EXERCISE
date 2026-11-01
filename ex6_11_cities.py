# 6-11. Cities
cities = {
    "Tokyo": {"country": "Jepang", "population": "14 juta", "fact": "Kota terpadat di dunia."},
    "Bandung": {"country": "Indonesia", "population": "2.5 juta", "fact": "Dikenal sebagai Kota Kembang."},
    "Paris": {"country": "Prancis", "population": "2.1 juta", "fact": "Dikenal sebagai Kota Cahaya."}
}
for city, info in cities.items():
    print(f"\nKota: {city}")
    print(f"  Negara: {info['country']}")
    print(f"  Populasi: {info['population']}")
    print(f"  Fakta: {info['fact']}")
