# 3-10. Every Function
languages = ["Python", "C", "Java", "JavaScript", "Rust"]
languages.append("Go")
languages.insert(1, "C++")
del languages[2]
popped_lang = languages.pop()
languages.remove("Java")
print("Sorted:", sorted(languages))
languages.reverse()
languages.sort()
print("Final List:", languages)
print("Length:", len(languages))
