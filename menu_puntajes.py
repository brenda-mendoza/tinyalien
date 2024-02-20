import pygame
from constantes import *
from configuraciones import *
from sql import *
from Class_Boton import Boton

def menu_puntajes(pantalla):

    #FONDO
    fondo = pygame.image.load(r"fondos\fondo_puntajes.png")
    #BTN VOLVER
    volver = Boton(750, 600, "Volver", r"imagenes_interfaz\PNG\boton_metal_grande.png", FUENTE_32, ROJO)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        pantalla.blit(fondo, (0, 0))
        volver.draw(pantalla)

        #Conecta con la base de datos y trae los 3 puntajes mas altos
        lista_puntajes = buscar_puntajes_altos()
        pos_y = 200  # Ajusta la posición vertical de los elementos en pantalla

        if lista_puntajes:
            # Titulo de la pantalla
            renderizar_texto(pantalla, "   Nombre   |  Puntaje    ", FUENTE_38, ROJO, 430, 150)
            # Recorre la lista de puntajes y los muestra
            for nombre, puntaje in lista_puntajes:
                blitear_variable_en_pantalla(pantalla, nombre, puntaje, (450, pos_y),(500,70), BLANCO, AZUL, FUENTE_32)             
                pos_y += 100  # Ajusta el espacio vertical entre los elementos

        else:
            renderizar_texto(pantalla, "No hay puntajes para mostrar", FUENTE_36, ROJO, 100,250)
        
        #Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Verificar si se hizo clic en el botón de volver
                if volver.rectangulo.collidepoint(x, y):
                    click.play()
                    return -1

        pygame.display.flip()
        RELOJ.tick(FPS)

