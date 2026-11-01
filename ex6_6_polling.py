# 6-6. Polling
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}
people = ["jen", "budi", "phil", "dian"]
for p in people:
    if p in favorite_languages:
        print(f"Terima kasih {p.title()} sudah mengisi survei!")
    else:
        print(f"Halo {p.title()}, silakan isi survei bahasa favorit Anda!")
