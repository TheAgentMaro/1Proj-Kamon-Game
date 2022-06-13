from Systeme import Game
from SystemeIA import GameIA
from SystemeOnline import GameOnline

#------------------------------------#
from tkinter import *
import tkinter
from PIL import Image, ImageTk
#------------------------------------#

#Pygame musique 
import pygame
pygame.mixer.init()
pygame.mixer.music.load("RUDE.ogg")

#------------------------------------#


class Menu: 
    
    def __init__(self):
        
        #------------------------------------ Tkinter main fenétre ------------------------------------#
        
        self.__main = Tk(className=" KAMON ")
        self.__main.geometry("1440x900")
        self.__main.iconbitmap('kamon.ico')

        
        #------------------------------------background  ------------------------------------# 
        
        self.__Kamonbg = self.image("assets/background.jpg", 1440, 900)
        

        #------------------------------------List des logos ------------------------------------ #
    
        self.__kamonLogos = [   "assets\logo\kamon1.png",
                                "assets\logo\kamon2.png",
                                "assets\logo\kamon3.png",
                                "assets\logo\kamon4.png",
                                "assets\logo\kamon5.png",
                                "assets\logo\kamon6.png"]
        
        #------------------------------------ Liste des couleurs  ------------------------------------#
        
        self.__listcouleur = [
                             "light slate gray",
                             "red",
                             "hot pink",
                             "light sky blue",
                             "orange",
                             "chartreuse4",
                             "yellow2",
                             "HotPink3",
                             "DodgerBlue3",
                             "SlateBlue3",
                             "goldenrod3",
                             "PaleGreen2",
                             "orchid4",
                             "magenta4",
                             "tan4",
                             "sea green"]
        
        #------------------------------------#Themes + Styles #------------------------------------ #
        
        self.__themeSamurai = (self.__Kamonbg, self.__listcouleur, self.__kamonLogos)
        self.__samuraiTheme = self.__themeSamurai
        self.__fgcouleur = "white"
        self.__bgcouleur = "#696969"
        self.__bdSize = 5
        self.__bdcouleur = "#D16928"

        
        #------------------------------------# Background main #------------------------------------#
        self.__bg = Canvas(self.__main, width=1400, height=900, highlightthickness=0)
        self.__bg.place(x=720, y=450, anchor="center")
        self.__bgImage = self.__samuraiTheme[0]
        self.__bg.create_image(720, 450, image = self.__bgImage) 
         
        
        #------------------------------------# Label Kamon #------------------------------------#
        logo = tkinter.PhotoImage(file = "assets/logokamon.png")
        self.__labelKamon = Label(self.__main, image=logo, highlightthickness=self.__bdSize,)
        self.__labelKamon.place(x=720, y=250, anchor="center")
        self.__labelKamonConfig = [720, 200]
        
        #------------------------------------# Boutton 1vs1 #------------------------------------#
        img1 = tkinter.PhotoImage(file = "assets/button_vs.png")
        self.__button1vs1 = Button(self.__main,image=img1, fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: [self.changeDisplay([self.__labelKamon, self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonParametreKamon, self.__buttonQuitterGame], [self.__canvasPlateau, self.__buttonPAUSE, self.__buttonMusic , self.__buttonMusic2, self.__buttonMusic3], [self.__canvasPlateauConfig, self.__buttonPAUSEConfig,self.__buttonMusicconfig,self.__buttonMusicconfigp,self.__buttonMusicconfigs]), self.startGame(37, 70)], highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__button1vs1.place(x=720, y=400, anchor="center")
        self.__button1vs1Config = [720, 400]
        
        #------------------------------------# Boutton 1vsIA #------------------------------------#
        img2 = tkinter.PhotoImage(file = "assets/button_vs-ia.png")
        self.__button1vsIA = Button(self.__main, image=img2, fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: [self.changeDisplay([self.__labelKamon, self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonParametreKamon, self.__buttonQuitterGame], [self.__canvasPlateau, self.__buttonPAUSE, self.__buttonMusic, self.__buttonMusic2, self.__buttonMusic3], [self.__canvasPlateauConfig, self.__buttonPAUSEConfig,self.__buttonMusicconfig,self.__buttonMusicconfigp,self.__buttonMusicconfigs]),self.startGameIA(37, 70)], highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__button1vsIA.place(x=720, y=500, anchor="center")
        self.__button1vsIAConfig = [720, 500]
        
        #------------------------------------# Boutton 1vs1 Online #------------------------------------#
        img3 = tkinter.PhotoImage(file = "assets/button_vs-online.png")
        self.__button1vs1online = Button(self.__main, image=img3 ,fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelKamon, self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonParametreKamon, self.__buttonQuitterGame], [self.__labelOnline, self.__buttonBackOnline, self.__buttonJoin,  self.__joinEntryArea, ], [self.__labelOnlineConfig, self.__buttonBackOnlineConfig, self.__buttonJoinConfig,  self.__joinEntryAreaConfig]), highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__button1vs1online.place(x=720, y=600, anchor="center")
        self.__button1vs1onlineConfig = [720, 600]
        
        #------------------------------------# Boutton Parametre Kamon #------------------------------------#
        img4 = tkinter.PhotoImage(file = "assets/parametre.png")
        self.__buttonParametreKamon = Button(self.__main,image=img4, fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelKamon, self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonParametreKamon, self.__buttonQuitterGame], [self.__labelParametreMenu, self.__buttonBackParametreMenu], [self.__labelParametreMenuConfig, self.__buttonBackParametreMenuConfig]),  highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonParametreKamon.place(x=1300, y=100, anchor="center")
        self.__buttonParametreKamonConfig = [1300, 100]
        
        #------------------------------------# Boutton Quitter Game #------------------------------------#
        img5 = tkinter.PhotoImage(file = "assets/button_quitter.png")
        self.__buttonQuitterGame = Button(self.__main,  image=img5, fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.__main.destroy(), highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonQuitterGame.place(x=720, y=700, anchor="center")
        self.__buttonQuitterGameConfig = [720, 700]
        
        #------------------------------------# Label Online #------------------------------------#
        self.__labelOnline = Label(self.__main, text="ONLINE", font=("Helvetica", 44, "bold"), fg=self.__fgcouleur, bg=self.__bgcouleur, highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__labelOnlineConfig = [720, 200]
        
        
        #------------------------------------# Boutton Retour Online #------------------------------------#
        self.__buttonBackOnline = Button(self.__main, text='Back', font=("Helvetica", 24, "bold"), fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelOnline, self.__buttonBackOnline, self.__buttonJoin,  self.__joinEntryArea ], [self.__labelKamon, self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonParametreKamon, self.__buttonQuitterGame], [self.__labelKamonConfig, self.__button1vs1Config, self.__button1vsIAConfig, self.__button1vs1onlineConfig, self.__buttonParametreKamonConfig, self.__buttonQuitterGameConfig]),  highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonBackOnlineConfig = [100, 100]
        
        
        #------------------------------------# Bouton Join #------------------------------------#
        self.__buttonJoin = Button(self.__main, text='Join', font=("Helvetica", 24, "bold"), fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: [self.changeDisplay([self.__labelKamon, self.__buttonQuitterGame], [self.__canvasPlateau, self.__buttonPAUSE, self.__buttonMusic, self.__buttonMusic2, self.__buttonMusic3], [self.__canvasPlateauConfig, self.__buttonPAUSEConfig,self.__buttonMusicconfig,self.__buttonMusicconfigp,self.__buttonMusicconfigs]),self.startGameIA(37, 70)], highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonJoinConfig = [550, 400]

        #------------------------------------# Entrée Join #------------------------------------#
        self.__joinEntryArea = Entry(self.__main, font=("Helvetica", 20, "bold"), fg="black", bg="white", width=25, highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur, relief=FLAT)
        self.__joinEntryArea.insert(0, "(Entrer votre IP)")
        self.__joinEntryAreaConfig = [850, 400]

        
        #------------------------------------# Boutton PAUSE #------------------------------------#
        img6 = tkinter.PhotoImage(file = "assets/pause.png")
        self.__buttonPAUSE = Button(self.__main, image=img6, fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__buttonPAUSE, self.__canvasPlateau], [self.__labelPAUSE, self.__buttonBackPAUSE, self.__buttonParametrePAUSE, self.__buttonRelancer, self.__buttonSaveGame, self.__buttonQuitter], [self.__labelPAUSEConfig, self.__buttonBackPAUSEConfig, self.__buttonParametrePAUSEConfig, self.__buttonRelancerConfig, self.__buttonSaveGameConfig, self.__buttonQuitterConfig]), highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonPAUSEConfig = [1260, 50]

        
        
        #------------------------------------# Boutton Musique #------------------------------------#
        img7 = tkinter.PhotoImage(file = "assets/playmusic.png")
        self.__buttonMusic = Button(self.__main, image=img7, fg=self.__fgcouleur, bg=self.__bgcouleur, command=self.play ,highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonMusicconfig = [1300, 120]
        
        play = tkinter.PhotoImage(file = "assets/play.png")
        self.__buttonMusic2 = Button(self.__main, image=play, fg=self.__fgcouleur, bg=self.__bgcouleur, command=self.unpause ,highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonMusicconfigp = [1235, 190]
        
        stop = tkinter.PhotoImage(file = "assets/pausem.png")
        self.__buttonMusic3 = Button(self.__main, image=stop, fg=self.__fgcouleur, bg=self.__bgcouleur, command=self.paused ,highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonMusicconfigs = [1300, 190]
        
        
        
        #------------------------------------# Plateau Game #------------------------------------#
        self.__canvasPlateau = Canvas(self.__main, width=1200, height=900, highlightthickness=0, highlightbackground=self.__bdcouleur, bg="#1a1916")
        self.__canvasPlateauConfig = [605, 450]
        
        
        #------------------------------------# Label PAUSE #------------------------------------#
        self.__labelPAUSE = Label(self.__main, text="PAUSE", font=("Helvetica", 44, "bold"), fg=self.__fgcouleur, bg=self.__bgcouleur, highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__labelPAUSEConfig = [720, 200]
        
        
        #------------------------------------# Boutton Retour PAUSE #------------------------------------#
        backimg = tkinter.PhotoImage(file = "assets/back.png")
        self.__buttonBackPAUSE = Button(self.__main, image=backimg , fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelPAUSE, self.__buttonBackPAUSE, self.__buttonParametrePAUSE, self.__buttonRelancer, self.__buttonSaveGame, self.__buttonQuitter], [self.__buttonPAUSE, self.__canvasPlateau], [self.__buttonPAUSEConfig, self.__canvasPlateauConfig]),  highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonBackPAUSEConfig = [100, 100]
        
        
        #------------------------------------# Boutton Parametre PAUSE #------------------------------------#
        self.__buttonParametrePAUSE = Button(self.__main, image=img4, fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelPAUSE, self.__buttonBackPAUSE, self.__buttonParametrePAUSE, self.__buttonRelancer, self.__buttonSaveGame, self.__buttonQuitter], [self.__labelParametrePAUSE, self.__buttonBackParametrePAUSE], [self.__labelParametrePAUSEConfig, self.__buttonBackParametrePAUSEConfig]),  highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonParametrePAUSEConfig = [1300, 60]
        
        
        #------------------------------------# Boutton Relancer #------------------------------------#
        reimg = tkinter.PhotoImage(file = "assets/button_relancer.png")
        self.__buttonRelancer = Button(self.__main, image=reimg , fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.nouvPartie())
        self.__buttonRelancerConfig = [720, 400]
        
        
        #------------------------------------# Boutton Save Game #------------------------------------#
        savimg = tkinter.PhotoImage(file = "assets/button_sauvegarder-et-quitter.png")
        self.__buttonSaveGame = Button(self.__main, image=savimg , fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelPAUSE, self.__buttonBackPAUSE, self.__buttonParametrePAUSE, self.__buttonRelancer, self.__buttonSaveGame, self.__buttonQuitter], [self.__labelKamon, self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonParametreKamon, self.__buttonQuitterGame], [self.__labelKamonConfig, self.__button1vs1Config, self.__button1vsIAConfig, self.__button1vs1onlineConfig, self.__buttonParametreKamonConfig, self.__buttonQuitterGameConfig]),  highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonSaveGameConfig = [720, 500]
        
        
        #------------------------------------# Boutton Quitter #------------------------------------#
        quitimg = tkinter.PhotoImage(file = "assets/button_quitter.png")
        self.__buttonQuitter = Button(self.__main, image = quitimg, fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelPAUSE, self.__buttonBackPAUSE, self.__buttonParametrePAUSE, self.__buttonRelancer, self.__buttonSaveGame, self.__buttonQuitter], [self.__labelKamon, self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonParametreKamon, self.__buttonQuitterGame], [self.__labelKamonConfig, self.__button1vs1Config, self.__button1vsIAConfig, self.__button1vs1onlineConfig, self.__buttonParametreKamonConfig, self.__buttonQuitterGameConfig]),  highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonQuitterConfig = [720, 600]
        
        
        #------------------------------------# Label Parametre PAUSE #------------------------------------#
        self.__labelParametrePAUSE = Label(self.__main, image=img4, fg=self.__fgcouleur, bg=self.__bgcouleur, highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__labelParametrePAUSEConfig = [720, 100]
        
        
        #------------------------------------# Boutton Retour Parametre PAUSE #------------------------------------#
        self.__buttonBackParametrePAUSE = Button(self.__main, text='Back', font=("Helvetica", 24, "bold"), fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelParametrePAUSE, self.__buttonBackParametrePAUSE], [self.__labelPAUSE, self.__buttonBackPAUSE, self.__buttonParametrePAUSE, self.__buttonRelancer, self.__buttonSaveGame, self.__buttonQuitter], [self.__labelPAUSEConfig, self.__buttonBackPAUSEConfig, self.__buttonParametrePAUSEConfig, self.__buttonRelancerConfig, self.__buttonSaveGameConfig, self.__buttonQuitterConfig]),  highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonBackParametrePAUSEConfig = [100, 100]
        
        
        #------------------------------------# Label Parametre Menu #------------------------------------#
        self.__labelParametreMenu = Label(self.__main, image=img4, fg=self.__fgcouleur, bg=self.__bgcouleur, highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__labelParametreMenuConfig = [720, 100]
        
        
        #------------------------------------ Boutton Retour Parametre Menu #------------------------------------
        self.__buttonBackParametreMenu = Button(self.__main, text='Back', font=("Helvetica", 24, "bold"), fg=self.__fgcouleur, bg=self.__bgcouleur, command=lambda: self.changeDisplay([self.__labelParametreMenu, self.__buttonBackParametreMenu], [self.__labelKamon, self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonParametreKamon, self.__buttonQuitterGame], [self.__labelKamonConfig, self.__button1vs1Config, self.__button1vsIAConfig, self.__button1vs1onlineConfig, self.__buttonParametreKamonConfig, self.__buttonQuitterGameConfig]),  highlightthickness=self.__bdSize, highlightbackground=self.__bdcouleur)
        self.__buttonBackParametreMenuConfig = [100, 100]

        self.__couleurPlateau = "black"
        self.__bgCase = "#D16928"
        self.__couleurPlayer1 = "white"
        self.__couleurPlayer2 = "black"
        
        self.__main.mainloop()

    
    #------------------------------------  Musique ------------------------------------ #

    def play(self):
        pygame.mixer.music.play(-1)
        
    def paused(self):
        #------------------------------------###
        pygame.mixer.music.pause()
        #------------------------------------####
    def unpause(self):
        global pause
        pygame.mixer.music.unpause()
        pause = False 
    
    #------------------------------------   Changer la taille d'une image ------------------------------------ # 

    def image(self, image, width, height):
        file = Image.open(image)
        file = file.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(file)
    
    #------------------------------------   Changer de fenetre dans le menu ------------------------------------ #
    
    def changeDisplay(self, listSupp, listAdd, listConfig):
        for i in range(len(listSupp)):
            listSupp[i].place_forget()
        for j in range(len(listAdd)):
            listAdd[j].place(x=listConfig[j][0], y=listConfig[j][1], anchor="center")
                
    #------------------------------------  Récupère les codes ------------------------------------ #

         
    # Code pour rejoindre       
    def getJoinText(self):
        self.__joinCode = self.__joinEntryArea.get()
        self.__joinEntryArea.get() == '192.168.31.183'
        
    #------------------------------------ Game 1vs1  ------------------------------------ #
        
    def startGame(self, PlateauSize, rayon):
        turn = Game(self.__canvasPlateau, self.__canvasPlateauConfig, PlateauSize, rayon, self.__samuraiTheme[2], self.__samuraiTheme[1], self.__couleurPlateau, self.__couleurPlayer1, self.__couleurPlayer2, self.__bgCase)
        turn.AffichagePlateau()
        
    #------------------------------------ Game 1vsIA  ------------------------------------ #
        
    def startGameIA(self, PlateauSize, rayon):
        turn = GameIA(self.__canvasPlateau, self.__canvasPlateauConfig, PlateauSize, rayon, self.__samuraiTheme[2], self.__samuraiTheme[1], self.__couleurPlateau, self.__couleurPlayer1, self.__couleurPlayer2, self.__bgCase)
        turn.AffichagePlateau()
        
    #------------------------------------ Game 1vs1 Online  ------------------------------------ #
    def startGameOnline(self, PlateauSize, rayon):
        turn = GameOnline(self.__canvasPlateau, self.__canvasPlateauConfig, PlateauSize, rayon, self.__samuraiTheme[2], self.__samuraiTheme[1], self.__couleurPlateau, self.__couleurPlayer1, self.__couleurPlayer2, self.__bgCase)
        turn.AffichagePlateau()
        
    #------------------------------------   Relancer une partie ------------------------------------ #
    def nouvPartie(self):
        self.__main.destroy()
        Menu()
        
    #------------------------------------ Theme  ------------------------------------ #
    
    def Theme(self, theme):
        self.__samuraiTheme = theme

#IP
def getJoinText():
    return '192.168.31.183'  

Menu()