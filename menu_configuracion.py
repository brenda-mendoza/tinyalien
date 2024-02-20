import pygame
from constantes import *
from configuraciones import *
from Class_Boton import Boton

# Inicializa el sonido ambiente
ambiente.play(-1)

# Inicializa la bandera de play en True
flag_play = True

def menu_configuracion(pantalla):
    #Brief ejecuta el menu de la configuracion del sonido
    #Parameters : la pantalla
    #Return -1 si presiona volver
    
    
    #Fondo
    fondo = pygame.image.load(r"fondos\fondo_cactus.png")
    #Botones
    boton_play = Boton(600, 300, "     ", r"imagenes_interfaz\PNG\play.jpg", FUENTE_38, VERDE)
    boton_pause = Boton(700, 300, "     ", r"imagenes_interfaz\PNG\pausa.jpg", FUENTE_38, ROJO)
    volver = Boton(600, 430, "Volver", r"imagenes_interfaz\PNG\boton_metal.png", FUENTE_32, AZUL)

    
    while True:
        
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
        
                # Click en Boton PLAY
                if boton_play.rectangulo.collidepoint(x, y):
                    click.play()
                    btn_play_click()

                # Click en Boton PAUSE
                elif boton_pause.rectangulo.collidepoint(x, y):
                    click.play()
                    btn_pause_click()

                # Click en Boton VOLVER
                elif volver.rectangulo.collidepoint(x, y):
                    click.play()
                    return -1

        pantalla.blit(fondo, (0, 0))
        renderizar_texto(pantalla, " Sonido ", FUENTE_38, ROSA_OSCURO, 540, 150)
        boton_play.draw(pantalla)
        boton_pause.draw(pantalla)
        volver.draw(pantalla)

        pygame.display.flip()
        RELOJ.tick(30)


########## FUNCIONES BTN PAUSA Y PLAY ##########
def btn_play_click():
    global flag_play
    #Brief verifica si el sonido esta apagado y si es asi lo enciende
    #Parameters no tiene
    #Return no tiene

    if flag_play == False:
        ambiente.play()
 
    flag_play = True

def btn_pause_click():
    #Brief verifica si el sonido esta encendido y si es asi lo apaga
    #Parameters no tiene
    #Return no tiene

    global flag_play
    if flag_play:
        ambiente.stop()
    
    flag_play = False
