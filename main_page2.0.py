import os
from PIL import Image
import customtkinter as ctk
import webbrowser

# Função para abrir os links
def browser(link):
    webbrowser.open(link)

# Função para carregar dados dos podcasts
def carregar_dados_podcasts(ficheiro_podcast):
    podcasts = []
    try:
        with open(ficheiro_podcast, "r") as ficheiro:
            for line in ficheiro:
                partes = line.strip().split(",")
                if len(partes) == 3:
                    podcasts.append({"name": partes[0], "image": partes[1], "link": partes[2]})
    except FileNotFoundError:
        print(f"Arquivo {ficheiro_podcast} não encontrado!")
    return podcasts

# Criar o ficheiro de podcasts
with open("podcasts.txt", "w") as ficheiro_podcast:
    ficheiro_podcast.write("Joe Rogan,imagens/joerogan.png,https://www.youtube.com/live/ycPr5-27vSI?si=MLe4_W3phP3af-Cf\n")
    ficheiro_podcast.write("Peweecast,imagens/peweecast.png,https://youtu.be/RmyzRnLZ2WE?si=Yjtvme3ZIq_o8nXA\n")
    ficheiro_podcast.write("Joe Rogan,imagens/joerogan.png,https://www.youtube.com/live/ycPr5-27vSI?si=MLe4_W3phP3af-Cf\n")
    ficheiro_podcast.write("Peweecast,imagens/peweecast.png,https://youtu.be/RmyzRnLZ2WE?si=Yjtvme3ZIq_o8nXA\n")
    ficheiro_podcast.write("Chris Williamson,imagens/chris.png,https://youtu.be/DLfWv_Ey27s?si=0TBI6EcvkQ8LurOp\n")
    ficheiro_podcast.write("Flowpodcast,imagens/flowpodcast.png,https://youtu.be/P3mX2WB6xhQ?si=2IBW3XTF6zGY3WsC\n")
    ficheiro_podcast.write("The George Janko Show,imagens/georgejanko.png,https://youtu.be/6t-l0Y_uj9k?si=xgFd4n79eK74BrWo\n")
    ficheiro_podcast.write("The Diary of a CEO,imagens/thediary.png,https://youtu.be/jyCJeglqCe4?si=VRQnhegJ0gvIzdZO\n")
    ficheiro_podcast.write("Inteligencia ltda,imagens/inteligencia.png,https://youtu.be/3tsHfsk1o2I?si=uc_FvbVbjLAf4IiY\n")
    ficheiro_podcast.write("Shay Shay Club,imagens/shanon.png,https://youtu.be/JYL0blfer6M?si=sDptY0eD5wqZru8N\n")
    ficheiro_podcast.write("Lex Fridman,imagens/lexfridman.png,https://youtu.be/Kbk9BiPhm7o?si=sbSQMd_V55QC_Bw3\n")
    ficheiro_podcast.write("Pedro Mota,imagens/pedro.png,https://youtu.be/__bj2A4Ou5Q?si=tJQEWamDkewVsgPe\n")
    ficheiro_podcast.write("Joe Rogan,imagens/joerogan2.png,https://youtu.be/HwyAX69xG1Q?si=R6qj_XnOkP4qkx8p\n")
    ficheiro_podcast.write("The Flagrant,imagens/flagrant.png,https://youtu.be/LHTwv56jZ7E?si=UaOYFLgfHMTFUYay\n")
    ficheiro_podcast.write("The George Janko Show,imagens/georgejanko2.png,https://youtu.be/DND5JF9ioRw?si=fwY1pD2JBPZFKfvf\n")
    ficheiro_podcast.write("Peweecast,imagens/peweecast2.png,https://youtu.be/WXFcWcqGx80?si=D7tu2CVB6a5vkOiY\n")

    # Outros podcasts omitidos para concisão

