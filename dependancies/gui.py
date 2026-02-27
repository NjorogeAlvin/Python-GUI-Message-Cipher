import customtkinter as ctk
from cryptography.fernet import Fernet

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

     
        #GUI Elements
        self.title("Message Cipher")
        self.geometry("600x400")
        self._set_appearance_mode("dark")
        self.columnconfigure((0, 1, 2, 3, 4),  weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)
        self.rowconfigure((9, 10, 11), weight=3)
        

        #Labels
        self.message_label = ctk.CTkLabel(self, text="Enter your message", fg_color="navy")
        self.key_label = ctk.CTkLabel(self, text="Secret Key", fg_color="black")
        self.output_label = ctk.CTkLabel(self, text="Output", fg_color="darkblue")

        #Label Geometry
        self.message_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        self.key_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        self.output_label.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky="ew")


        #Entry Bars
        self.entry=ctk.CTkEntry(self, placeholder_text="Input message")
        self.entry.grid(row=1, column=0, columnspan=4, rowspan=3, padx=20, pady=20, sticky="nsew")
        self.key=ctk.CTkEntry(self, placeholder_text="Generate Custom Key")
        self.key.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
        self.display = ctk.CTkEntry(self, placeholder_text="Output message")
        self.display.grid(row=9, column=0,  columnspan=4, rowspan=3, padx=20, pady=20, sticky="nsew")
        
        #Buttons
        self.encrypt_button = ctk.CTkButton(self, text="Encrypt", command=self.encrypt_button)
        self.decrypt_button = ctk.CTkButton(self, text="Decrypt", command=self.decrypt_button)
        self.generate_button = ctk.CTkButton(self, text="Generate key", command=self.generate_button)

        #Button Grid
        self.encrypt_button.grid(row=4,column=0, columnspan=2, padx=5, pady= 5, sticky="ew")
        self.decrypt_button.grid(row=4,column=2, padx=5, columnspan=2, pady= 5, sticky="ew")
        self.generate_button.grid(row= 7, column=0, columnspan=4, padx=5, pady= 5, sticky="ew")
    
    #Button Functions
    def generate_button(self):
        self.key.delete(0, "end")
        self.key_1 = Fernet.generate_key()
        self.f = Fernet(self.key_1)
        self.key.insert(0, self.key_1.decode())

    def encrypt_button(self):
        message = self.entry.get()
        custom_key = self.key.get()
        f = Fernet(custom_key)
        token = f.encrypt(message.encode())
        self.display.delete(0, "end")
        self.display.insert(0, token.decode())
        
    def decrypt_button(self):
        custom_key = self.key.get()
        custom_message = self.entry.get()
        self.custom_f = Fernet(custom_key)
        custom_token = self.custom_f.decrypt(custom_message.encode())
        self.display.delete(0, "end")
        self.display.insert(0, custom_token.decode())
