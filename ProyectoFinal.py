import os
from sense_hat import *
from time import sleep 
from random import randint

    



sense = SenseHat()
sense.clear()
vidas = 3
puntaje1, puntaje2, puntaje3,encontradas = 0,0,0,0
puntajeW1,puntajeW2,puntajeW3 = 5,3,2
#olvidelo

R = [255, 0, 0]  # red
Y = [255, 255, 0]  # yellow
G = [0, 255, 0]  # green
W = [255, 255, 255]  # white
B = [0, 0, 255]  # Blue
O = [0, 0, 0]  # Black
N = [250, 20,0] #Naranja

# Emojis
Skull1_logo = [
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, B, W, W, B, W, O,
    O, W, W, W, W, W, W, O,
    O, O, W, Y, Y, W, O, O,
    O, O, W, W, W, W, O, O,
]

Skull2_logo = [
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, B, W, W, O, W, O,
    O, W, W, W, W, W, W, O,
    O, O, W, Y, Y, W, O, O,
    O, O, W, W, W, W, O, O, ]

Skull3_logo = [
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, B, W, W, B, W, O,
    O, W, W, W, W, W, W, O,
    O, O, W, Y, Y, W, O, O,
    O, O, W, W, W, W, O, O, ]

Skull21_logo = [
    O, O, O, O, O, O, O, O,
    O, O, Y, Y, Y, Y, O, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, B, Y, Y, B, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, O, Y, B, B, Y, O, O,
    O, O, Y, Y, Y, Y, O, O,
]

Skull22_logo = [
    O, O, O, O, O, O, O, O,
    O, O, Y, Y, Y, Y, O, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, B, Y, Y, O, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, O, Y, B, B, Y, O, O,
    O, O, Y, Y, Y, Y, O, O, ]

Skull23_logo = [
    O, O, O, O, O, O, O, O,
    O, O, Y, Y, Y, Y, O, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, B, Y, Y, B, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, O, Y, B, B, Y, O, O,
    O, O, Y, Y, Y, Y, O, O, ]

Skull31_logo = [
    R, O, O, O, O, O, O, R,
    R, O, R, R, R, R, O, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, R, W, R, R, W, R, O,
    O, R, R, R, R, R, R, O,
    O, O, R, W, W, R, O, O,
    O, O, R, R, R, R, O, O,
]


number3 = [
    O, O, W, W, W, W, W, O,
    O, O, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, O, W, W, W, W, W, O,
    O, O, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, O, W, W, W, W, W, O,
    O, O, W, W, W, W, W, O, ]

number2 = [
    O, O, W, W, W, W, W, O,
    O, O, W, W, W, W, W, O,
    O, O, O, O, O, W, W, O,
    O, O, W, W, W, W, W, O,
    O, O, W, W, W, W, W, O,
    O, O, W, W, O, O, O, O,
    O, O, W, W, W, W, W, O,
    O, O, W, W, W, W, W, O, ]

number1 = [
    O, O, O, W, W, W, O, O,
    O, O, O, W, W, W, O, O,
    O, O, O, O, W, W, O, O,
    O, O, O, O, W, W, O, O,
    O, O, O, O, W, W, O, O,
    O, O, O, O, W, W, O, O,
    O, O, O, O, W, W, O, O,
    O, O, O, W, W, W, W, O, ]

# Codigo jostick

def wait_for_move():
    while True:
        e = sense.stick.wait_for_event()
        if e.action != ACTION_RELEASED:
            return e

# Codigo Introduccion

def intro():
    print("")
    print("░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░")
    print("░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░   Bienvenido a  ")
    print("░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░ -Encuentra la Moneda-")
    print("░░░░░░▐▌░░░░▀▀███████▀")
    print("▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒")
    sleep(2)
    os.system("cls")
    print("Encuentra las  monedas amarillas,\nSi fallas reiniciaras desde cero")
    sleep(4)
    os.system("cls")


# Codigo introNivel1


def intro1():
    sense.set_pixels(Skull1_logo)
    sleep(.5)
    sense.set_pixels(Skull2_logo)
    sleep(.5)
    sense.set_pixels(Skull3_logo)
    sleep(.5)
    sense.clear(O)
    sense.show_message("LVL 1", text_colour=W)
    # scroll_speed=0.01
    sense.set_pixels(number3)
    sleep(1)
    sense.set_pixels(number2)
    sleep(1)
    sense.set_pixels(number1)
    sleep(1)
    sense.clear(O)

# codigo introNivel2


