import pygame
from Class_Boton import Boton
from constantes import *
from configuraciones import *


def menu_niveles(pantalla, nivel_actual:int):
    #Brief: Muestra los distintos niveles en pantalla
    #Parameters: la pantalla y el nivel actual
    #Return: el nivel seleccionado

    #FONDO
    fondo = pygame.image.load(r"fondos\fondo_menu_niveles.png")
    
    #BOTONES
    nivel1 = Boton(610, 200, "   NIVEL 1 - Inicia la aventura", r"imagenes_interfaz\PNG\boton_metal_grande.png", FUENTE_32, VERDE)
    nivel2 = Boton(610, 300, "   NIVEL 2 - Esto se pone frio!", r"imagenes_interfaz\PNG\boton_metal_grande.png", FUENTE_32, AZUL)
    nivel3 = Boton(610, 400, "   NIVEL 3 - El infierno está aquí", r"imagenes_interfaz\PNG\boton_metal_grande.png", FUENTE_32, NARANJA)
    volver = Boton(700, 500, "Volver", r"imagenes_interfaz\PNG\boton_metal_grande.png", FUENTE_32, ROJO)

    # Determina si los botones están habilitados según el nivel actual
    nivel1.habilitado = nivel_actual >= 1
    nivel2.habilitado = nivel_actual >= 2
    nivel3.habilitado = nivel_actual >= 3


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        pantalla.blit(fondo, (0, 0))
        
        #Dibuja los botones de cada nivel
        nivel1.draw(pantalla)
        nivel2.draw(pantalla)
        nivel3.draw(pantalla)
     
        volver.draw(pantalla)
        
        # EVENTOS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Verificar si se hizo clic en alguno de los botones de niveles
                if nivel1.rectangulo.collidepoint(x, y):
                    click.play()
                    return 1
                try:
                    #Lo meti en un bloque try porque si hacia click arrojaba un error
                    if nivel2.rectangulo.collidepoint(x, y):
                        click.play()
                        return 2
                    elif nivel3.rectangulo.collidepoint(x, y):
                        click.play()
                        return 3
                except:
                    print("no habilitado")
                
                if volver.rectangulo.collidepoint(x, y):
                    return -1

        pygame.display.flip()
        RELOJ.tick(FPS) 