from winsound import Beep
import time

class parlante():
    #Constructor
    def __init__(self,color,marca, status):
        self.colorParlante= color
        self.marcaP = marca
        self.isEncendido = status
    #Propiedades
    material = "plastico"
    estado = False
    

   #Metodos||Acciones

    def __TocarMusica1(self):
     
       #Beep(frequency, duration) Frequency in Hertz, duration in ms
       ###################################################
       # Mario Bros Theme ( Beep Music )##################
       # Address: https://www.autoitscript.com/forum/topic/40848-beep-music-mario-bros-theme/
       ###################################################
       ###################### by J0keR  ##################
       ###################################################
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
        
    def Encender(self,estado):
        if estado == True:
            print("Encendiendo Parlante")
            for i in range (5):
                time.sleep(0.5)
                print("....")
                print("Parlante encendido.\nBienvenido!.")
                break
            self.isEncendido = True
            self.__TocarMusica1()
            return 1

        else:
            print("Parlante apagado")

ParlanteJBL = parlante("Rojo","JBL",True)


ParlanteJBL.Encender(True)


