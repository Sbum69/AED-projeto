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
    admin_app.resizable(True, True)

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
    tab_gerir_podcast = admin_tab.add("Gerir Podcasts")
    tab_gerir_trendings = admin_tab.add("Gerir Tendencias")
    tab_gerir_humor = admin_tab.add("Gerir Humor")
    tab_gerir_desenvolvimento = admin_tab.add("Gerir Desenvolvimento")
    tab_gerir_estrelas = admin_tab.add("Gerir Estrelas")
    tab_gerir_entretenimento = admin_tab.add("Gerir Entretenimento")

    # Botões no menu lateral
    ctk.CTkButton(menu_lateral, text="Lista de Podcasts", command=lambda: admin_tab.set("Listar Podcasts")).pack(
        pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral, text="Lista de Users", command=lambda: admin_tab.set("Lista de utilizadores")).pack(
        pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral, text="Gerir Users", command=lambda: admin_tab.set("Gerir Users")).pack(
        pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral,text="Gerir Podcasts",command=lambda:admin_tab.set("Gerir Podcasts")).pack(
        pady=20,padx=10,anchor = "w")
    ctk.CTkButton(menu_lateral,text="Gerir Trendings",command=lambda:admin_tab.set("Gerir Tendencias")).pack(
        pady=20,padx=10,anchor = "w")
    ctk.CTkButton(menu_lateral,text="Gerir Categoria Humor",command=lambda:admin_tab.set("Gerir Humor")).pack(
        pady=20,padx=10,anchor="w")
    ctk.CTkButton(menu_lateral,text="Gerir Desenvolvimento",command=lambda:admin_tab.set("Gerir Desenvolvimento")).pack(
        pady=20,padx=10, anchor = "w")
    ctk.CTkButton(menu_lateral,text="Gerir Estrelas",command=lambda:admin_tab.set("Gerir Estrelas")).pack(
        pady=20,padx=10, anchor = "w")
    ctk.CTkButton(menu_lateral,text="Gerir Entertenimento",command=lambda:admin_tab.set("Gerir Entertenimento")).pack(
         pady=20,padx=10, anchor = "w")
       
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
    
    #=============================
    # Tab para gestão de podcasts
    #=============================
    
    def carregar_podcasts():
        podcast = []
        try:
            with open("podcasts.txt","r") as ficheiro:
                return ficheiro.readlines()
        except FileNotFoundError:
            messagebox.showerror("Erro","O arquivo podcasts.txt não existe")
            return []
        

    def salvar_podcasts():
        conteudo = txtbox_gerir_podcasts.get("1.0","end").strip()
        linhas = conteudo.split("\n")
        try:
            with open("podcasts.txt","w") as ficheiro:
              for linha in linhas:
                  ficheiro.write(f"{linha}\n")
            messagebox.showinfo("Sucesso","Alterações salvas com sucesso!")
        except FileNotFoundError:
            messagebox.showerror("Erro","O arquivo podcasts.txt não existe")
    
    txtbox_gerir_podcasts = ctk.CTkTextbox(tab_gerir_podcast,fg_color="black",text_color="white",font=("Helvetica",14))
    txtbox_gerir_podcasts.pack(fill="both",expand=True,padx=10)

    def exibir_podcasts():
        linhas = carregar_podcasts()
        if linhas:
            txtbox_gerir_podcasts.delete("1.0","end")
            for linha in linhas:
                partes = linha.strip().split(",")
                if len(partes) == 3:
                    nome = partes[0]
                    imagem = partes[1]
                    link = partes[2]
                    txtbox_gerir_podcasts.insert("1.0",f"Nome:{nome}\nImagem: {imagem}\nlink: {link}\n\n")
        else:
            txtbox_gerir_podcasts.insert("1.0","Nenhum podcast encontrado.")
    exibir_podcasts()

       

    btn_salvar_podcasts = ctk.CTkButton(tab_gerir_podcast,text="Guardar alterações",command=salvar_podcasts,fg_color="teal")
    btn_salvar_podcasts.pack(pady=10)
    
    #=================================
    # Tab para a gestão das tendencias
    #=================================

    def carregar_tendencias():
        trendings = []
        try:
            with open("trending.txt","r") as ficheiro_trending:
                return ficheiro_trending.readlines()
        except FileNotFoundError:
            messagebox.showerror("Erro","O trending.txt não existe")
            return []
    
    def salvar_tendencias():
        conteudo = txtbox_gerir_podcasts.get("1.0","end").strip()
        linhas = conteudo.split("\n")
        try:
            with open("trending.txt","w") as ficheiro_trending:
              for linha in linhas:
                  ficheiro_trending.write(f"{linha}\n")
            messagebox.showinfo("Sucesso","Alterações salvas com sucesso!")
        except FileNotFoundError:
            messagebox.showerror("Erro","O arquivo trending.txt não existe")

    txtbox_gerir_tendencias = ctk.CTkTextbox(tab_gerir_trendings,fg_color="black",text_color="white",font=("Helvetica",14))
    txtbox_gerir_tendencias.pack(fill="both",expand=True,padx=10)

    def exibir_tendencias():
        linhas = carregar_tendencias()
        if linhas:
            txtbox_gerir_tendencias.delete("1.0","end")
            for linha in linhas:
                partes = linha.strip().split(",")
                if len(partes) == 3:
                    nome = partes[0]
                    imagem = partes[1]
                    link = partes[2]
                    txtbox_gerir_tendencias.insert("1.0",f"Nome:{nome}\nImagem: {imagem}\nlink: {link}\n\n")
        else:
            txtbox_gerir_tendencias.insert("1.0","Nenhum podcast encontrado.")
    exibir_tendencias()

    btn_salvar_tendencias = ctk.CTkButton(tab_gerir_trendings,text="Guardar alterações",command=salvar_tendencias,fg_color="teal")
    btn_salvar_tendencias.pack(pady=10)

    #==================
    # Tab para gestão da categoria de humor
    #==================

    def carregar_humor():
        humor = []
        try:
            with open("humor.txt","r") as ficheiro_humor:
                return ficheiro_humor.readlines()
        except FileNotFoundError:
            messagebox.showerror("Erro","O humor.txt não existe")
            return []
        
    def salvar_humor():
        conteudo = txtbox_gerir_podcasts.get("1.0","end").strip()
        linhas = conteudo.split("\n")
        try:
            with open("humor.txt","w") as ficheiro_humor:
              for linha in linhas:
                  ficheiro_humor.write(f"{linha}\n")
            messagebox.showinfo("Sucesso","Alterações salvas com sucesso!")
        except FileNotFoundError:
            messagebox.showerror("Erro","O arquivo humor.txt não existe")

    txtbox_gerir_humor = ctk.CTkTextbox(tab_gerir_humor,fg_color="black",text_color="white",font=("Helvetica",14))
    txtbox_gerir_humor.pack(fill="both",expand=True,padx=10)

    def exibir_humor():
        linhas = carregar_humor()
        if linhas:
            txtbox_gerir_humor.delete("1.0","end")
            for linha in linhas:
                partes = linha.strip().split(",")
                if len(partes) == 3:
                    nome = partes[0]
                    imagem = partes[1]
                    link = partes[2]
                    txtbox_gerir_humor.insert("1.0",f"Nome:{nome}\nImagem: {imagem}\nlink: {link}\n\n")
        else:
            txtbox_gerir_humor.insert("1.0","Nenhum podcast encontrado.")
    exibir_humor()

    btn_salvar_humor = ctk.CTkButton(tab_gerir_humor,text="Guardar alterações",command=salvar_tendencias,fg_color="teal")
    btn_salvar_humor.pack(pady=10)


    #==================
    # Tab gestão de categoria de desenvolvimento
    #==================

    def carregar_desenvolvemento():
        desenvolvimento = []
        try:
            with open("desenvolvimento.txt","r") as ficheiro_desenvolvimento:
                return ficheiro_desenvolvimento.readlines()
        except FileNotFoundError:
            messagebox.showerror("Erro","O desenvolvimento.txt não existe")
            return []
    
    def salvar_desenvolvimento():
        conteudo = txtbox_gerir_desenvolvimento.get("1.0","end").strip()
        linhas = conteudo.split("\n")
        try:
            with open("desenvolvimento.txt","w") as ficheiro_desenvolvimento:
              for linha in linhas:
                  ficheiro_desenvolvimento.write(f"{linha}\n")
            messagebox.showinfo("Sucesso","Alterações salvas com sucesso!")
        except FileNotFoundError:
            messagebox.showerror("Erro","O arquivo desenvolvimento.txt não existe")
    
    txtbox_gerir_desenvolvimento = ctk.CTkTextbox(tab_gerir_desenvolvimento,fg_color="black",text_color="white",font=("Helvetica",14))
    txtbox_gerir_desenvolvimento.pack(fill="both",expand=True,padx=10)

    def exibir_desenvolvimento():
        linhas = carregar_desenvolvemento()
        if linhas:
            txtbox_gerir_desenvolvimento.delete("1.0","end")
            for linha in linhas:
                partes = linha.strip().split(",")
                if len(partes) == 3:
                    nome = partes[0]
                    imagem = partes[1]
                    link = partes[2]
                    txtbox_gerir_desenvolvimento.insert("1.0",f"Nome:{nome}\nImagem: {imagem}\nlink: {link}\n\n")
        else:
            txtbox_gerir_desenvolvimento.insert("1.0","Nenhum podcast encontrado.")
    exibir_desenvolvimento()

    btn_salvar_desenvolvimento = ctk.CTkButton(tab_gerir_desenvolvimento,text="Guardar alterações",command=salvar_desenvolvimento,fg_color="teal")
    btn_salvar_desenvolvimento.pack(pady=10)

    #=======================
    #Tab para Gerir estrelas
    #=======================

    def carregar_estrelas():
        estrelas = []
        try:
            with open("estrelas.txt","r") as ficheiro_estrelas:
                return ficheiro_estrelas.readlines()
        except FileNotFoundError:
            messagebox.showerror("Erro","O estrelas.txt não existe")
            return []
        
    def salvar_estrelas():
        conteudo = txtbox_gerir_estrelas.get("1.0","end").strip()
        linhas = conteudo.split("\n")
        try:
            with open("estrelas.txt","w") as ficheiro_desenvolvimento:
              for linha in linhas:
                  ficheiro_desenvolvimento.write(f"{linha}\n")
            messagebox.showinfo("Sucesso","Alterações salvas com sucesso!")
        except FileNotFoundError:
            messagebox.showerror("Erro","O arquivo estralas.txt não existe")
    
    txtbox_gerir_estrelas = ctk.CTkTextbox(tab_gerir_estrelas,fg_color="black",text_color="white",font=("Helvetica",14))
    txtbox_gerir_estrelas.pack(fill="both",expand=True,padx=10)

    def exibir_estrelas():
        linhas = carregar_estrelas()
        if linhas:
            txtbox_gerir_estrelas.delete("1.0","end")
            for linha in linhas:
                partes = linha.strip().split(",")
                if len(partes) == 3:
                    nome = partes[0]
                    imagem = partes[1]
                    link = partes[2]
                    txtbox_gerir_estrelas.insert("1.0",f"Nome:{nome}\nImagem: {imagem}\nlink: {link}\n\n")
        else:
            txtbox_gerir_estrelas.insert("1.0","Nenhum podcast encontrado.")
    exibir_estrelas()

    btn_salvar_estrelas = ctk.CTkButton(tab_gerir_estrelas,text="Guardar alterações",command=salvar_estrelas,fg_color="teal")
    btn_salvar_estrelas.pack(pady=10)

        
    #==================
    # Tab para gerir a categoria de entertenimento
    #==================

    def carregar_entertenimento():
        entertenimento = []
        try:
            with open("entertenimento.txt","r") as ficheiro_entertenimento:
                return ficheiro_entertenimento.readlines()
        except FileNotFoundError:
            messagebox.showerror("Erro","O ficheiro entertenimento.txt não existe")
            return []
    
    def salvar_entertenimento():
        conteudo = txtbox_gerir_entertenimento.get("1.0","end").strip()
        linhas = conteudo.split("\n")
        try:
            with open("entertenimento.txt","w") as ficheiro_entertenimento:
              for linha in linhas:
                  ficheiro_entertenimento.write(f"{linha}\n")
            messagebox.showinfo("Sucesso","Alterações salvas com sucesso!")
        except FileNotFoundError:
            messagebox.showerror("Erro","O arquivo estralas.txt não existe")
    
    txtbox_gerir_entertenimento = ctk.CTkTextbox(tab_gerir_entretenimento,fg_color="black",text_color="white",font=("Helvetica",14))
    txtbox_gerir_entertenimento.pack(fill="both",expand=True,padx=10)

    def exibir_entertenimento():
        linhas = carregar_entertenimento()
        if linhas:
            txtbox_gerir_entertenimento.delete("1.0","end")
            for linha in linhas:
                partes = linha.strip().split(",")
                if len(partes) == 3:
                    nome = partes[0]
                    imagem = partes[1]
                    link = partes[2]
                    txtbox_gerir_entertenimento.insert("1.0",f"Nome:{nome}\nImagem: {imagem}\nlink: {link}\n\n")
        else:
            txtbox_gerir_entertenimento.insert("1.0","Nenhum podcast encontrado.")
    exibir_entertenimento()

    btn_salvar_entertenimento = ctk.CTkButton(tab_gerir_entretenimento,text="Guardar alterações",command=salvar_entertenimento,fg_color="teal")
    btn_salvar_entertenimento.pack(pady=10)


    admin_app.mainloop()



admin_dashboard()





