import os
from PIL import Image
import customtkinter as ctk
import webbrowser
from tkinter import messagebox
import glob

# Função para abrir os links
def browser(link):
    webbrowser.open(link)

# Função para carregar dados dos podcasts
def carregar_dados_podcasts(ficheiro_podcast):
    podcasts = []
    try:
        with open("podcasts.txt","r") as ficheiro_podcast:
            for line in ficheiro_podcast:
                partes = line.strip().split(",")
                if len(partes) == 3:
                    podcasts.append({"name":partes[0],"image":partes[1],"link":partes[2]})
    except FileNotFoundError:
        print(f"Arquivo {ficheiro_podcast} não encontrado !")
    return podcasts

"""
Criar um ficheiro txt onde estarão os 
dados dos podcasts
"""
with open("podcasts.txt","w") as ficheiro_podcast:
        ficheiro_podcast.write("Joe Rogan,imagens/joerogan.png,https://www.youtube.com/live/ycPr5-27vSI?si=MLe4_W3phP3af-Cf\n")
        ficheiro_podcast.write("Peweecast,imagens/peweecast.jpeg,https://youtu.be/RmyzRnLZ2WE?si=Yjtvme3ZIq_o8nXA\n")
        ficheiro_podcast.write("Chris Williamson,imagens/chris.jpeg,https://youtu.be/DLfWv_Ey27s?si=0TBI6EcvkQ8LurOp\n")
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
        ficheiro_podcast.write("Shay Shay Club,imagens/shanon2.png,https://youtu.be/8oRRZiRQxTs?si=NpFt07LtOV5UhJvk\n")
        ficheiro_podcast.write("The Flagrant,imagens/flagrant2.png,https://youtu.be/Ry1IjOft95c?si=lXJY35VtndhAuKDH\n")


