import customtkinter as ctk
from PIL import Image
import sqlite3
from tkinter import messagebox
import webbrowser

# Configuração inicial
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("430x700")
app.title("PodSpot")

# Configuração do banco de dados
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

# Função para criar a tela de Sign Up
def criar_frame_signup():
    for widget in app.winfo_children():
        widget.destroy()

    frame_signup = ctk.CTkFrame(master=app, width=430, height=700, fg_color="#191414", corner_radius=40)
    frame_signup.pack(padx=10, pady=10, fill="both", expand=True)

    # Logotipo
    logo_image = ctk.CTkImage(dark_image=Image.open("logo aed.png"), size=(100, 100))
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

    def cadastrar_usuario():
        user = username.get()
        mail = email.get()
        passwd = password.get()
        confirm_passwd = confirm_password.get()

        if not user or not mail or not passwd or not confirm_passwd:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        if passwd != confirm_passwd:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return

        cursor.execute("INSERT INTO usuarios (username, email, password) VALUES (?, ?, ?)", (user, mail, passwd))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        criar_frame_login()

    btn_signup = ctk.CTkButton(frame_signup, text="Cadastrar", command=cadastrar_usuario,
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
    logo_image = ctk.CTkImage(dark_image=Image.open("logo aed.png"), size=(100, 100))
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

    def login_usuario():
        user = username.get()
        passwd = password.get()

        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (user, passwd))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {user}!")
            # Aqui você pode redirecionar para a página inicial do PodSpot
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    btn_login = ctk.CTkButton(frame_login, text="Login", command=login_usuario,
                              width=300, corner_radius=30, fg_color="#1DB954", text_color="white")
    btn_login.place(relx=0.5, y=330, anchor="center")

    btn_guest = ctk.CTkButton(frame_login, text="Entrar como Convidado", command=entrar_como_convidado,
                              width=300, corner_radius=30, fg_color="gray", text_color="white")
    btn_guest.place(relx=0.5, y=380, anchor="center")

    btn_signup_redirect = ctk.CTkButton(frame_login, text="Não tem conta? Sign Up", command=criar_frame_signup,
                                        width=300, corner_radius=30, fg_color="transparent", text_color="white")
    btn_signup_redirect.place(relx=0.5, y=430, anchor="center")

# Função para entrar como convidado
def entrar_como_convidado():
    messagebox.showinfo("Convidado", "Você está entrando como convidado. Algumas funcionalidades podem estar limitadas.")
    # Aqui você pode redirecionar para a página inicial do PodSpot

# Inicializa a tela de login ao abrir o app
criar_frame_login()
app.mainloop()
