# 6-5. Rivers
rivers = {"Nile": "Egypt", "Amazon": "Brazil", "Yangtze": "China"}
for river, country in rivers.items():
    print(f"Sungai {river} mengalir di negara {country}.")
print("\nNama Sungai:")
for river in rivers.keys():
    print(river)
print("\nNama Negara:")
for country in rivers.values():
    print(country)
