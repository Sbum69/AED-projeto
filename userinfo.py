from PIL import Image
import customtkinter as ctk

def user_info():
    # Janela principal
    user_page = ctk.CTk()
    user_page.title("Informações do Usuário")
    user_page.geometry("700x500")

    # Frame principal
    frame_principal = ctk.CTkFrame(master=user_page, fg_color="green")
    frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

    # Título
    titulo = ctk.CTkLabel(master=frame_principal, text="Informações do Usuário",
                          font=ctk.CTkFont(size=20, weight="bold"), text_color="white")
    titulo.pack(pady=10)

    # Frame para o formulário
    form_frame = ctk.CTkFrame(master=frame_principal, fg_color="#282828", corner_radius=15)
    form_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Dados fictícios do usuário (você pode integrar com um banco de dados depois)
    user_data = {
        "Nome": "Sheldon Jasse",
        "Data de Criação": "2025-01-11",
        "Tipo de Usuário": "Admin",
        "Email": "sheldon.jasse@example.com",
        "Data de Nascimento": "2000-06-15",
        "Telefone": "+244 912 345 678"
    }

    # Função para salvar as alterações
    def salvar_alteracoes():
        for campo, widget in campos.items():
            if campo == "Tipo de Usuário":
                user_data[campo] = tipo_usuario_dropdown.get()  # Obtém a opção selecionada
            else:
                user_data[campo] = widget.get()  # Obtém o valor do campo de texto
        print("Dados salvos:", user_data)  # Aqui você pode substituir pela lógica de salvamento real
        ctk.CTkMessagebox.show_info(title="Sucesso", message="Informações atualizadas com sucesso!")

    # Exibição e edição dos dados do usuário
    campos = {}
    for idx, (campo, valor) in enumerate(user_data.items()):
        label = ctk.CTkLabel(master=form_frame, text=campo + ":", text_color="white", font=ctk.CTkFont(size=14))
        label.grid(row=idx, column=0, padx=10, pady=10, sticky="e")

        if campo == "Tipo de Usuário":
            # Dropdown para selecionar o tipo de usuário
            tipo_usuario_dropdown = ctk.CTkOptionMenu(
                master=form_frame,
                values=["Admin", "User"],
                fg_color="#404040",
                text_color="white",
                corner_radius=10
            )
            tipo_usuario_dropdown.set(valor)  # Define o valor atual
            tipo_usuario_dropdown.grid(row=idx, column=1, padx=10, pady=10, sticky="w")
            campos[campo] = tipo_usuario_dropdown
        else:
            # Campo de texto para edição
            entry = ctk.CTkEntry(
                master=form_frame,
                width=300,
                fg_color="#404040",
                text_color="white",
                corner_radius=10
            )
            entry.insert(0, valor)  # Define o valor atual
            entry.grid(row=idx, column=1, padx=10, pady=10, sticky="w")
            campos[campo] = entry

    # Botão para salvar alterações
    salvar_btn = ctk.CTkButton(
        master=frame_principal,
        text="Salvar Alterações",
        fg_color="#1DB954",
        text_color="white",
        corner_radius=10,
        command=salvar_alteracoes
    )
    salvar_btn.pack(pady=10)

    # Função de logout
    def logout():
        user_page.destroy()  # Fecha a janela atual
        print("Usuário desconectado.")  # Aqui você pode adicionar a lógica para retornar à tela de login

    # Botão de logout
    logout_btn = ctk.CTkButton(
        master=frame_principal,
        text="Logout",
        fg_color="#E74C3C",
        text_color="white",
        corner_radius=10,
        command=logout
    )
    logout_btn.pack(pady=10)

    user_page.mainloop()

# Chamar a função para testar
user_info()
