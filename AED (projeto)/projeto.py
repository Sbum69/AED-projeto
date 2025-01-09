import customtkinter as ctk
import feedparser
import vlc
import os
import wget
import tkinter.messagebox as messagebox
import validators
from PIL import Image, ImageTk  # Para carregar o logo

# Funções auxiliares
def carregar_canais():
    if os.path.exists(".channels"):
        with open(".channels", "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def salvar_canais(canais):
    with open(".channels", "w") as f:
        f.writelines([canal + "\n" for canal in canais])

# Classe principal
class PodcastStreamer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Podcast Streamer")
        self.geometry("900x600")
        
        self.canais = carregar_canais()
        self.player = None
        self.instance = vlc.Instance()

        # Layout principal
        self.grid_columnconfigure(1, weight=1)  # Configura expansão da área principal
        self.grid_rowconfigure(0, weight=1)

        # Menu lateral
        self.menu_frame = ctk.CTkFrame(self, width=200)
        self.menu_frame.grid(row=0, column=0, sticky="ns")
        self.menu_frame.grid_propagate(False)

        # Adicionando o logo
        try:
            logo = Image.open("image.png")
            logo = logo.resize((150, 150), Image.ANTIALIAS)
            logo_img = ImageTk.PhotoImage(logo)
            self.logo_label = ctk.CTkLabel(self.menu_frame, image=logo_img, text="")
            self.logo_label.image = logo_img
            self.logo_label.pack(pady=20)
        except Exception as e:
            print(f"Erro ao carregar a imagem do logo: {e}")

        # Botões do menu lateral
        self.favoritos_button = ctk.CTkButton(self.menu_frame, text="Favoritos", command=self.favoritos)
        self.favoritos_button.pack(pady=10)

        self.home_button = ctk.CTkButton(self.menu_frame, text="Home Page", command=self.home_page)
        self.home_button.pack(pady=10)

        self.logout_button = ctk.CTkButton(self.menu_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side="bottom", pady=20)

        # Gêneros de podcast
        self.genres_label = ctk.CTkLabel(self.menu_frame, text="Gêneros de Podcast:")
        self.genres_label.pack(pady=10)

        self.genres = ["Tecnologia", "Comédia", "Saúde", "Negócios", "Cultura"]
        self.genres_combobox = ctk.CTkComboBox(self.menu_frame, values=self.genres)
        self.genres_combobox.pack(pady=5)

        # Área principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Widgets principais na área central
        self.add_url_label = ctk.CTkLabel(self.main_frame, text="Adicionar URL do Podcast:")
        self.add_url_label.pack(pady=5)

        self.add_url_entry = ctk.CTkEntry(self.main_frame, width=400)
        self.add_url_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(self.main_frame, text="Adicionar", command=self.adicionar_canal)
        self.add_button.pack(pady=5)

        self.list_canais_button = ctk.CTkButton(self.main_frame, text="Listar Canais", command=self.listar_canais)
        self.list_canais_button.pack(pady=10)

        self.canais_combobox = ctk.CTkComboBox(self.main_frame, values=self.canais or ["Nenhum canal"])
        self.canais_combobox.pack(pady=5)

        self.play_button = ctk.CTkButton(self.main_frame, text="Reproduzir", command=self.reproduzir_podcast)
        self.play_button.pack(pady=10)

        self.download_button = ctk.CTkButton(self.main_frame, text="Baixar Episódio", command=self.baixar_episodio)
        self.download_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(self.main_frame, text="Parar", command=self.parar_reproducao)
        self.stop_button.pack(pady=10)

        self.video_panel = ctk.CTkFrame(self.main_frame, width=400, height=300)
        self.video_panel.pack(pady=10)

        self.video_widget = self.video_panel.winfo_id()

    # Funções principais
    def favoritos(self):
        messagebox.showinfo("Favoritos", "Funcionalidade de Favoritos em desenvolvimento.")

    def home_page(self):
        messagebox.showinfo("Home Page", "Você já está na página inicial.")

    def logout(self):
        self.destroy()  # Fecha o programa

    def adicionar_canal(self):
        novo_canal = self.add_url_entry.get()
        if validators.url(novo_canal) and novo_canal not in self.canais:
            self.canais.append(novo_canal)
            salvar_canais(self.canais)
            self.add_url_entry.delete(0, ctk.END)
            self.canais_combobox.configure(values=self.canais)
            messagebox.showinfo("Sucesso", "Canal adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "URL inválida ou já adicionada.")

    def listar_canais(self):
        if self.canais:
            messagebox.showinfo("Canais", "\n".join(self.canais))
        else:
            messagebox.showinfo("Canais", "Nenhum canal adicionado.")

    def reproduzir_podcast(self):
        try:
            canal_index = self.canais_combobox.get()
            try:
                canal_index = int(canal_index)
                feed = feedparser.parse(self.canais[canal_index])
            except ValueError:
                messagebox.showerror("Erro", "Selecione um canal válido.")
                return

            if 'media_content' in feed.entries[0]:
                url_media = feed.entries[0].media_content[0]["url"]
            else:
                url_media = feed.entries[0].enclosures[0].href

            self.player = self.instance.media_player_new()
            media = self.instance.media_new(url_media)
            self.player.set_media(media)
            self.player.set_hwnd(int(self.video_panel.winfo_id()))
            self.player.audio_set_volume(50)

            if self.player.play() == -1:
                raise Exception("Falha ao reproduzir a mídia.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao reproduzir: {e}")

    def baixar_episodio(self):
        try:
            canal_index = self.canais_combobox.get()
            try:
                canal_index = int(canal_index)
                feed = feedparser.parse(self.canais[canal_index])
            except ValueError:
                messagebox.showerror("Erro", "Selecione um canal válido.")
                return

            if 'media_content' in feed.entries[0]:
                url_media = feed.entries[0].media_content[0]["url"]
            else:
                url_media = feed.entries[0].enclosures[0].href

            destino = os.path.join("downloads", os.path.basename(url_media))
            os.makedirs("downloads", exist_ok=True)
            wget.download(url_media, destino)
            messagebox.showinfo("Sucesso", f"Episódio baixado: {destino}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao baixar: {e}")

    def ajustar_volume(self, volume):
        if self.player:
            self.player.audio_set_volume(int(volume))

    def parar_reproducao(self):
        if self.player:
            self.player.stop()

if __name__ == "__main__":
    app = PodcastStreamer()
    app.mainloop()
