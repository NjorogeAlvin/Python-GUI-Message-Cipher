from cryptography.fernet import Fernet

message = input("Enter your message: ")

key = Fernet.generate_key()

new_f = Fernet(key)

token=new_f.encrypt(message.encode())

print(token)

token_1 = new_f.decrypt(token).decode()

print(token_1)



