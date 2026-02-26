from cryptography.fernet import Fernet

message = input("Enter your message: ")

key = Fernet.generate_key()

f = Fernet(key)

token=f.encrypt(message.encode())

print(token)

token_1 = f.decrypt(token).decode()

print(token_1)



