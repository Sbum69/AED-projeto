import customtkinter as ctk
import os
from tkinter import messagebox
from PIL import Image


# Função para carregar dados dos podcasts
def carregar_dados_podcasts(ficheiro_podcast):
    podcasts = []
    try:
        with open("podcasts.txt", "r") as ficheiro:
            for line in ficheiro:
                partes = line.strip().split(",")
                if len(partes) == 3:
                    podcasts.append({"name": partes[0], "image": partes[1], "link": partes[2]})
    except FileNotFoundError:
        print(f"Arquivo {ficheiro_podcast} não encontrado!")
    return podcasts


# Função para carregar dados de usuários
def carregar_dados_user(ficheiro_user):
    users = []
    try:
        with open("usuarios.txt", "r") as arquivo:
            for line in arquivo:
                partes = line.strip().split(",")
                if len(partes) == 3:
                    users.append({"nome": partes[0], "email": partes[1], "password": partes[2]})
    except FileNotFoundError:
        print(f"Arquivo {ficheiro_user} não encontrado!")
    return users


# Função para salvar dados de usuários
def salvar_dados_user(ficheiro_user, lista_users):
    try:
        with open("usuarios.txt", "w") as arquivo:
            for user in lista_users:
                linha = f"{user['nome']},{user['email']},{user['password']}\n"
                arquivo.write(linha)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao salvar os usuários: {str(e)}")


# Função principal para o dashboard do admin
def admin_dashboard():
    global user, entry_nome, entry_email, entry_senha, txtbox_user

    user = carregar_dados_user("usuarios.txt")
    podcasts = carregar_dados_podcasts("podcasts.txt")

    admin_app = ctk.CTk()
    admin_app.title("PodSpot")
    admin_app.geometry("1024x900")
    admin_app.resizable(False, False)

    # Frame principal do dashboard do admin
    frame_principal = ctk.CTkFrame(admin_app, fg_color="green")
    frame_principal.pack(fill="both", expand=True)

    # Menu lateral de navegação
    menu_lateral = ctk.CTkFrame(master=frame_principal, width=200, fg_color="#1DB954")
    menu_lateral.pack(side="left", fill="y")

    # Tabviews para funcionalidades do Admin
    admin_tab = ctk.CTkTabview(frame_principal, corner_radius=10, fg_color="green")
    admin_tab.pack(fill="both", expand=True, padx=10, pady=10)

    # Abas para funcionalidades
    tab_podcasts = admin_tab.add("Listar Podcasts")
    tab_listar_user = admin_tab.add("Lista de utilizadores")
    tab_gerir_user = admin_tab.add("Gerir Users")

    # Botões no menu lateral
    ctk.CTkButton(menu_lateral, text="Lista de Podcasts", command=lambda: admin_tab.set("Listar Podcasts")).pack(
        pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral, text="Lista de Users", command=lambda: admin_tab.set("Lista de utilizadores")).pack(
        pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral, text="Gerir Users", command=lambda: admin_tab.set("Gerir Users")).pack(
        pady=20, padx=10, anchor="w")

    # ==================
    # Tab de Podcasts
    # ==================
    scroll_frame = ctk.CTkScrollableFrame(tab_podcasts, fg_color="black")
    scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

    for idx, podcast in enumerate(podcasts):
        frame_podcast = ctk.CTkFrame(master=scroll_frame, fg_color="green")
        frame_podcast.grid(row=idx // 4, column=idx % 4, padx=10, pady=10)

        try:
            podcast_image = ctk.CTkImage(dark_image=Image.open(podcast["image"]), size=(150, 150))
        except FileNotFoundError:
            podcast_image = None

        ctk.CTkButton(
            master=frame_podcast,
            image=podcast_image,
            text=podcast["name"],
            compound="top",
            command=lambda link=podcast["link"]: os.system(f"start {link}")
        ).pack(pady=(0, 5))

    # ==================
    # Tab de Listar Users
    # ==================
    def atualizar_lista_users():
        txtbox_user.delete("1.0", "end")
        if user:
            for u in user:
                txtbox_user.insert("end", f"Nome: {u['nome']} | Email: {u['email']} | Password: {u['password']}\n")
        else:
            txtbox_user.insert("1.0", "Nenhum usuário encontrado.")

    txtbox_user = ctk.CTkTextbox(tab_listar_user, fg_color="black", text_color="white")
    txtbox_user.pack(fill="both", expand=True, padx=10)

    atualizar_lista_users()

    # ============================
    # Tab para Gerir Users
    # ============================
    def adicionar_user():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()

        if nome and email and senha:
            novo_user = {"nome": nome, "email": email, "password": senha}
            user.append(novo_user)
            salvar_dados_user("usuarios.txt", user)
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
            atualizar_lista_users()
            entry_nome.delete(0, "end")
            entry_email.delete(0, "end")
            entry_senha.delete(0, "end")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def remover_user():
        email = entry_email.get()
        if email:
            user_encontrado = next((u for u in user if u["email"] == email), None)
            if user_encontrado:
                user.remove(user_encontrado)
                salvar_dados_user("usuarios.txt", user)
                messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")
                atualizar_lista_users()
            else:
                messagebox.showerror("Erro", "Usuário não encontrado!")
        else:
            messagebox.showerror("Erro", "Por favor, insira o email do usuário para remover!")

    frame_form = ctk.CTkFrame(tab_gerir_user)
    frame_form.pack(pady=20)

    ctk.CTkLabel(frame_form, text="Nome:").grid(row=0, column=0, pady=5, padx=5)
    entry_nome = ctk.CTkEntry(frame_form)
    entry_nome.grid(row=0, column=1, pady=5, padx=5)

    ctk.CTkLabel(frame_form, text="Email:").grid(row=1, column=0, pady=5, padx=5)
    entry_email = ctk.CTkEntry(frame_form)
    entry_email.grid(row=1, column=1, pady=5, padx=5)

    ctk.CTkLabel(frame_form, text="Senha:").grid(row=2, column=0, pady=5, padx=5)
    entry_senha = ctk.CTkEntry(frame_form, show="*")
    entry_senha.grid(row=2, column=1, pady=5, padx=5)

    ctk.CTkButton(frame_form, text="Adicionar Usuário", command=adicionar_user, fg_color="#1DB954").grid(
        row=3, column=0, columnspan=2, pady=10)

    ctk.CTkButton(frame_form, text="Remover Usuário", command=remover_user, fg_color="red").grid(
        row=4, column=0, columnspan=2, pady=10)

    admin_app.mainloop()


# Executar o dashboard do admin
admin_dashboard()





