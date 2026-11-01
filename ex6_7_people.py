# 6-7. People
person1 = {"first_name": "Royyan", "last_name": "Abdurrofi", "age": 21, "city": "Bandung"}
person2 = {"first_name": "Budi", "last_name": "Santoso", "age": 22, "city": "Jakarta"}
person3 = {"first_name": "Siti", "last_name": "Aminah", "age": 20, "city": "Surabaya"}
people = [person1, person2, person3]
for person in people:
    print(f"{person['first_name']} {person['last_name']}, Umur: {person['age']}, Kota: {person['city']}")