def intro2():
    sense.show_message("LVL 2", text_colour=Y)
    sense.set_pixels(Skull21_logo)
    sleep(1)
    sense.set_pixels(Skull22_logo)
    sleep(.5)
    sense.set_pixels(Skull23_logo)
    sleep(.5)
    sense.set_pixels(number3)
    sleep(.5)
    sense.set_pixels(number2)
    sleep(.5)
    sense.set_pixels(number1)
    sleep(.5)
    sense.clear(O)

# codigo IntroNivel3


def intro3():
    sense.show_message("LVL 3", text_colour=R, scroll_speed=0.1)
    sense.set_pixels(Skull31_logo)
    sleep(2)
    sense.set_pixels(number3)
    sleep(.2)
    sense.set_pixels(number2)
    sleep(.2)
    sense.set_pixels(number1)
    sleep(.2)
    sense.clear(O)

# Codigo Mensaje Ganador


def win():
    print("██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗")
    print("╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║")
    print("░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║")
    print("░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║")
    print("░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║")
    print("░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝")
    sense.clear(Y)
    sleep(.2)
    sense.clear(B)
    sleep(.2)
    sense.clear(G)
    sleep(2)
    sense.clear(Y)
    sleep(.2)


def Lose():
    sense.clear(R)
    sleep(2)
    print("  ░█──░█ ░█▀▀▀█ ░█─░█ 　 ░█─── ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀  ")
    print("  ░█▄▄▄█ ░█──░█ ░█─░█ 　 ░█─── ░█──░█ ─▀▀▀▄▄ ░█▀▀▀ ")
    print("  ──░█── ░█▄▄▄█ ─▀▄▄▀ 　 ░█▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄")
    sleep(2)
    os.system("cls")


def Vida_Menos():
    global vidas
    if vidas == 0:
        Lose()
    else:
        vidas -= 1


def Nivel1():
    # Puntajes nivel 1
    global encontradas
    global puntaje1
    global puntajeW1
    puntajeM1 = 5
    intro1()
    print("Monedas a encontrar"+ "-->" + str(puntajeM1))

    # Nivel 1
    for turno in range(puntajeW1):

        coinx = randint(0, 7)
        coiny = randint(0, 7)
        # print(coinx,coiny)

        # Escondiendo moneda
        sense.set_pixel(coinx, coiny, Y)
        sleep(1)
        sense.clear(Y)
        sleep(1)
        sense.clear()

        # coordenadas del jugador
        x = randint(0, 7)
        y = randint(0, 7)
        sense.set_pixel(x, y, W)
        for moneda in range(1):   
              
            while True:  
                e = wait_for_move()

                if e.direction == DIRECTION_MIDDLE:

                    if x == coinx and y == coiny:
                        sense.set_pixel(x, y, G)
                        encontradas += 1
                    else:
                        sense.set_pixel(x, y, R)

                    sleep(1)
                    sense.clear()
                    break
                sense.clear()

                if e.direction == DIRECTION_UP and y > 0:
                    y = y - 1
                elif e.direction == DIRECTION_DOWN and y < 7:
                    y = y + 1
                elif e.direction == DIRECTION_LEFT and x > 0:
                    x = x - 1
                elif e.direction == DIRECTION_RIGHT and x < 7:
                    x = x + 1
                sense.set_pixel(x, y, W)
            
        if encontradas >= 1:
            puntaje1 += 1
            puntajeM1-= 1
            print("Monedas a encontrar"+ "-->" + str(puntajeM1))

    if puntaje1 == puntajeW1:
        Nivel2()
    else:
        Lose()
        sense.show_message(
            "Score" + "" + str(puntaje3 + puntaje2 + puntaje1))


