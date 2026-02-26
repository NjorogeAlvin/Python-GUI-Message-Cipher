import customtkinter as ctk
from cryptography.fernet import Fernet

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

         #Fernet Key Stuff
        self.secret_key = Fernet.generate_key()
        self.f = Fernet(self.secret_key)

        #GUI Elements
        self.title("Message Cipher")
        self.geometry("600x500")
        self._set_appearance_mode("dark")
        self.entry=ctk.CTkEntry(self, placeholder_text="Input message")
        self.entry.grid(row=0, columnspan=4, padx=20, pady=20, sticky="ew")
        self.columnconfigure((0, 1),  weight=1)
        self.key=ctk.CTkEntry(self)
        self.key.grid(row=2, columnspan=4, padx=20, pady=20, sticky="ew")
        self.key.insert(0, self.secret_key)
        self.display = ctk.CTkEntry(self, placeholder_text="Decoded message")
        self.display.grid(row=4, columnspan=4, padx=20, pady=20, sticky="ew")
        
    #Buttons
        self.encrypt_button = ctk.CTkButton(self, text="Encrypt", command=self.encrypt_button)
        self.decrypt_button = ctk.CTkButton(self, text="decrypyt", command=self.decrypt_button)
        self.copy_button = ctk.CTkButton(self, text="Copy", command=self.copy_button)

    #Button Grid
        self.encrypt_button.grid(row=1 ,columnspan=4, padx=5, pady= 5)
        self.decrypt_button.grid(row=5,columnspan=4, padx=5, pady= 5)
        self.copy_button.grid(row= 3,columnspan=4, padx=5, pady= 5)
    
    #Button Functions
    def encrypt_button(self):
        message = self.entry.get()
        token = self.f.encrypt(message.encode())
        self.display.delete(0, "end")
        self.display.insert(0, token.decode())
        
    def decrypt_button(self):
        token = self.display.get()
        message = self.f.decrypt(token.encode())
        self.entry.delete(0, "end")
        self.entry.insert(0, message.decode())

    def copy_button(self):
        self.clipboard_clear()
        self.clipboard_append(self.display.get())


app = App()
app.mainloop()

