from argon2 import PasswordHasher

pass_hasher = PasswordHasher()
res = pass_hasher.hash("MySecurePassword")

print(res)
