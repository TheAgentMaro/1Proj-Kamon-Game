from Plateau import Plateau
from Connection import Network
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import math
from math import *
from random import *

class GameOnline:
    
    
    def __init__(self, canvas, canvasConfig, PlateauSize, rayon, listlogos, listColor, colorPlateau, colorPlayer1, colorPlayer2, bgCase):
        
        self.__canvasPlateau = canvas
        self.__canvasPlateau.bind('<Button-1>', self.Tours)
        
        self.__bgCase = bgCase
        self.__rayon = rayon
        self.__borderdWidth = 10
        self.__Plateau = Plateau(rayon, PlateauSize, canvasConfig[0], canvasConfig[1], listlogos, listColor)
        self.__dic = self.__Plateau.getDic()
        self.__ring = self.__Plateau.getRing()
        self.__colorPlateau = colorPlateau
        self.__lastHit = ()
        
        
        self.__player1 = 1
        self.__player2 = 2
        self.__colorPlayer1 = colorPlayer1
        self.__colorPlayer2 = colorPlayer2
        self.__player = self.__player1
        self.__colorPlayer = self.__colorPlayer1
        
        self.player1total = 0
        self.player2total = 0

        self.__up_orange1 = [(1,-3,2)]
        self.__up_orange2 = [(2,-3,1)]
        
        self.__down_orange1 = [(-1,3,-2)]
        self.__down_orange2 = [(-2,3,-1)]
        
        self.__up_blue1 = [(-1,-2,3)]
        self.__up_blue2 = [(-2,-1,3)]
        
        self.__down_blue1 = [(1,2,-3)]
        self.__down_blue2 = [(2,1,-3)]
        
        self.__gauche_vert1 = [(3,-2,-1)]
        self.__gauche_vert2 = [(3,-1,-2)]
        
        self.__droite_vert1 = [(-3,1,2)]
        self.__droite_vert2 = [(-3,2,1)]
        
        self._player1detect =[]
        self._player2detect =[]
        
        #connection réseau
        self.net = Network()
    
    def Tours(self, event):
        """
        Role : Tours de je un par un 

        :param event: position du souris 
        """ 
        key = self.where(event.x, event.y)
        if key != "no":
            value = self.__dic[key]
            if self.premierCoup(key, self.__ring):
                self.put(value) #value = [(951.5, 249.9481317257946), (<PIL.ImageTk.PhotoImage object at 0x00000189675F12D0>, 'red'), 'black']
                self.changePlayer()
                if value[2] == 'white':
                    self.player1total = self.player1total + 1
                    self._player1detect.append(key)
                    print('WHITE Player list :' , self._player1detect)
                if value[2] == 'black':
                    self.player2total = self.player2total + 1
                    self._player2detect.append(key)
                    print('BLACK Player list :' , self._player2detect)
                print('Joueur White Totale Pion Posé :', self.player1total,'Joueur Black Totale Pion Posé :', self.player2total)
                if self.player2total == 18 and self.player2total == 18:
                    showinfo('Match Nul !!', 'Félicitations à vous deux !')
                self.checkbord()


            
    

    
    def premierCoup(self, key, ring):
        if self.__lastHit == ():
            return ((key[0] == ring or key[0] == -ring) and (key[1] != ring or key[1] != -ring) and (key[2] != ring or key[2] != -ring)) ^ ((key[1] == ring or key[1] == -ring) and (key[2] != ring or key[2] != -ring) and (key[0] != ring or key[0] != -ring)) ^ ((key[2] == ring or key[2] == -ring) and (key[1] != ring or key[1] != -ring) and (key[0] != ring or key[0] != -ring))
        if self.__lastHit != ():
            return self.possible(key)
             
        
    #------------------------------------   
    # Possible ?
    #------------------------------------ 
    
    def possible(self, key):
        value = self.__dic[key]
        if value[1][0] != "":
            if value[2] == "vide":
                if self.__lastHit == () or self.__lastHit[0] == value[1][0] or self.__lastHit[1] == value[1][1]:
                    return True
                elif self.__lastHit != () and self.__lastHit[0] != value[1][0] or self.__lastHit[1] != value[1][1]:
                    #return self.winner()
                    pass
        return False

                
    def where(self, x, y):
        for value in self.__dic.values():
            if math.sqrt((value[0][0] - x)*(value[0][0] - x) + (value[0][1] - y)*(value[0][1] - y)) < self.__Plateau.getHeight()/2:
                key = self.getKey(value)
                return key
        return "no"
    
    #------------------------------------   
    # Trouve la clé avec sa valeur
    #------------------------------------ 
    
    def getKey(self, val):

        for key, value in self.__dic.items():
            if val == value:

                print(key)
                return key #(q , r , s)
     
    #------------------------------------   
    # Ajoute un pion et enregistre le coup
    #------------------------------------  
           
    def put(self, value):

        value[2] = self.__colorPlayer

        
        self.__lastHit = (value[1][0], value[1][1]) #logo , coleur
        
        listCoordCorner = self.__Plateau.generateCoordCorner(value[0][0], value[0][1], self.__rayon*0.9)
        
        listCoordCircle = self.__Plateau.generateCoordCircle(value[0][0], value[0][1], self.__rayon*1.2)
        #polygon
        self.__canvasPlateau.create_polygon(listCoordCorner, fill="", outline=self.__colorPlayer, width=0.2*self.__rayon)
        
        #cercle
        self.__canvasPlateau.create_oval(listCoordCircle, fill="", outline=self.__colorPlayer, width=0.3*self.__rayon)
        
    #------------------------------------   
    # Changement de joueur
    #------------------------------------  
        
    def changePlayer(self):

        if self.__player == self.__player1:
            self.__player = self.__player2
            self.__colorPlayer = self.__colorPlayer2
        else:
            self.__player = self.__player1
            self.__colorPlayer = self.__colorPlayer1
            self.__player1, self.__player2 = self.parse_data(self.send_data())
    
    def winner(self):
                if self.player1total > self.player2total :
                        showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                elif self.player1total == self.player2total :
                        showinfo('Match Nul !!', 'Félicitations à vous deux !')
                elif self.player1total < self.player2total :
                        showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')

                
    def checkbord(self):
        
        for vert in self.__droite_vert1:
            for vert2 in self.__droite_vert2:
                    for vert3 in self.__gauche_vert1:
                        for vert4 in self.__gauche_vert2:
                            if vert in self._player1detect and vert3 in self._player1detect and len(self._player1detect) >= 7 :
                                print("Jonction entre deux bord Vert Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                                
                            elif vert in self._player2detect and vert3 in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif vert2 in self._player1detect and vert3  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif vert2 in self._player2detect and vert3  in self._player2detect and len(self._player2detect) >= 7   :
                                print("Jonction entre deux bord Vert Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif  vert in self._player1detect and vert4 in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif vert in self._player2detect and vert4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif vert2 in self._player1detect and vert4  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif vert2 in self._player2detect and vert4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
        for oran in self.__up_orange1:
            for oran2 in self.__up_orange2:
                    for oran3 in self.__down_orange1:
                        for oran4 in self.__down_orange2:
                            if oran in self._player1detect and oran3 in self._player1detect  and len(self._player1detect) >= 7 :
                                print("Jonction entre deux bord Orange Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                                
                            elif oran in self._player2detect and oran3 in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif oran2 in self._player1detect and oran3  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif oran2 in self._player2detect and oran3  in self._player2detect and len(self._player2detect) >= 7   :
                                print("Jonction entre deux bord Orange Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif  oran in self._player1detect and oran4 in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif oran in self._player2detect and oran4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif oran2 in self._player1detect and oran4  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif oran2 in self._player2detect and oran4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
        for blue in self.__up_blue1:
                for blue2 in self.__up_blue2:
                    for blue3 in self.__down_blue1:
                        for blue4 in self.__down_blue2:
                            if blue in self._player1detect and blue3 in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                                
                            elif blue in self._player2detect and blue3 in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif blue2 in self._player1detect and blue3  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif blue2 in self._player2detect and blue3  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif  blue in self._player1detect and blue4 in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif blue in self._player2detect and blue4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif blue2 in self._player1detect and blue4  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif blue2 in self._player2detect and blue4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')

#------------------------------------  Connection Data ------------------------------------ #
     
    def send_data(self):
        """
        Send position to server
        :return: None
        """
        data = str(self.net.id) + ":" + str(self.__player) + "," + str(self.__player)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0,0


    
    def AffichagePlateau(self):
        self.__canvasPlateau.delete(ALL)
        for value in self.__dic.values():
            listCoordCorner = self.__Plateau.generateCoordCorner(value[0][0], value[0][1], self.__rayon)
            listCoordCircle = self.__Plateau.generateCoordCircle(value[0][0], value[0][1], self.__rayon)
            self.__canvasPlateau.create_polygon(listCoordCorner, fill=self.__bgCase, outline=self.__colorPlateau, width=self.__borderdWidth)
            self.__canvasPlateau.create_oval(listCoordCircle, fill=value[1][1], width=0)
            self.__canvasPlateau.create_image(value[0][0], value[0][1], image=value[1][0])
            self.__canvasPlateau.create_polygon(listCoordCorner, fill="", outline=self.__colorPlateau, width=self.__borderdWidth, activeoutline="yellow")
            self.__canvasPlateau.create_line(1250, 300, 650, 0,width=10, fill="#fc870c")
            self.__canvasPlateau.create_line(180,0,180,1200,width=10, fill="#619456")
            self.__canvasPlateau.create_line(1030,0,1030,1200,width=10, fill="#619456")
            self.__canvasPlateau.create_line(0,645,1200,1200,width=10, fill="#fc870c")
            self.__canvasPlateau.create_line(0,300,560,0,width=10, fill="#616CA3") 
            self.__canvasPlateau.create_line(1700,400,560,945,width=10, fill="#616CA3")
        self.__canvasPlateau.update()



    


