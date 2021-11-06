import pygame
import time
import random

#Definiciones globales
pygame.init()

#w = ancho
#h = alto

pantallaw = 1000
pantallah = 1000

#Colores
fondo = (50,50,50)
white = (255,255,255)
marco = (100,100,200)
vereda = (40,39,39)
selva = (10,150,10)
agua = (100,100,230)

#Resources
crocki = pygame.image.load('crockicrocki.png')
carr = pygame.image.load('carr.png')
carl = pygame.image.load('carl.png')
tortuga = pygame.image.load('tortugas.png')
arbol = pygame.image.load('arbol.png')

crockis = []

areajuego = pygame.display.set_mode((pantallaw,pantallah))
pygame.display.set_caption('Crocki Crocki!')

gametimer = pygame.time.Clock()

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largetext = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = (x,y)
    areajuego.blit(TextSurf, TextRect)

def obj_colisiones(a,jposx,w):
    if jposx >= a and jposx <= a+w:
        return True
    elif jposx+50 >= a and jposx+50 <= a+w:
        return True
    return False


def game_loop():
#Posiciones Iniciales
    jposx = 950
    jposy = 900

    auto01y = 550
    auto02y = 600
    auto03y = 650
    auto04y = 700
    auto05y = 750
    auto06y = 800
    auto07y = 850

    agua01y = 100
    agua02y = 150
    agua03y = 200
    agua04y = 250
    agua05y = 300
    agua06y = 350
    agua07y = 400
    agua08y = 450

    auto01 = [100,300]
    auto02 = [200,400]
    auto03 = [300,400]
    auto04 = [100,700]
    auto05 = [600,800]
    auto06 = [100,900]
    auto07 = [500,950]

    agua01 = [100,350]
    agua02 = [200,500]
    agua03 = [400,950]
    agua04 = [100,400]
    agua05 = [500,750]
    agua06 = [100,900]
    agua07 = [700,850]
    agua08 = [300,600]

    #crockis = []

    g1mx = 7
    g2mx = 4
    g3mx = -4

    ciclos = 5000
    puntaje = 0
    
    termino = False

    while not termino:
        #EVENTOS DEL TECLADO
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            termino = True
                        if event.key == pygame.K_LEFT:
                            if jposx <= 0:
                                jposx = 0
                            else:
                                jposx = jposx-50
                            #print("A la izquierda")
                        elif event.key == pygame.K_RIGHT:
                            if jposx >= 950:
                                jposx = 950
                            else:
                                jposx = jposx+50
                            #print("A la derecha")
                        elif event.key == pygame.K_UP:
                            if jposy <= 50:
                                jposy = 50
                            else:
                                jposy = jposy-50
                            #print("A la derecha")
                        elif event.key == pygame.K_DOWN:
                            if jposy >= 900:
                                jposy = 900
                            else:
                                jposy = jposy+50
                            #print("A la derecha")

        #COLISIONES
        if jposy == 850:
            for a in auto07:
                termino = obj_colisiones(a,jposx,50)
                if termino:
                    break
        if jposy == 800:
            for a in auto06:
                termino = obj_colisiones(a,jposx,50)
                if termino:
                    break
        if jposy == 750:
            for a in auto05:
                termino = obj_colisiones(a,jposx,50)
                if termino:
                    break
        if jposy == 700:
            for a in auto04:
                termino = obj_colisiones(a,jposx,50)
                if termino:
                    break
        if jposy == 650:
            for a in auto03:
                termino = obj_colisiones(a,jposx,50)
                if termino:
                    break
        if jposy == 600:
            for a in auto02:
                termino = obj_colisiones(a,jposx,50)
                if termino:
                    break
        if jposy == 550:
            for a in auto01:
                termino = obj_colisiones(a,jposx,50)
                if termino:
                    break

        #COLISIONES EN EL AGUA
        #COLISIONES
        notenelagua = False

        if jposy == 450:
            for a in agua08:
                notenelagua = obj_colisiones(a,jposx,150)
                if notenelagua:
                    break
            if notenelagua:
                jposx = jposx + g2mx
            else:
                termino = True
                break
        if jposy == 400:
            for a in agua07:
                notenelagua = obj_colisiones(a,jposx,150)
                if notenelagua:
                    break
            if notenelagua:
                jposx = jposx + g3mx
            else:
                termino = True
                break
        if jposy == 350:
            for a in agua06:
                notenelagua = obj_colisiones(a,jposx,150)
                if notenelagua:
                    break
            if notenelagua:
                jposx = jposx + g1mx
            else:
                termino = True
                break
        if jposy == 300:
            for a in agua05:
                notenelagua = obj_colisiones(a,jposx,150)
                if notenelagua:
                    break
            if notenelagua:
                jposx = jposx + g3mx
            else:
                termino = True
                break
        if jposy == 250:
            for a in agua04:
                notenelagua = obj_colisiones(a,jposx,150)
                if notenelagua:
                    break
            if notenelagua:
                jposx = jposx + g1mx
            else:
                termino = True
                break
        if jposy == 200:
            for a in agua03:
                notenelagua = obj_colisiones(a,jposx,150)
                if notenelagua:
                    break
            if notenelagua:
                jposx = jposx + g3mx
            else:
                termino = True
                break
        if jposy == 150:
            for a in agua02:
                notenelagua = obj_colisiones(a,jposx,150)
                if notenelagua:
                    break
            if notenelagua:
                jposx = jposx + g2mx
            else:
                termino = True
                break
        if jposy == 100:
            for a in agua01:
                notenelagua = obj_colisiones(a,jposx,150)
                if notenelagua:
                    break
            if notenelagua:
                jposx = jposx + g3mx
            else:
                termino = True
                break

        #LLEGADA A LA META
        if jposy == 50:
            puntaje = puntaje + 20000
            jposy = 900
            crockis.append(jposx)

        #MOVIMIENTOS
        #Autos
        for x in range(0,len(auto01)):
            if auto01[x] >= 990:
                auto01[x] = 0
            else:
                auto01[x] = (auto01[x] + g1mx)
        for x in range(0,len(auto02)):
            if auto02[x] <= 0:
                auto02[x] = 990
            else:
                auto02[x] = (auto02[x] + g3mx)
        for x in range(0,len(auto03)):
            if auto03[x] <= 0:
                auto03[x] = 990
            else:
                auto03[x] = (auto03[x] + g3mx)
        for x in range(0,len(auto04)):
            if auto04[x] >= 990:
                auto04[x] = 0
            else:
                auto04[x] = (auto04[x] + g1mx)
        for x in range(0,len(auto05)):
            if auto05[x] >= 990:
                auto05[x] = 0
            else:
                auto05[x] = (auto05[x] + g2mx)
        for x in range(0,len(auto06)):
            if auto06[x] <= 0:
                auto06[x] = 990
            else:
                auto06[x] = (auto06[x] + g3mx)
        for x in range(0,len(auto07)):
            if auto07[x] >= 990:
                auto07[x] = 0
            else:
                auto07[x] = (auto07[x] + g2mx)

        #Cosas en el Agua
        for x in range(0,len(agua01)):
            if agua01[x] <= -100:
                agua01[x] = 990
            else:
                agua01[x] = (agua01[x] + g3mx)
        for x in range(0,len(agua02)):
            if agua02[x] >= 990:
                agua02[x] = -100
            else:
                agua02[x] = (agua02[x] + g2mx)
        for x in range(0,len(agua03)):
            if agua03[x] <= -100:
                agua03[x] = 990
            else:
                agua03[x] = (agua03[x] + g3mx)
        for x in range(0,len(agua04)):
            if agua04[x] >= 990:
                agua04[x] = -100
            else:
                agua04[x] = (agua04[x] + g1mx)
        for x in range(0,len(agua05)):
            if agua05[x] <= -100:
                agua05[x] = 990
            else:
                agua05[x] = (agua05[x] + g3mx)
        for x in range(0,len(agua06)):
            if agua06[x] >= 990:
                agua06[x] = -100
            else:
                agua06[x] = (agua06[x] + g1mx)
        for x in range(0,len(agua07)):
            if agua07[x] <= -100:
                agua07[x] = 990
            else:
                agua07[x] = (agua07[x] + g3mx)
        for x in range(0,len(agua08)):
            if agua08[x] >= 990:
                agua08[x] = -100
            else:
                agua08[x] = (agua08[x] + g2mx)
        

        #PINTAR FONDO
        areajuego.fill(fondo)
        #PINTAR Marco y cosas fijas
        #Marco
        pygame.draw.rect(areajuego, marco, [0, 0, pantallaw, 50])
        pygame.draw.rect(areajuego, marco, [0, 950, pantallaw, 50])
        #Veredas
        pygame.draw.rect(areajuego, vereda, [0, 500, pantallaw, 50])
        pygame.draw.rect(areajuego, vereda, [0, 900, pantallaw, 50])
        #Selva
        pygame.draw.rect(areajuego, selva, [0, 50, pantallaw, 50])
        #Agua
        pygame.draw.rect(areajuego, agua, [0, 100, pantallaw, 400])


        message_display("Ciclos restantes: "+str(ciclos),300,975)
        message_display("Puntaje de Crockis salvados: "+str(puntaje),300,25)

        for a in agua01:
            areajuego.blit(tortuga,(a,agua01y))
        for a in agua02:
            areajuego.blit(arbol,(a,agua02y))
        for a in agua03:
            areajuego.blit(tortuga,(a,agua03y))
        for a in agua04:
            areajuego.blit(arbol,(a,agua04y))
        for a in agua05:
            areajuego.blit(tortuga,(a,agua05y))
        for a in agua06:
            areajuego.blit(arbol,(a,agua06y))
        for a in agua07:
            areajuego.blit(tortuga,(a,agua07y))
        for a in agua08:
            areajuego.blit(arbol,(a,agua08y))
        
        areajuego.blit(crocki,(jposx,jposy))

        for a in auto01:
            areajuego.blit(carr,(a,auto01y))
        for a in auto02:
            areajuego.blit(carl,(a,auto02y))
        for a in auto03:
            areajuego.blit(carl,(a,auto03y))
        for a in auto04:
            areajuego.blit(carr,(a,auto04y))
        for a in auto05:
            areajuego.blit(carr,(a,auto05y))
        for a in auto06:
            areajuego.blit(carl,(a,auto06y))
        for a in auto07:
            areajuego.blit(carr,(a,auto07y))

        for a in crockis:
            areajuego.blit(crocki,(a,50))
        
        



        #Mostrar todo
        pygame.display.update()
        gametimer.tick(60)
        ciclos = ciclos-1
        if ciclos == 0:
            termino = True
    if puntaje == 0:
        ciclos = 0
    return ciclos+puntaje


def main():
    #Cuerpo del programa que llama al juego
    areajuego.fill(fondo)
    score = game_loop()

    time.sleep(4)
    areajuego.fill(fondo)
    for a in crockis:
        areajuego.blit(crocki,(a,50))
    message_display("Puntaje total: "+str(score),300,450)
    pygame.display.update()
    print("Tu score fue: ",score)
    time.sleep(4)
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()