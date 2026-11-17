from app.core.security import hash_password, verify_password

password = "secret123"

hashed_password = hash_password(password)

print("Opriginla:", password)
print("Hashed:", hashed_password)

print(
    "Correct password:",
    verify_password(password, hashed_password)
)

print(
    "Wrong password:",
    verify_password("wrong-password", hashed_password)
)