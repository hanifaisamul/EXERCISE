# 5-10. Checking Usernames
current_users = ["John", "Admin", "Sarah", "Mike", "Alex"]
new_users = ["mike", "john", "David", "Emma", "LUCY"]
current_users_lower = [u.lower() for u in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Nama '{new_user}' sudah digunakan. Silakan masukkan nama pengguna lain.")
    else:
        print(f"Nama '{new_user}' tersedia.")
