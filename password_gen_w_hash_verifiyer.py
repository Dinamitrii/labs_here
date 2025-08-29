from argon2 import PasswordHasher

ph = PasswordHasher()
res = ph.hash("MySecurePassword")


try:
    ph.verify(res, "MySecurePassword")
    print("Password match!")

except Exception:
    print("Incorrect password.")