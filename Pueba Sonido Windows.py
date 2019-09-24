from winsound import Beep
import time



class parlante():
    #Constructor
    def __init__(self,color,marca, status,nivel,Vnivel):
        self.colorParlante= color
        self.marcaP = marca
        self.isEncendido = status
        self.bateria = nivel
        self.volumen = Vnivel
    #Propiedades
    material = "plastico"
    estado = False
    

   #Metodos||Acciones:
##############---- MUSICA SISTEMA ----------------#############

    def __MusicEncendido(self):
        Beep(500,200)
        Beep(800,200)

    def __MusicApagado(self):
        Beep(200,100)
        Beep(700,200)

##################------CANCIONES-------##########################

    
    def __TocarMusica1(self):
       ###################################################
       # Mario Bros Theme ( Beep Music )##################
       # Address: https://www.autoitscript.com/forum/topic/40848-Beep-music-mario-bros-theme/
        Beep(480,200)
        Beep(1568,200)
        Beep(1568,200)
        Beep(1568,200)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(784,200)
        Beep(370,200)
        Beep(392,200)
        Beep(370,200)
        Beep(392,200)
        Beep(392,400)
        Beep(196,400)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(740,200)
        Beep(84,200)
        Beep(880,200)
        Beep(831,200)
        Beep(880,200)
        Beep(988,400)
        Beep(880,200)
        Beep(784,200)
        Beep(699,200)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(740,200)
        Beep(784,200)
        Beep(880,200)
        Beep(830,200)
        Beep(880,200)
        Beep(988,400)
        time.sleep(200/1000)
        Beep(1108,10)
        Beep(1174,200)
        Beep(1480,10)
        Beep(1568,200)
        time.sleep(200/1000)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(740,200)
        Beep(784,200)
        Beep(784,200)
        Beep(740,200)
        Beep(784,200)
        Beep(880,200)
        Beep(830,200)
        Beep(880,200)
        Beep(988,400)
        Beep(880,200)
        Beep(784,200)
        Beep(699,200)
        Beep(659,200)
        Beep(699,200)
        Beep(784,200)
        Beep(880,400)
        Beep(784,200)
        Beep(699,200)
        Beep(659,200)
        Beep(587,200)
        Beep(659,200)
        Beep(699,200)
        Beep(784,400)
        Beep(699,200)
        Beep(659,200)
        Beep(587,200)
        Beep(523,200)
        Beep(587,200)
        Beep(659,200)
        Beep(699,400)
        Beep(659,200)
        Beep(587,200)
        Beep(494,200)
        Beep(523,200)
        time.sleep(400/1000)
        Beep(349,400)
        Beep(392,200)
        Beep(330,200)
        Beep(523,200)
        Beep(494,200)
        Beep(466,200)
        Beep(440,200)
        Beep(494,200)
        Beep(523,200)
        Beep(880,200)
        Beep(494,200)
        Beep(880,200)
        Beep(1760,200)
        Beep(440,200)
        Beep(392,200)
        Beep(440,200)
        Beep(494,200)
        Beep(784,200)
        Beep(440, 200)
        Beep(784,200)
        Beep(1568,200)
        Beep(392,200)
        Beep(349,200)
        Beep(392,200)
        Beep(440,200)
        Beep(699,200)
        Beep(415,200)
        Beep(699,200)
        Beep(1397,200)
        Beep(349,200)
        Beep(330,200)
        Beep(311,200)
        Beep(330,200)
        Beep(659,200)
        Beep(699,400)
        Beep(784,400)
        Beep(440,200)
        Beep(494,200)
        Beep(523,200)
        Beep(880,200)
        Beep(494,200)
        Beep(880,200)
        Beep(1760,200)
        Beep(440,200)
        Beep(392,200)
        Beep(440,200)
        Beep(494,200)
        Beep(784,200)
        Beep(440,200)
        Beep(784,200)
        Beep(1568,200)
        Beep(392,200)
        Beep(349,200)
        Beep(392,200)
        Beep(440,200)
        Beep(699,200)
        Beep(659,200)
        Beep(699,200)
        Beep(740,200)
        Beep(784,200)
        Beep(392,200)
        Beep(392,200)
        Beep(392,200)
        Beep(392,200)
        Beep(196,200)
        Beep(196,200)
        Beep(196,200)
        Beep(185,200)
        Beep(196,200)
        Beep(185,200)
        Beep(196,200)
        Beep(208,200)
        Beep(220,200)
        Beep(233,200)
        Beep(247,200)
        print("song finished")
    
    def __TocarMusica2(self):
        #Beep(frequency, duration) Frequency in Hertz, duration in ms
        # Composer: Akash Agrawal
        # Address: https://hashtagakash.wordpress.com/2014/01/22/182/
        Beep(659, 125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(523, 125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(784, 125)
        time.sleep(0.375)
        Beep(392, 125)
        time.sleep(0.375)
        Beep(523, 125)
        time.sleep(0.250)
        Beep(392, 125)
        time.sleep(0.250)
        Beep(330, 125)
        time.sleep(0.250)
        Beep(440, 125)
        time.sleep(0.125)
        Beep(494, 125)
        time.sleep(0.125)
        Beep(466, 125)
        time.sleep(0.42)
        Beep(440, 125)
        time.sleep(0.125)
        Beep(392, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(784, 125)
        time.sleep(0.125)
        Beep(880, 125)
        time.sleep(0.125)
        Beep(698, 125)
        Beep(784, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(587, 125)
        Beep(494, 125)
        time.sleep(0.125)
        Beep(523, 125)
        time.sleep(0.250)
        Beep(392, 125)
        time.sleep(0.250)
        Beep(330, 125)
        time.sleep(0.250)
        Beep(440, 125)
        time.sleep(0.125)
        Beep(494, 125)
        time.sleep(0.125)
        Beep(466, 125)
        time.sleep(0.42)
        Beep(440, 125)
        time.sleep(0.125)
        Beep(392, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(784, 125)
        time.sleep(0.125)
        Beep(880, 125)
        time.sleep(0.125)
        Beep(698, 125)
        Beep(784, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(587, 125)
        Beep(494, 125)
        time.sleep(0.375)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(415, 125)
        Beep(440, 125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(440, 125)
        Beep(523, 125)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(698, 125)
        time.sleep(0.125)
        Beep(698, 125)
        Beep(698, 125)
        time.sleep(0.625)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(415, 125)
        Beep(440, 125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(440, 125)
        Beep(523, 125)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(622, 125)
        time.sleep(0.250)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(523, 125)
        time.sleep(0.1125)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(415, 125)
        Beep(440, 125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(440, 125)
        Beep(523, 125)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(698, 125)
        time.sleep(0.125)
        Beep(698, 125)
        Beep(698, 125)
        time.sleep(0.625)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(415, 125)
        Beep(440, 125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(440, 125)
        Beep(523, 125)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(622, 125)
        time.sleep(0.250)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(523, 125)
        print("Song finished")
        
    def __TocarMusica3(self):
        Beep (659, 120)  #  Treble E
        time.sleep(0.120)
        Beep (622,120)  #  Treble D#
        time.sleep(0.120)

        Beep (659, 120)  #  Treble E
        time.sleep(0.120)
        Beep (622, 120)  #  Treble D#
        time.sleep(0.120)
        Beep (659, 120)  #  Treble E
        time.sleep(0.120)
        Beep (494, 120)  #  Treble B
        time.sleep(0.120)
        Beep (587, 120)  #  Treble D
        time.sleep(0.120)
        Beep (523, 120)  #  Treble C
        time.sleep(0.120)

        Beep (440, 120)  #  Treble A
        time.sleep(0.140)
        Beep (262, 120)  #  Middle C
        time.sleep(0.120)
        Beep (330, 120)  #  Treble E
        time.sleep(0.120)
        Beep (440, 120)  #  Treble A
        time.sleep(0.120)

        Beep (494, 120)  #  Treble B
        time.sleep(0.140)
        Beep (330, 120)  #  Treble E
        time.sleep(0.120)
        Beep (415, 120)  #  Treble G#
        time.sleep(0.120)
        Beep (494, 120)  #  Treble B
        time.sleep(0.120)

        Beep (523, 120)  #  Treble C
        time.sleep(0.140)
        Beep (330, 120)  #  Treble E
        time.sleep(0.120)
        Beep (659, 120)  #  Treble E
        time.sleep(0.120)
        Beep (622, 120)  #  Treble D#
        time.sleep(0.120)

        Beep (659, 120)  #  Treble E
        time.sleep(0.120)
        Beep (622, 120)  #  Treble D#
        time.sleep(0.120)
        Beep (659, 120)  #  Treble E
        time.sleep(0.120)
        Beep (494, 120)  #  Treble B
        time.sleep(0.120)
        Beep (587, 120)  #  Treble D
        time.sleep(0.120)
        Beep (523, 120)  #  Treble C
        time.sleep(0.120)

        Beep (440, 120)  #  Treble A
        time.sleep(0.140)
        Beep (262, 120)  #  Middle C
        time.sleep(0.120)
        Beep (330, 120)  #  Treble E
        time.sleep(0.120)
        Beep (440, 120)  #  Treble A
        time.sleep(0.120)

        Beep (494, 120)  #  Treble B
        time.sleep(0.140)
        Beep (330, 120)  #  Treble E
        time.sleep(0.120)        
        Beep (523, 120)  #  Treble C
        time.sleep(0.120)
        Beep (494, 120)  #  Treble B
        time.sleep(0.140)
        Beep (440, 120)  #  Treble A

    def __TocarMusica4(self):
        Beep (300, 500)
        time.sleep(0.1) 
        Beep (300, 500)
        time.sleep(0.1)
        Beep (300, 500)
        time.sleep(0.10)
        Beep (250, 500)
        time.sleep(0.10)
        Beep (350, 250)
        Beep (300, 500)
        time.sleep(0.10)
        Beep (250, 500)
        time.sleep(0.10)
        Beep (350, 250)
        Beep (300, 500)
        time.sleep(0.10)

    def __TocarMusica5(self):
        Beep(658, 125) 
        Beep(1320, 500) 
        Beep(990, 250) 
        Beep(1056, 250)
        Beep(1188, 250)
        Beep(1320, 125)
        Beep(1188, 125)
        Beep(1056, 250) 
        Beep(990, 250) 
        Beep(880, 500) 
        Beep(880, 250) 
        Beep(1056, 250) 
        Beep(1320, 500) 
        Beep(1188, 250) 
        Beep(1056, 250) 
        Beep(990, 750) 
        Beep(1056, 250) 
        Beep(1188, 500) 
        Beep(1320, 500) 
        Beep(1056, 500) 
        Beep(880, 500) 
        Beep(880, 500) 
        time.sleep (0.250 )
        Beep(1188, 500) 
        Beep(1408, 250) 
        Beep(1760, 500) 
        Beep(1584, 250) 
        Beep(1408, 250) 
        Beep(1320, 750) 
        Beep(1056, 250) 
        Beep(1320, 500) 
        Beep(1188, 250) 
        Beep(1056, 250) 
        Beep(990, 500) 
        Beep(990, 250) 
        Beep(1056, 250) 
        Beep(1188, 500) 
        Beep(1320, 500) 
        Beep(1056, 500) 
        Beep(880, 500) 
        Beep(880, 500) 
        time.sleep (0.500 )
        Beep(1320, 500)

        Beep(990, 250) 
        Beep(1056, 250) 
        Beep(1188, 250) 
        Beep(1320, 125) 
        Beep(1188, 125) 
        Beep(1056, 250) 
        Beep(990, 250) 
        Beep(880, 500) 
        Beep(880, 250) 
        Beep(1056, 250) 
        Beep(1320, 500) 
        Beep(1188, 250) 
        Beep(1056, 250) 
        Beep(990, 750) 
        Beep(1056, 250) 
        Beep(1188, 500) 
        Beep(1320, 500) 
        Beep(1056, 500) 
        Beep(880, 500) 
        Beep(880, 500) 
        time.sleep( 0.250 )
        Beep(1188, 500)
        Beep(1408, 250) 
        Beep(1760, 500)   
        Beep(1584, 250)    
        Beep(1408, 250)     
        Beep(1320, 750) 
        Beep(1056, 250)
        Beep(1320, 500) 
        Beep(1188, 250) 
        Beep(1056, 250) 
        Beep(990, 500) 
        Beep(990, 250) 
        Beep(1056, 250) 
        Beep(1188, 500) 
        Beep(1320, 500) 
        Beep(1056, 500) 
        Beep(880, 500) 
        Beep(880, 500) 
        time.sleep (0.500)
        Beep(660, 1000) 
        Beep(528, 1000) 
        Beep(594, 1000) 
        Beep(495, 1000) 
        Beep(528, 1000) 
        Beep(440, 1000) 
        Beep(419, 1000) 
        Beep(495, 1000) 
        Beep(660, 1000) 
        Beep(528, 1000) 
        Beep(594, 1000) 
        Beep(495, 1000) 
        Beep(528, 500) 
        Beep(660, 500) 
        Beep(880, 1000) 
        Beep(838, 2000) 
        Beep(660, 1000) 
        Beep(528, 1000) 
        Beep(594, 1000) 
        Beep(495, 1000) 
        Beep(528, 1000) 
        Beep(440, 1000) 
        Beep(419, 1000) 
        Beep(495, 1000) 
        Beep(660, 1000) 
        Beep(528, 1000) 
        Beep(594, 1000) 
        Beep(495, 1000) 
        Beep(528, 500) 
        Beep(660, 500) 
        Beep(880, 1000) 
        Beep(838, 2000)

 
#################----BASICOS----#########################

    def Encender(self,estado):
        if estado == True:
            print("Encendiendo Parlante")
            for i in range (5):
                time.sleep(0.5)
                print("....")
                print("Parlante encendido.\nBienvenido!.")
                break
            self.isEncendido = True
            self.__MusicEncendido()
            self.MostrarMenu()
            return 1
    
    def Apagar(self,estado):
            print("")
            print("Apagando Parlante")
            for i in range (5):
                time.sleep(0.5)
                print("....")
                print("Parlante Apagado.\nAdios.")
                break
            self.__MusicApagado()

    def VerBateria(self,nivel):
        print(self.bateria,"%")
    
    def VerVolumen(self):
        print(self.volumen)

    def play(self, arg1, arg2, arg3):
        print("Reproduciendo audio:")
        Beep(arg1, arg2)
        time.sleep(arg3)
        print("Fin audio:")

    def PlayMusic(self):
        try:
            print("Reproduciendo audio:")
            
        except: 
            KeyboardInterrupt 
            e = input("press enter:")
    
    def StopMusic(self,stop):
        if PlayMusic == True:
            miSong

    def ChangeSong(self):
        pass

    def __Menu(self):
        pass
        '''
        print("\nElige una opcion:\n1)Tocar cancion\n2)Detener\n3)Cambiar cancion\n4)Apagar Parlante")
        
        f = int(input("Cual Opcion eliges?:"))

        while f > 0 and f< 5:
            if f == 1:
                #self.play()
                self.MostrarMenu()
            elif f == 2:
                self.StopMusic()
                self.MostrarMenu
            elif f == 3:
                self.ChangeSong()
                self.MostrarMenu()
            elif f == 4:
                self.Apagar(True)
                break
        '''


    def MostrarMenu(self):
        self.__Menu()


#ParlanteJBL = parlante("Rojo","JBL",True,100,50)

#ParlanteJBL.Encender(True)
#ParlanteJBL.MostrarMenu()

QSC = parlante("Rojo","QSC",True,100,50)
QSC.Encender(True)  


miSong =  [[300,500, 1], [300,300, 0.1], [300,300, 2], [100,500, 0.1], [200,600, 1 ]]
miSong2 = [300,500, 0.1]
miSong3 = [300,500, 0.1]
'''
QSC.play(miSong)
'''



def desconcatenar(lista):
    a1,a2,a3 = lista
    
    QSC.play(a1,a2,a3)

def partirCadena(lista):
    for elemento in lista:
        
        desconcatenar(elemento)




qsc.REPRODUCIR(miSong)
