import customtkinter as ctk
from PIL import Image
import os
import tkinter.messagebox as messagebox

# Funções auxiliares
def carregar_usuarios():
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as f:
            return {line.split(':')[0]: line.split(':')[1].strip() for line in f.readlines()}
    return {}

def salvar_usuario(usuario, senha):
    with open("usuarios.txt", "a") as f:
        f.write(f"{usuario}:{senha}\n")

# Classe principal
class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login e Cadastro")
        self.geometry("500x500")
        self.resizable(True, True)  # Permitir maximizar/redimensionar a janela

        self.usuarios = carregar_usuarios()

        # Carregando a imagem
        self.logo_image = ctk.CTkImage(Image.open("logo aed.png"), size=(150, 150))

        # Layout inicial
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.pack(fill="both", expand=True)

        self.criar_pagina_login()


    def criar_pagina_login(self):
        # Limpa o frame principal
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        # Layout da tela de login
        ctk.CTkLabel(self.frame_principal, image=self.logo_image, text="").pack(pady=20)

        ctk.CTkLabel(self.frame_principal, text="Acesse sua Conta", font=("Arial", 20)).pack(pady=20)

        self.username_entry = ctk.CTkEntry(self.frame_principal, placeholder_text="Usuário", width=250)
        self.username_entry.pack(pady=12)

        self.password_entry = ctk.CTkEntry(self.frame_principal, placeholder_text="Senha", show="*", width=250)
        self.password_entry.pack(pady=12)

        self.login_button = ctk.CTkButton(self.frame_principal, text="Entrar", command=self.realizar_login, width=200)
        self.login_button.pack(pady=12)

        self.signup_button = ctk.CTkButton(self.frame_principal, text="Cadastrar-se", command=self.criar_pagina_cadastro, width=200)
        self.signup_button.pack(pady=12)

    def criar_pagina_cadastro(self):
        # Limpa o frame principal
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        # Layout da tela de cadastro
        ctk.CTkLabel(self.frame_principal, image=self.logo_image, text="").pack(pady=20)

        ctk.CTkLabel(self.frame_principal, text="Crie sua Conta", font=("Arial", 20)).pack(pady=20)

        self.username_entry = ctk.CTkEntry(self.frame_principal, placeholder_text="Usuário", width=250)
        self.username_entry.pack(pady=12)

        self.password_entry = ctk.CTkEntry(self.frame_principal, placeholder_text="Senha", show="*", width=250)
        self.password_entry.pack(pady=12)

        self.signup_button = ctk.CTkButton(self.frame_principal, text="Cadastrar", command=self.realizar_cadastro, width=200)
        self.signup_button.pack(pady=12)

        self.back_button = ctk.CTkButton(self.frame_principal, text="Voltar", command=self.criar_pagina_login, width=200)
        self.back_button.pack(pady=12)

    def realizar_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.usuarios and self.usuarios[username] == password:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            resposta = messagebox.askyesno(
                "Usuário não encontrado",
                "Usuário ou senha inválidos. Deseja se cadastrar?"
            )
            if resposta:  # Se o usuário clicar em 'Sim'
                self.criar_pagina_cadastro()

    def realizar_cadastro(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.usuarios:
            messagebox.showerror("Erro", "Usuário já cadastrado.")
        elif len(username) < 3 or len(password) < 3:
            messagebox.showerror("Erro", "Usuário e senha devem ter pelo menos 3 caracteres.")
        else:
            self.usuarios[username] = password
            salvar_usuario(username, password)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.criar_pagina_login()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