# Função para página inicial
def pagina_inicial(user):
   
    main_page = ctk.CTk()
    main_page.title("PodSpot")
    main_page.geometry("1024x700")

    # Frame principal da janela inicial
    frame_principal = ctk.CTkFrame(master=main_page, fg_color="green")
    frame_principal.pack(fill="both", expand=True)

    # Menu lateral de navegação
    menu_lateral = ctk.CTkFrame(master=frame_principal, width=200, fg_color="#1DB954")
    menu_lateral.pack(side="left", fill="y")

    # Ícones do menu
    icon_home = ctk.CTkImage(light_image=Image.open("home_icon.png"), size=(30, 30))
    icon_estrelas = ctk.CTkImage(light_image=Image.open("staricon.png"), size=(30, 30))
    icon_trending = ctk.CTkImage(light_image=Image.open("tredingicon.png"), size=(30, 30))
    icon_favoritos = ctk.CTkImage(light_image=Image.open("favoritos.png"), size=(30, 30))
    icon_gostos = ctk.CTkImage(light_image=Image.open("Gostos.png"), size=(30, 30))

    # Tabs principais
    tabview = ctk.CTkTabview(master=frame_principal, width=800, height=500, corner_radius=20, fg_color="green")
    tabview.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    tab_home = tabview.add("Home")
    tab_estrelas = tabview.add("Estrelas")
    tab_trending = tabview.add("Trending")
    tab_favorites = tabview.add("Favoritos")
    tab_gostos = tabview.add("Gostos")

    # Botões do menu lateral
    ctk.CTkButton(menu_lateral, text="Home", image=icon_home, compound="left",
                  fg_color="#1DB954", command=lambda: tabview.set("Home")).pack(pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral, text="Estrelas", image=icon_estrelas, compound="left",
                  fg_color="#1DB954", command=lambda: tabview.set("Estrelas")).pack(pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral, text="Trending", image=icon_trending, compound="left",
                  fg_color="#1DB954", command=lambda: tabview.set("Trending")).pack(pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral, text="Favoritos", image=icon_favoritos, compound="left",
                  fg_color="#1DB954", command=lambda: tabview.set("Favoritos")).pack(pady=20, padx=10, anchor="w")
    ctk.CTkButton(menu_lateral, text="Gostos", image=icon_gostos, compound="left",
                  fg_color="#1DB954", command=lambda: tabview.set("Gostos")).pack(pady=20, padx=10, anchor="w")

    # ScrollFrame da aba Home
    scroll_frame = ctk.CTkScrollableFrame(master=tab_home, width=200, height=200, fg_color="black")
    scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Carregar dados dos podcasts
    ficheiro_podcast = carregar_dados_podcasts("podcasts.txt")
    favoritos = []
    gostos = []

    # Função para atualizar Favoritos
    def atualizar_favoritos():
        for widget in tab_favorites.winfo_children():
            widget.destroy()
        for podcast in favoritos:
            podcast_image = ctk.CTkImage(dark_image=Image.open(podcast["image"]), size=(150, 150))
            ctk.CTkButton(tab_favorites, image=podcast_image, text=podcast["name"], compound="top",
                          fg_color="green", command=lambda link=podcast["link"]: browser(link)).pack(pady=10, padx=10)

    # Função para atualizar Gostos
    def atualizar_gostos():
        for widget in tab_gostos.winfo_children():
            widget.destroy()
        for podcast in gostos:
            podcast_image = ctk.CTkImage(dark_image=Image.open(podcast["image"]), size=(150, 150))
            ctk.CTkButton(tab_gostos, image=podcast_image, text=podcast["name"], compound="top",
                          fg_color="green", command=lambda link=podcast["link"]: browser(link)).pack(pady=10, padx=10)

    # Função para adicionar aos Favoritos
    def adicionar_favoritos(podcast):
        if podcast in favoritos:
            favoritos.remove(podcast)
        else:
            favoritos.append(podcast)
        atualizar_favoritos()

    # Função para adicionar aos Gostos
    def adicionar_gostos(podcast):
        if podcast in gostos:
            gostos.remove(podcast)
        else:
            gostos.append(podcast)
        atualizar_gostos()

    # Criar botões para cada podcast na aba Home
    for idx, podcast in enumerate(ficheiro_podcast):
        frame_podcast = ctk.CTkFrame(master=scroll_frame, fg_color="green")
        frame_podcast.grid(row=idx // 4, column=idx % 4, padx=10, pady=10)

        podcast_image = ctk.CTkImage(dark_image=Image.open(podcast["image"]), size=(150, 150))

        # Adiciona podcast na Home
        ctk.CTkButton(master=frame_podcast, image=podcast_image, text=podcast["name"], compound="top",
                      fg_color="green", width=150, height=100, command=lambda link=podcast["link"]: browser(link)).pack(pady=(0, 5))
        ctk.CTkButton(master=frame_podcast, text="Favoritar", command=lambda p=podcast: adicionar_favoritos(p)).pack(pady=(5, 0))
        ctk.CTkButton(master=frame_podcast, text="Gostos", command=lambda p=podcast: adicionar_gostos(p)).pack(pady=(5, 0))

    # Atualizar as abas ao abrir a janela
    atualizar_favoritos()
    atualizar_gostos()

    main_page.mainloop()

#pagina_inicial('')
