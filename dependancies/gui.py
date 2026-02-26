import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
    
        self.title("Message Cipher")
        self.geometry("600x500")
        self._set_appearance_mode("dark")