# Função para página inicial
def pagina_inicial(user):


   


    favoritos = []
    gostos = []
    main_page = ctk.CTk()
    main_page.title("PodSpot")
    main_page.geometry("1024x700")
    main_page.resizable()

    # Frame principal da janela inicial
    frame_principal = ctk.CTkFrame(master=main_page,fg_color="green")
    frame_principal.pack(fill="both",expand=True)

    # Menu lateral de navegação
    menu_lateral = ctk.CTkFrame(master=frame_principal,width=400,fg_color="#1DB954")
    menu_lateral.pack(side="left",fill="y")

   # Barra de Pesquisa

    frame_pesquisa = ctk.CTkFrame(main_page,width=800)
    frame_pesquisa.pack(pady=20,expand=True)

    # Entrada de texto para a barra de pesquisa

    entry_pesquisa = ctk.CTkEntry(frame_pesquisa,width=400,placeholder_text="Pesquisa um podcast...")
    entry_pesquisa.pack(side="left",padx=10)

    # Frame para exibir os resultados da pesquisa

    frame_resultados_pesquisa = ctk.CTkFrame(main_page,fg_color="green",width=800,height=1020)
    frame_resultados_pesquisa.pack(fill="both",expand=True,padx=20,pady=20)

    scroll_pesquisa = ctk.CTkScrollableFrame(frame_resultados_pesquisa,height=500,fg_color="black")
    scroll_pesquisa.pack(fill="both",expand=True,padx=10,pady=10)
    
    # Função para pesquisar
    def pesquisar():
        for widget in scroll_pesquisa.winfo_children():
            widget.destroy
        
        query = entry_pesquisa.get().strip().lower()
        if not query:
            messagebox.showinfo("Pesquisa","Por favor,insira o nome de um podcast.")
            return
        # Carregar dados dos Podcasts

        with open("podcasts.txt","r") as ficheiro_podcast:
            podcasts_disponiveis = [line.strip().split(",")for line in ficheiro_podcast.readlines()]

            resultados = [podcast for podcast in podcasts_disponiveis if query in podcast[0].lower()]

            if resultados:
                for podcast in resultados:
                    # Carregar imagem do Podacast Pesquisado
                    podcast_image = ctk.CTkImage(dark_image=Image.open(podcast[1]),size=(70,70))

                    btn_podcast = ctk.CTkButton(scroll_pesquisa,image=podcast_image,text=podcast[0],
                    compound="left",fg_color="transparent",text_color="white", command=lambda link=podcast[2]:browser(link),)
                    btn_podcast.pack(side="left",padx=10)
            else:
                ctk.CTkLabel(frame_resultados_pesquisa,text="Nenhum podcast encontrado",text_color="white",font=("Helvetica",16)).pack(pady=20)

    # Icones para o Menu
    icon_home = ctk.CTkImage(light_image=Image.open("home_icon.png"),size=(30,30))
    icon_estrelas = ctk.CTkImage(light_image=Image.open("staricon.png"),size=(30,30))
    icon_trending = ctk.CTkImage(light_image=Image.open("tredingicon.png"),size=(30,30))
    icon_favoritos = ctk.CTkImage(light_image=Image.open("favoritos.png"),size=(30,30))
    icon_gostos = ctk.CTkImage(light_image=Image.open("imagens/Gostos.png"), size=(30, 30))
    icon_user = ctk.CTkImage(light_image=Image.open("usericone.png"),size=(30,30))
    icon_humor = ctk.CTkImage(light_image=Image.open("humor.png"),size=(30,30))
    icon_desenvolvimento = ctk.CTkImage(light_image=Image.open("imagens/desenvolvimento.png"),size=(30,30))
    icon_entretenimento = ctk.CTkImage(light_image=Image.open("imagens/entertenimento.png"),size=(30,30))


    # Tabs: Home, Estrelas, Trending, Favoritos, gostos
    tabview = ctk.CTkTabview(master=frame_principal,width=800,height=500,corner_radius=20,fg_color="green")
    tabview.pack(side="right",fill="both",expand = True,padx=10,pady=10)

    tab_home = tabview.add("Home")
    tab_estrelas = tabview.add("Estrelas")
    tab_trending = tabview.add("Trending")
    tab_favorites = tabview.add("Favoritos")
    tab_gostos = tabview.add("Gostos")
    tab_humor = tabview.add("Humor")
    tab_desenvolvimento = tabview.add("Desenvolvimento")
    tab_entertenimento = tabview.add("Entertenimento")
    tab_user = tabview.add("Perfil")

    # Botões no menu lateral
    
    btn_pesquisar = ctk.CTkButton(frame_pesquisa, text="Search", command=pesquisar)
    
    btn_pesquisar.pack(side="left", padx=5)

    btn_home = ctk.CTkButton(menu_lateral,text="Home",image=icon_home,compound="left",
                            fg_color="#1DB954",command=lambda:tabview.set("Home"))
    btn_home.pack(pady=20,padx=10,anchor="w")

    btn_estrelas = ctk.CTkButton(menu_lateral,text="Estrelas",image=icon_estrelas,compound="left",
                                fg_color="#1DB954",command=lambda:tabview.set("Estrelas"))
    btn_estrelas.pack(pady=20,padx=10,anchor="w")

    btn_trending = ctk.CTkButton(menu_lateral,text="Trending",image=icon_trending,compound="left",
                                fg_color="#1DB954",command=lambda:tabview.set("Trending"))
    btn_trending.pack(pady=20,padx=10,anchor="w")

    btn_favoritos = ctk.CTkButton(menu_lateral,text="Favoritos",image=icon_favoritos,compound="left",
                                fg_color="#1DB954",command=lambda:tabview.set("Favoritos"))
    btn_favoritos.pack(pady=20,padx=10,anchor="w")

    ctk.CTkButton(menu_lateral, text="Gostos", image=icon_gostos, compound="left",
                  fg_color="#1DB954", command=lambda: tabview.set("Gostos")).pack(pady=20, padx=10, anchor="w")
    
    btn_humor = ctk.CTkButton(menu_lateral,text="Humor",image=icon_humor,compound="left",
                                fg_color="#1DB954",command=lambda:tabview.set("Humor"))
    btn_humor.pack(pady=20,padx=10,anchor="w")

    btn_desenvolvimento = ctk.CTkButton(menu_lateral,text="Desenvolvimento",image=icon_desenvolvimento,compound="left",
                                    fg_color="#1DB954",command=lambda:tabview.set("Desenvolvimento"))
    btn_desenvolvimento.pack(pady=20,padx=10,anchor="w")

    btn_entertenimento = ctk.CTkButton(menu_lateral,text="Entertenimento",image=icon_entretenimento,compound="left",
                                    fg_color="#1DB954",command=lambda:tabview.set("Entertenimento"))
    btn_entertenimento.pack(pady=20,padx=10,anchor="w")

    btn_user = ctk.CTkButton(menu_lateral,text="Perfil",image=icon_user,compound="left",fg_color="#1DB954",command=lambda:tabview.set("Perfil"))
    btn_user.pack(pady=20,padx=10,anchor="w")


    # Scrollbar para a tab home
    scroll_frame = ctk.CTkScrollableFrame(master=tab_home,width=200,height=200,fg_color="black")
    scroll_frame.pack(fill="both",expand=True,padx=10,pady=10)

    #Carregar dados do arquivo
    ficheiro_podcast = carregar_dados_podcasts("podcasts.txt")
    print(ficheiro_podcast)


    # Loop para criar botões de podcast
    for i in range(6):
        for j in range(4):
            idx = i * 4 + j
            if idx < len(ficheiro_podcast):
                frame_podcasts = ctk.CTkFrame(master=scroll_frame,fg_color="green")
                frame_podcasts.grid(row=i, column=j,padx=10,pady=10)

                # Carregar imagem do podcast
                podcast_image = ctk.CTkImage(dark_image=Image.open(ficheiro_podcast[idx]["image"]),size=(150,150))

                # Criar botões dos podcasts
                btn_podcast = ctk.CTkButton(master=frame_podcasts,image=podcast_image,text=ficheiro_podcast[idx]["name"],
                                            compound="top",fg_color="green",width=150,height=100,
                                        command=lambda link=ficheiro_podcast[idx]["link"]:browser(link))
                btn_podcast.pack(pady=(0,5))

                # Botão de favoritar
                btn_favoritar = ctk.CTkButton(master=frame_podcasts,text="Favoritar",height=30,width=30,
                                            command=lambda podcast=ficheiro_podcast[idx]:adicionar_favoritos(podcast))
                btn_favoritar.pack(pady=(5,0))

                btn_gostos = ctk.CTkButton(master=frame_podcasts,text="gostos",height=30,width=30,
                                            command=lambda podcast=ficheiro_podcast[idx]:adicionar_gostos(podcast))
                btn_gostos.pack(pady=(5,0))
            
            
    

    # Função para atualizar a tab favoritos
    def atualizar_favoritos():
        for widget in tab_favorites.winfo_children():
            widget.destroy()

        for i, podcast in enumerate(favoritos):
            podcast_image = ctk.CTkImage(dark_image=Image.open(podcast["image"]), size=(150, 150))

            btn_podcast = ctk.CTkButton(master=tab_favorites, image=podcast_image, text=f"Podcast {i+1}", 
                                        compound="top", fg_color="green", width=150, height=100,
                                        command=lambda link=podcast["link"]: browser(link))
            btn_podcast.grid(row=i // 4, column=i % 4, padx=10, pady=10)

        
    def atualizar_gostos():
        for widget in tab_gostos.winfo_children():
            widget.destroy()

        for i, podcast in enumerate(gostos):
            podcast_image = ctk.CTkImage(dark_image=Image.open(podcast["image"]), size=(150, 150))

            btn_podcast = ctk.CTkButton(master=tab_gostos, image=podcast_image, text=f"Podcast {i+1}", 
                                        compound="top", fg_color="green", width=150, height=100,
                                        command=lambda link=podcast["link"]: browser(link))
            btn_podcast.grid(row=i // 4, column=i % 4, padx=10, pady=10)


    def atualizar_user():
        for widget in tab_user.winfo_children():
            widget.destroy()

       


    # Função de adicionar favoritos
    def adicionar_favoritos(podcast):
        if podcast in favoritos:
            favoritos.remove(podcast)
            messagebox.showinfo("Favoritos",f"{podcast['name']} removido dos favoritos")
    
        else:
            favoritos.append(podcast)
            messagebox.showinfo("Favoritos",f"O Podcast {podcast['name']} foi adicionado aos favoritos!")
        atualizar_favoritos() 

    #adicionar gostos
    def adicionar_gostos(podcast):
        if podcast in gostos:
            gostos.remove(podcast)
            messagebox.showinfo("Gostos",f"{podcast['name']} foi removido dos gostos")
        else:
            gostos.append(podcast)
            messagebox.showinfo("Gostos",f"O Podcast {podcast['name']} foi adicionado aos gostos!")
        atualizar_gostos()

    # Conteudo da Tab de Estrelas.
    label_estrelas =ctk.CTkLabel(tab_estrelas,text="Estrelas",text_color="white",font=("Helvetica",28))
    label_estrelas.pack(pady=20)

    # Scroll Bar para a tab estrelas
    estrelas_scroll_frame = ctk.CTkScrollableFrame(master=tab_estrelas,width=200,height=200,fg_color="black")
    estrelas_scroll_frame.pack(fill="both",expand=True,padx=10,pady=10)

    # Função para carregar os dados das estrelas
    def carregar_dados_estrelas(ficheiro_estrela):
        estrelas = []
        try:
            with open("estrelas.txt","r") as ficheiro_estrela:
                for line in ficheiro_estrela:
                  partes_estrela = line.strip().split(",")
                  if len(partes_estrela) == 3:
                    estrelas.append({"name":partes_estrela[0],"image":partes_estrela[1],"link":partes_estrela[2]})
        except FileNotFoundError:
            print(f"Arquivo {ficheiro_estrela} não encontrado !")
        return estrelas 

    with open("estrelas.txt","w") as ficheiro_estrela:

        ficheiro_estrela.write("Joe Rogan,imagens/joerogan.png,https://www.youtube.com/results?search_query=joe+rogan\n")
        ficheiro_estrela.write("Lex Fridman,imagens/lexfridmanphoto.png,https://www.youtube.com/results?search_query=lex+fridman\n")
        ficheiro_estrela.write("George Janko,imagens/georgejanko.png,https://www.youtube.com/results?search_query=george+janko\n")
        ficheiro_estrela.write("Chris Williamson,imagens/chris.jpeg,https://www.youtube.com/@ChrisWillx\n")
        ficheiro_estrela.write("Shanon Sharpe,imagens/shanon.png,https://www.youtube.com/@ClubShayShay\n")
        ficheiro_estrela.write("Andrew Schulz,imagens/Andrew.png,https://www.youtube.com/@OfficialFlagrant\n")
        ficheiro_estrela.write("Vilela Rogerio,imagens/vilela.png,https://www.youtube.com/@inteligencialtda\n")
        ficheiro_estrela.write("Pedro Mota,imagens/pedro.png,https://www.youtube.com/results?search_query=pedro+teixeira+da+mota\n")
        ficheiro_estrela.write("Steve Bartllet,imagens/steven.png,https://www.youtube.com/@TheDiaryOfACEO\n")
   
      # Função para abrir os links
    def browser(link):
        webbrowser.open(link)

    estrelas = carregar_dados_estrelas("estrelas.txt")

    for i in range(4):
      for j in range(3):
          idx = i * 3 + j
          if idx < len(estrelas):
                    frame_estrelas = ctk.CTkFrame(master=estrelas_scroll_frame,fg_color="transparent")
                    frame_estrelas.grid(row=i,column=j,padx=10,pady=10)

                    # Carregar imagens das estrelas
                    estrela_image = ctk.CTkImage(dark_image=Image.open(estrelas[idx]["image"]),size=(150,150))

                    # Cria botões com imagens
                    btn_stars = ctk.CTkButton(master=frame_estrelas,image=estrela_image,text=estrelas[idx]["name"],compound="top",
                                            fg_color="green",width=150,height=100,command=lambda link=estrelas[idx]["link"]:browser(link))
                    btn_stars.pack(pady=(0,5))


    #Conteudo da Aba Trending
    label_trending =ctk.CTkLabel(tab_trending,text="Trending",text_color="white",font=("Helvetica",28))
    label_trending.pack(pady=20)

    frame_treding = ctk.CTkFrame(master=tab_trending,fg_color="black")
    frame_treding.pack(fill="both",expand = True,padx=10,pady=10)

    # Função para carregar dados dos trendings
    def carregar_dados_trending(ficheiro_trending):
        trending = []
        try:
            with open("trending.txt","r") as ficheiro_trending:
                
                for line in ficheiro_trending:
                  partes_trending = line.strip().split(",")
                  if len(partes_trending) == 3:
                    trending.append({"name":partes_trending[0],"image":partes_trending[1],"link":partes_trending[2]})
        except FileNotFoundError:
            print(f"Arquivo {ficheiro_trending} não encontrado !")
        return trending

    with open("trending.txt","w") as ficheiro_trending:
        
        ficheiro_trending.write("Joe Rogan,imagens/joeroganlogo.png,https://www.youtube.com/results?search_query=joe+rogan\n")
        ficheiro_trending.write("Peweecast,imagens/peweecastlogo.png,https://www.youtube.com/@PeeWeeCast\n")
        ficheiro_trending.write("Shay Shay Club,imagens/shanonlogo.png,https://www.youtube.com/@ClubShayShay\n")
        ficheiro_trending.write("Flagrant,imagens/flagrantlogo.png,https://www.youtube.com/@OfficialFlagrant\n")
        
        
    def browser(link):
        webbrowser.open(link)
    
    trending = carregar_dados_trending("trending.txt")
    
    for i, trending in enumerate(trending):
        trendig_imagem = ctk.CTkImage(dark_image=Image.open(trending["image"]),size=(100,100))

        btn_trending = ctk.CTkButton(master=frame_treding,image=trendig_imagem,text="",compound="top",
                                     fg_color="green",width=150,height=150,command=lambda link= trending["link"]:browser(link),corner_radius=30)
        btn_trending.grid(row=i//2, column = i%2, padx=10,pady=10)


    
    # Conteudo da Aba Favoritos
    label_favoritos =ctk.CTkLabel(tab_favorites,text="",text_color="white",font=("Helvetica",28))
    label_favoritos.pack(pady=20)

    frame_favoritos = ctk.CTkFrame(master=tab_favorites,fg_color="black")
    frame_favoritos.pack(fill="both",expand=True,padx=10,pady=10)

    # Conteudo da aba Humor
    label_humor = ctk.CTkLabel(tab_humor,text="Humor",font=("Helvetica",28))
    label_humor.pack(pady=20)

    frame_humor = ctk.CTkFrame(master=tab_humor,fg_color="black")
    frame_humor.pack(fill="both",expand = True,padx=10,pady=10)


    # Função para carregar dados dos podcasts de humor
    def carregar_dados_humor(ficheiro_humor):
        humor = []
        try:
            with open("humor.txt","r") as ficheiro_humor:
                
                for line in ficheiro_humor:
                  partes_humor = line.strip().split(",")
                  if len(partes_humor) == 3:
                    humor.append({"name":partes_humor[0],"image":partes_humor[1],"link":partes_humor[2]})
        except FileNotFoundError:
            print(f"Arquivo {ficheiro_humor} não encontrado !")
        return humor
    
    with open("humor.txt","w") as ficheiro_humor:

        ficheiro_humor.write("Shay Shay Club,imagens/shanonlogo.png,https://www.youtube.com/@ClubShayShay\n")
        ficheiro_humor.write("ShxtsnGigs Podcast,imagens/sixguys.jpg,https://www.youtube.com/@ShtsNGigsPodcast\n")
        ficheiro_humor.write("800 Pound Gorilla Media,imagens/gorrila.png,https://www.youtube.com/@800pgm/videos\n")
    
    
    def browser(link):
        webbrowser.open(link)
    
    humor = carregar_dados_humor(ficheiro_humor)

    for i, humor in enumerate(humor):
        humor_imagem = ctk.CTkImage(dark_image=Image.open(humor["image"]),size=(100,100))

        btn_humor = ctk.CTkButton(master=frame_humor,image=humor_imagem,text="",compound="top",
                                     fg_color="green",width=150,height=150,command=lambda link= humor["link"]:browser(link),corner_radius=30)
        btn_humor.grid(row=i//2, column = i%2, padx=10,pady=10)
    
    
    # Conteudo da aba de Desenvolvimento
    label_desenvolvimento = ctk.CTkLabel(tab_humor,text="Desenvolvimento Pessoal",font=("Helvetica",28))
    label_desenvolvimento.pack(pady=20)

    frame_desenvolvimento = ctk.CTkFrame(master=tab_desenvolvimento,fg_color="black")
    frame_desenvolvimento.pack(fill="both",expand = True,padx=10,pady=10)

    # Função para carregar dados dos podcasts de Desenvolvimento
    def carregar_dados_desenvolvimento(ficheiro_desenvolvimento):
        desenvolvimento = []
        try:
            with open("desenvolvimento.txt","r") as ficheiro_desenvolvimento:
                
                for line in ficheiro_desenvolvimento:
                  partes_desenvolvimento = line.strip().split(",")
                  if len(partes_desenvolvimento) == 3:
                    desenvolvimento.append({"name":partes_desenvolvimento[0],"image":partes_desenvolvimento[1],"link":partes_desenvolvimento[2]})
        except FileNotFoundError:
            print(f"Arquivo {ficheiro_desenvolvimento} não encontrado !")
        return desenvolvimento
    
    with open("desenvolvimento.txt","w") as ficheiro_desenvolvimento:

        ficheiro_desenvolvimento.write("The Diary of a CEO,imagens/steven.png,https://www.youtube.com/@TheDiaryOfACEO\n")
        ficheiro_desenvolvimento.write("Lex Fridman,imagens/lexfridmanphoto.png,https://www.youtube.com/results?search_query=lex+fridman\n")
        ficheiro_desenvolvimento.write("The Mindset Mentor Podcast,imagens/mindset.png,https://www.youtube.com/@mindsetmentorpodcast\n")
        ficheiro_desenvolvimento.write("Chris Williamson,imagens/chris.jpeg,https://www.youtube.com/@ChrisWillx\n")

    def browser(link):
        webbrowser.open(link)
    
    desenvolvimento = carregar_dados_desenvolvimento(ficheiro_desenvolvimento)

    for i, desenvolvimento in enumerate(desenvolvimento):
        desenvolvimento_image = ctk.CTkImage(dark_image=Image.open(desenvolvimento["image"]),size=(100,100))

        btn_desenvolvimento = ctk.CTkButton(master=frame_desenvolvimento,image=desenvolvimento_image,text=desenvolvimento["name"],compound="top",
                                        fg_color="green",width=150,height=150,command=lambda link=desenvolvimento["link"]:browser(link),corner_radius=30)
        btn_desenvolvimento.grid(row=i//2, column = i%2, padx=10,pady=10)

    # Conteudo da aba de Entertrenimento
    label_entertenimento = ctk.CTkLabel(tab_entertenimento,text="Entertenimento",font=("Helvetica",28))
    label_entertenimento.pack(pady=20)

    frame_entertenimento = ctk.CTkFrame(master=tab_entertenimento,fg_color="black")
    frame_entertenimento.pack(fill="both",expand = True,padx=10,pady=10)


    # Função para carregar dados dos podcasts de Entertenimento
    def carregar_dados_entertenimento(ficheiro_entertenimento):
        entertenimento = []
        try:
            with open("entertenimento.txt","r") as ficheiro_entertenimento:
                
                for line in ficheiro_entertenimento:
                  partes_entertenimento = line.strip().split(",")
                  if len(partes_entertenimento) == 3:
                    entertenimento.append({"name":partes_entertenimento[0],"image":partes_entertenimento[1],"link":partes_entertenimento[2]})
        except FileNotFoundError:
            print(f"Arquivo {ficheiro_entertenimento} não encontrado !")
        return entertenimento
    
    with open("entertenimento.txt","w") as ficheiro_entertenimento:

        ficheiro_entertenimento.write("Joe Rogan,imagens/joeroganlogo.png,https://www.youtube.com/results?search_query=joe+rogan\n")
        ficheiro_entertenimento.write("Peweecast,imagens/peweecastlogo.png,https://www.youtube.com/@PeeWeeCast\n")
        ficheiro_entertenimento.write("Flagrant,imagens/flagrantlogo.png,https://www.youtube.com/@OfficialFlagrant\n")
        ficheiro_entertenimento.write("Flow Podcast,imagens/flowpodcastlogo.png,https://www.youtube.com/@FlowPodcast\n")

    def browser(link):
        webbrowser.open(link)
    
    entertenimento = carregar_dados_entertenimento(ficheiro_entertenimento)

    for i, entertenimento in enumerate(entertenimento):
        entertenimento_image = ctk.CTkImage(dark_image=Image.open(entertenimento["image"]),size=(100,100))

        btn_entertenimento = ctk.CTkButton(master=frame_entertenimento,image=entertenimento_image,text=entertenimento["name"],compound="top",
                                        fg_color="green",width=150,height=150,command=lambda link=entertenimento["link"]:browser(link),corner_radius=30)
        btn_entertenimento.grid(row=i//2, column = i%2, padx=10,pady=10)
    

    # Conteudo da aba de User
    label_user = ctk.CTkLabel(tab_user,text="User",font=("Helvetica",28))
    label_user.pack(pady=20)

    frame_user = ctk.CTkFrame(master=tab_user,fg_color="black")
    frame_user.pack(fill="both",expand = True,padx=10,pady=10)

     # Título
    titulo = ctk.CTkLabel(master=frame_user, text="Informações do Usuário",
                          font=ctk.CTkFont(size=20, weight="bold"), text_color="white")
    titulo.pack(pady=10)

    # Frame para o formulário
    form_frame = ctk.CTkFrame(master=frame_user, fg_color="#282828", corner_radius=15)
    form_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Dados fictícios do usuário (você pode integrar com um banco de dados depois)
    user_data = {
        "Nome": user[0],
        "Data de Criação": user[3],
        "Tipo de Usuário":  user[4],
        "Email": user[1],
        "Data de Nascimento": user[5],
        "Telefone":  user[6],
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
                values=["User"],
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
        master=frame_user,
        text="Salvar Alterações",
        fg_color="#1DB954",
        text_color="white",
        corner_radius=10,
        command=salvar_alteracoes
    )
    salvar_btn.pack(pady=10)

    # Função de logout
    def logout():
        main_page.destroy()

        #todo: check this
          # Fecha a janela atual
        print("Usuário desconectado.")  # Aqui você pode adicionar a lógica para retornar à tela de login

    # Botão de logout
    logout_btn = ctk.CTkButton( master=frame_principal, text="Logout", fg_color="#E74C3C", text_color="white", corner_radius=10,command=logout)
    logout_btn.pack(pady=10)

  

    main_page.mainloop()

#pagina_inicial('')