def Nivel2():
    global puntaje2
    global puntajeW2 
    puntajeM2 = 3
    
    
    
    #dejelo de uno para las pruebas
    intro2()
    print("\nMonedas a encontrar"+ "-->" + str(puntajeM2))
    # Inicia nivel 2

    for turno in range(puntajeW2):
        global encontradas 
        # Moneda 1
        coinx = randint(0, 7)
        coiny = randint(0, 7)

        # Moneda 2
        coinx2 = randint(0, 7)
        coiny2 = randint(0, 7)

        # Escondiendo moneda
        sense.set_pixel(coinx, coiny, Y)
        sense.set_pixel(coinx2, coiny2, Y)
        sleep(.5)
        sense.clear(Y)
        sleep(1)
        sense.clear()

        # coordenadas del jugador
        x = randint(0, 7)
        y = randint(0, 7)
        sense.set_pixel(x, y, W)

        for moneda in range(2):     #ahi quedaria adentro
              #el range(2) hace 0,1,2 o 1,2 ? o 0,1
            while True:  #
                e = wait_for_move()

                if e.direction == DIRECTION_MIDDLE:

                    if x == coinx and y == coiny:
                        sense.set_pixel(x, y, G)
                        encontradas += 1
                    elif x == coinx2 and y == coiny2:
                        sense.set_pixel(x, y, G)
                        encontradas += 1
                    else:
                        sense.set_pixel(x, y, R)

                    sleep(1)
                    sense.clear()
                    break
                sense.clear()

                if e.direction == DIRECTION_UP and y > 0:
                    y = y - 1
                elif e.direction == DIRECTION_DOWN and y < 7:
                    y = y + 1
                elif e.direction == DIRECTION_LEFT and x > 0:
                    x = x - 1
                elif e.direction == DIRECTION_RIGHT and x < 7:
                    x = x + 1
                sense.set_pixel(x, y, W)
                #arriba crack
        if encontradas == 2:
            puntaje2 += 1
            puntajeM2-= 1
            print("Monedas a encontrar"+ "-->" + str(puntajeM2))
            
            
    if puntaje2 == puntajeW2:
        Nivel3()
        
        
    else:
        Lose()
        sense.show_message(
            "Score" + "" + str(puntaje3 + puntaje2 + puntaje1))


def Nivel3():
    # Nivel 3
    global puntaje3
    global encontradas
    global puntajeW3
    puntajeM3 = 2
    intro3()
    print("\nMonedas a encontrar"+ "-->" + str(puntajeM2))
    # inicia nivel 3
    for turno in range(puntajeW3):
        #moneda 1
        coinx = randint(0, 7)
        coiny = randint(0, 7)
        # print(coinx,coiny)
        
        #Moneda 2
        coinx2 = randint(0, 7)
        coiny2 = randint(0, 7)
        
        #Moneda3
        coinx3 = randint(0, 7)
        coiny3 = randint(0, 7)
        
        #Fake Moneda1
        coinxF1 = randint(0, 7)
        coinyF1 = randint(0, 7)
        
        #Fake Moneda2
        coinxF2 = randint(0, 7)
        coinyF2 = randint(0, 7)

        # Escondiendo moneda
        sense.set_pixel(coinx, coiny, Y)
        sense.set_pixel(coinx2, coiny2, Y)
        sense.set_pixel(coinx3, coiny3, Y)
        sense.set_pixel(coinxF1, coinyF1, N)
        sense.set_pixel(coinxF2, coinyF2, N)
        
        
        sleep(.5)
        sense.clear(Y)
        sleep(1)
        sense.clear()

        # coordenadas del jugador
        x = randint(0, 7)
        y = randint(0, 7)
        sense.set_pixel(x, y, W)
        for moneda in range(3):    
                      
                    while True:  #
                        e = wait_for_move()
        
                        if e.direction == DIRECTION_MIDDLE:
        
                            if x == coinx and y == coiny:
                                sense.set_pixel(x, y, G)
                                encontradas += 1
                            elif x == coinx2 and y == coiny2:
                                sense.set_pixel(x, y, G)
                                encontradas += 1
                            elif x == coinx3 and y == coiny3:
                                sense.set_pixel(x, y, G)
                                encontradas += 1  
                                
                            else:
                                sense.set_pixel(x, y, R)
        
                            sleep(1)
                            sense.clear()
                            break
                        sense.clear()
        
                        if e.direction == DIRECTION_UP and y > 0:
                            y = y - 1
                        elif e.direction == DIRECTION_DOWN and y < 7:
                            y = y + 1
                        elif e.direction == DIRECTION_LEFT and x > 0:
                            x = x - 1
                        elif e.direction == DIRECTION_RIGHT and x < 7:
                            x = x + 1
                        sense.set_pixel(x, y, W)
                        #arriba crack
        if encontradas == 3:
                  puntaje2 += 1
                  puntajeM3-= 1
                  print("Monedas a encontrar"+ "-->" + str(puntajeM3))
        # este muestra el mensaje final
    if puntaje3 == puntajeW3:
        win()
        sense.show_message("Score" + "" + str(puntaje3 + puntaje2 + puntaje1))
    else:
        Lose()
        sense.show_message("Score" + "" + str(puntaje3 + puntaje2 + puntaje1))

# Codigo inicial


def juegoInicia():
  intro()
  Nivel1()


# llegue pappu
while True:
  
  juegoInicia()
  

