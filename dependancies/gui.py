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
        self.geometry("600x400")
        self._set_appearance_mode("dark")
        

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
        self.columnconfigure((0, 1, 2, 3, 4),  weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)
        self.rowconfigure((9, 10, 11), weight=3)
        self.key=ctk.CTkEntry(self)
        self.key.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
        self.key.insert(0, self.secret_key)
        self.display = ctk.CTkEntry(self, placeholder_text="Output message")
        self.display.grid(row=9, column=0,  columnspan=4, rowspan=3, padx=20, pady=20, sticky="nsew")
        
        #Buttons
        self.encrypt_button = ctk.CTkButton(self, text="Encrypt", command=self.encrypt_button)
        self.decrypt_button = ctk.CTkButton(self, text="Decrypyt", command=self.decrypt_button)
        self.copy_button = ctk.CTkButton(self, text="Copy", command=self.copy_button)

        #Button Grid
        self.encrypt_button.grid(row=4,column=0, columnspan=2, padx=5, pady= 5, sticky="ew")
        self.decrypt_button.grid(row=4,column=2, padx=5, columnspan=2, pady= 5, sticky="ew")
        self.copy_button.grid(row= 7, column=0, columnspan=4, padx=5, pady= 5, sticky="ew")
    
    #Button Functions
    def encrypt_button(self):
        message = self.entry.get()
        token = self.f.encrypt(message.encode())
        self.display.delete(0, "end")
        self.display.insert(0, token.decode())
        
    def decrypt_button(self):
        token = self.display.get()
        message = self.f.decrypt(token.encode())
        self.display.delete(0, "end")
        self.display.insert(0, message.decode())

    def copy_button(self):
        self.clipboard_clear()
        self.clipboard_append(self.display.get())


app = App()
app.mainloop()

