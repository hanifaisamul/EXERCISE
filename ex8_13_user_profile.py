# 8-13. User Profile
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
user = build_profile("Muhammad Royyan", "Abdurrofi", age=21, major="Teknik Komputer", city="Bandung")
print(user)
