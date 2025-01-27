import customtkinter as ctk
from PIL import Image
import os
from tkinter import messagebox
import webbrowser
from datetime import datetime
from github import pagina_inicial


# Configuração inicial
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("430x700")
app.title("PodSpot")

# Função para salvar os dados de login no arquivo txt
def salvar_dados_login(admin):
    admin_sistema = os.getlogin()
    with open("admin_login.txt", "a") as arquivo:
        arquivo.write(f"Usuário logado: {admin}, Usuário do sistema: {admin_sistema}\n")

# Função para criar a tela de Sign Up
def criar_frame_signup():
    for widget in app.winfo_children():
        widget.destroy()

    frame_signup = ctk.CTkFrame(master=app, width=430, height=700, fg_color="#191414", corner_radius=40)
    frame_signup.pack(padx=10, pady=10, fill="both", expand=True)

    # Logotipo
    logo_image = ctk.CTkImage(dark_image=Image.open("Logo.png"), size=(100, 100))
    logo_label = ctk.CTkLabel(frame_signup, image=logo_image, text="")
    logo_label.place(relx=0.5, y=50, anchor="center")

    label_titulo = ctk.CTkLabel(frame_signup, text="Sign Up", font=("Helvetica bold", 24), text_color="white")
    label_titulo.place(relx=0.5, y=150, anchor="center")

    username = ctk.CTkEntry(frame_signup, placeholder_text="Username...", width=300, corner_radius=30,
                            fg_color="transparent", text_color="white")
    username.place(relx=0.5, y=220, anchor="center")

    email = ctk.CTkEntry(frame_signup, placeholder_text="Email...", width=300, corner_radius=30,
                         fg_color="transparent", text_color="white")
    email.place(relx=0.5, y=270, anchor="center")

    password = ctk.CTkEntry(frame_signup, placeholder_text="Password...", show="*", width=300, corner_radius=30,
                            fg_color="transparent", text_color="white")
    password.place(relx=0.5, y=320, anchor="center")

    confirm_password = ctk.CTkEntry(frame_signup, placeholder_text="Confirm Password...", show="*",
                                    width=300, corner_radius=30, fg_color="transparent", text_color="white")
    confirm_password.place(relx=0.5, y=370, anchor="center")

    def cadastrar_admin():
        admin = username.get()
        mail = email.get()
        passwd = password.get()
        confirm_passwd = confirm_password.get()

        if not admin or not mail or not passwd or not confirm_passwd:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        if passwd != confirm_passwd:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return

        # Registro do usuário (simulação de banco de dados)
        with open("admin.txt", "a") as arquivo:
            arquivo.write(f"{admin},{mail},{passwd},{datetime.now().date()},,,\n")
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        criar_frame_login()

    btn_signup = ctk.CTkButton(frame_signup, text="Cadastrar", command=cadastrar_admin,
                               width=300, corner_radius=30, fg_color="#1DB954", text_color="white")
    btn_signup.place(relx=0.5, y=430, anchor="center")

    btn_login_redirect = ctk.CTkButton(frame_signup, text="Já tem conta? Login", command=criar_frame_login,
                                       width=300, corner_radius=30, fg_color="transparent", text_color="white")
    btn_login_redirect.place(relx=0.5, y=480, anchor="center")

# Função para criar a tela de Login
def criar_frame_login():
    for widget in app.winfo_children():
        widget.destroy()

    frame_login = ctk.CTkFrame(master=app, width=430, height=700, fg_color="#191414", corner_radius=40)
    frame_login.pack(padx=10, pady=10, fill="both", expand=True)

    # Logotipo
    logo_image = ctk.CTkImage(dark_image=Image.open("Logo.png"), size=(100, 100))
    logo_label = ctk.CTkLabel(frame_login, image=logo_image, text="")
    logo_label.place(relx=0.5, y=50, anchor="center")

    label_titulo = ctk.CTkLabel(frame_login, text="Login", font=("Helvetica bold", 24), text_color="white")
    label_titulo.place(relx=0.5, y=150, anchor="center")

    username = ctk.CTkEntry(frame_login, placeholder_text="Username...", width=300, corner_radius=30,
                            fg_color="transparent", text_color="white")
    username.place(relx=0.5, y=220, anchor="center")

    password = ctk.CTkEntry(frame_login, placeholder_text="Password...", show="*", width=300, corner_radius=30,
                            fg_color="transparent", text_color="white")
    password.place(relx=0.5, y=270, anchor="center")

    def login_admin():
        user = username.get()
        passwd = password.get()

        # Validação do login (simulação de banco de dados)
        try:
            with open("admin.txt", "r") as arquivo:
                admin = arquivo.readlines()
            for linha in admin:
                dados = linha.strip().split(",")
                if dados[0] == user and dados[2] == passwd:
                    salvar_dados_login(user)
                    messagebox.showinfo("Sucesso", f"Bem-vindo, {user}!")
                    app.destroy()
                    pagina_inicial(dados)
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Nenhum usuário cadastrado!")

    btn_login = ctk.CTkButton(frame_login, text="Login", command=login_admin,
                              width=300, corner_radius=30, fg_color="#1DB954", text_color="white")
    btn_login.place(relx=0.5, y=330, anchor="center")

 

    btn_signup_redirect = ctk.CTkButton(frame_login, text="Não tem conta? Sign Up", command=criar_frame_signup,
                                        width=300, corner_radius=30, fg_color="transparent", text_color="white")
    btn_signup_redirect.place(relx=0.5, y=430, anchor="center")


    def user_info(username):

        frame_principal = ctk.CTkFrame(master=user_page, fg_color="green")
        frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = ctk.CTkLabel(master=frame_principal, text=f"Informações do Usuário - {username}",
                          font=ctk.CTkFont(size=20, weight="bold"), text_color="white")
    titulo.pack(pady=10)

    form_frame = ctk.CTkFrame(master=frame_principal, fg_color="#282828", corner_radius=15)
    form_frame.pack(fill="both", expand=True, padx=10, pady=10)

    user_data = {}
    try:
        with open("userinfo.txt", "r") as userinfo_file:
            for linha in userinfo_file:
                if linha.startswith(username):
                    campos = linha.strip().split(",")
                    user_data = {
                        "Username": campos[0],
                        "Senha": campos[1],
                        "Data de Criação": campos[2].split(": ")[1]
                    }
                    break
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de informações do usuário não encontrado!")
        return

    campos_widgets = {}
    for idx, (campo, valor) in enumerate(user_data.items()):
        label = ctk.CTkLabel(master=form_frame, text=f"{campo}:", text_color="white", font=ctk.CTkFont(size=14))
        label.grid(row=idx, column=0, padx=10, pady=10, sticky="e")

        entry = ctk.CTkEntry(master=form_frame, width=300, fg_color="#404040", text_color="white", corner_radius=10)
        entry.insert(0, valor)
        entry.grid(row=idx, column=1, padx=10, pady=10, sticky="w")
        campos_widgets[campo] = entry

# Inicializa a tela de login ao abrir o app
criar_frame_login()
app.mainloop()
