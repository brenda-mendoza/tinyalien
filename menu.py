import pygame
from constantes import *
from Class_Boton import Boton
from menu_niveles import *
from menu_puntajes import *
from menu_configuracion import *

def menu_principal(pantalla, nivel_actual = 1):

    #FONDO
    fondo = pygame.image.load(r"fondos\fondo_menu_principal.png")
    #BOTONES
    jugar = Boton(570,200, "Jugar", r"imagenes_interfaz\PNG\boton_metal.png", FUENTE_36, ROSA)
    puntajes = Boton(540,300, "Puntaje", r"imagenes_interfaz\PNG\boton_metal_grande.png", FUENTE_36, VERDE)
    configuracion = Boton(480,400, "Configuracion", r"imagenes_interfaz\PNG\boton_metal_grande.png", FUENTE_36, AZUL)
    salir = Boton(570,500, "Salir", r"imagenes_interfaz\PNG\boton_metal.png", FUENTE_36, ROJO)


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        pantalla.blit(fondo, (0, 0))
        jugar.draw(pantalla)
        puntajes.draw(pantalla)
        configuracion.draw(pantalla)
        salir.draw(pantalla)


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if jugar.rectangulo.collidepoint(x, y):
                    click.play()
                    nivel_seleccionado = menu_niveles(pantalla, nivel_actual)
                    return nivel_seleccionado
                
                elif puntajes.rectangulo.collidepoint(x, y):
                    click.play()
                    opcion_seleccionada = menu_puntajes(pantalla)
                    return opcion_seleccionada
                
                elif configuracion.rectangulo.collidepoint(x, y):
                    click.play()
                    opcion_seleccionada = menu_configuracion(pantalla)
                
                elif salir.rectangulo.collidepoint(x, y):
                    pygame.quit()
                    quit()

        pygame.display.flip()
        RELOJ.tick(30)
