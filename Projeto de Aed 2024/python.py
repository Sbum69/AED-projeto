import tkinter as tk
from tkinter import messagebox, simpledialog
import webbrowser
import json
import os

# Caminho para o banco de dados JSON
DB_FILE = "musicas_podcasts.json"

# Inicializar o banco de dados se não existir
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"musicas": []}, f)

# Funções relacionadas ao banco de dados
class DatabaseManager:
    @staticmethod
    def carregar_dados():
        with open(DB_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def salvar_dados(dados):
        with open(DB_FILE, "w") as f:
            json.dump(dados, f, indent=4)

    @staticmethod
    def adicionar_musica(nome, categoria, link):
        dados = DatabaseManager.carregar_dados()
        dados["musicas"].append({"nome": nome, "categoria": categoria, "link": link})
        DatabaseManager.salvar_dados(dados)

    @staticmethod
    def buscar_por_categoria(categoria):
        dados = DatabaseManager.carregar_dados()
        return [m for m in dados["musicas"] if m["categoria"].lower() == categoria.lower()]

    @staticmethod
    def listar_todas():
        return DatabaseManager.carregar_dados()["musicas"]

# Funções principais (links do YouTube, favoritos, etc.)
class Funcionalidades:
    @staticmethod
    def abrir_link(link):
        webbrowser.open(link)

    @staticmethod
    def adicionar_favorito(nome, link):
        messagebox.showinfo("Favoritos", f"'{nome}' foi adicionado aos favoritos!")

# Interface gráfica (Tkinter)
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Músicas e Podcasts")
        self.geometry("800x600")
        self.config(bg="white")
        self.criar_widgets()

    def criar_widgets(self):
        # Barra de busca
        tk.Label(self, text="Pesquisar:", bg="white").pack(pady=5)
        self.entrada_busca = tk.Entry(self, width=40)
        self.entrada_busca.pack(pady=5)
        tk.Button(self, text="Buscar", command=self.buscar_categoria).pack(pady=5)

        # Área principal (lista de músicas)
        self.lista_musicas = tk.Listbox(self, width=100, height=20)
        self.lista_musicas.pack(pady=10)

        # Botões de interação
        tk.Button(self, text="Abrir Link", command=self.abrir_link_selecionado).pack(pady=5)
        tk.Button(self, text="Adicionar Nova Música", command=self.adicionar_musica).pack(pady=5)

        # Botão para exibir todos
        tk.Button(self, text="Exibir Todas as Músicas", command=self.listar_todas_musicas).pack(pady=5)

    # Funções para interação com a interface
    def buscar_categoria(self):
        categoria = self.entrada_busca.get()
        if not categoria:
            messagebox.showwarning("Atenção", "Digite uma categoria para buscar!")
            return

        musicas = DatabaseManager.buscar_por_categoria(categoria)
        self.lista_musicas.delete(0, tk.END)
        if musicas:
            for musica in musicas:
                self.lista_musicas.insert(tk.END, f"{musica['nome']} - {musica['link']}")
        else:
            messagebox.showinfo("Busca", "Nenhuma música encontrada nessa categoria!")

    def listar_todas_musicas(self):
        musicas = DatabaseManager.listar_todas()
        self.lista_musicas.delete(0, tk.END)
        for musica in musicas:
            self.lista_musicas.insert(tk.END, f"{musica['nome']} - {musica['link']}")

    def abrir_link_selecionado(self):
        selecionado = self.lista_musicas.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma música para abrir!")
            return

        musica = self.lista_musicas.get(selecionado[0])
        link = musica.split(" - ")[-1]
        Funcionalidades.abrir_link(link)

    def adicionar_musica(self):
        nome = simpledialog.askstring("Nova Música", "Digite o nome da música:")
        categoria = simpledialog.askstring("Nova Música", "Digite a categoria da música:")
        link = simpledialog.askstring("Nova Música", "Cole o link do YouTube:")
        
        if nome and categoria and link:
            DatabaseManager.adicionar_musica(nome, categoria, link)
            messagebox.showinfo("Sucesso", f"Música '{nome}' adicionada com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

# Inicializar a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
