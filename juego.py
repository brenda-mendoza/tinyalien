
import pygame, sys
from pygame.locals import *

from Class_UI import UI
from Class_Nivel import Nivel

from constantes import *
from menu import *
from menu_niveles import *
from menu_configuracion import *
from menu_puntajes import *
from modo import *
from items import *
from sql import *

from nivel1 import nivel_01_data
from nivel2 import nivel_02_data
from nivel3 import nivel_03_data


class Juego:
    def __init__(self, nivel_seleccionado) -> None:

       #Atributos del juego
        self.pausa = False
        self.puntaje = 0
        self.max_nivel = 3
        self.max_vidas = 3
        self.vidas_actual = 3
        self.monedas = 0    
        self.nivel_actual = nivel_seleccionado
        self.nivel = self.crear_nivel(self.nivel_actual)
        self.mostrando_pantalla_game_over = False
         
        #Vidas y Monedas
        self.ui = UI(PANTALLA)
        
    def crear_nivel(self, nivel_actual):
        # Brief: crea el nivel
        # Parameters: el nivel seleccionado
        # Return el nivel creado

        tiempo_inicial = pygame.time.get_ticks()

        match nivel_actual:
            case 1:
                nivel = Nivel(nivel_01_data, self.actualizar_monedas, self.actualizar_vidas,
                            self.verificar_siguiente_nivel, tiempo_inicial, self.mostrar_pantalla_juego_terminado)
            case 2:
                nivel = Nivel(nivel_02_data, self.actualizar_monedas, self.actualizar_vidas,
                            self.verificar_siguiente_nivel, tiempo_inicial, self.mostrar_pantalla_juego_terminado)
            case 3:
                nivel = Nivel(nivel_03_data, self.actualizar_monedas, self.actualizar_vidas,
                            self.verificar_siguiente_nivel, tiempo_inicial, self.mostrar_pantalla_juego_terminado)
        return nivel

    def actualizar_monedas(self, cantidad):
            #Brief suma las monedas acumuladas
            #Parameters la cantidad de monedas recolectadas
            #Return, no tiene
            self.monedas += cantidad
            self.puntaje = self.monedas

    def actualizar_vidas(self, cantidad):
        #Brief actualiza las vidas si recoje la vida extra
        #Parameters cantidad
        #Return no tiene
        if self.vidas_actual < 3 and cantidad > 0:
            self.vidas_actual += cantidad
        elif cantidad < 0:
            vida_actual = self.vidas_actual + cantidad
            if vida_actual > 0:
                self.vidas_actual += cantidad
            else:
                self.vidas_actual = 0

    def reiniciar_juego(self):
        # Atributos del juego
        self.puntaje = 0
        self.max_nivel = 3
        self.max_vidas = 3
        self.vidas_actual = 3
        self.monedas = 0
        self.nivel_actual = 1
        # Reiniciar el nivel existente en lugar de crear uno nuevo
        self.nivel.reiniciar_nivel()
        self.mostrando_pantalla_game_over = False

        # Vidas y Monedas
        self.ui = UI(PANTALLA)
 
    def verificar_game_over(self):
        if self.vidas_actual <= 0:

            self.mostrar_pantalla_juego_terminado()
            nivel_seleccionado = menu_principal(PANTALLA)

            if nivel_seleccionado != -1:
                self.reiniciar_juego()
                self.nivel_actual = nivel_seleccionado
                self.nivel = self.crear_nivel(self.nivel_actual)

    def verificar_siguiente_nivel(self):
        
        #Verifica si las monedas recolectadas fueron mas de 6
        if self.monedas > 6:
            self.vidas_actual = 3  

            #Crea una variable intermedia         
            nuevo_nivel = self.nivel_actual + 1

            #Para verificar si el nuevo nivel no supera al maximo nivel
            if nuevo_nivel <= self.max_nivel:
                
                self.nivel_actual = nuevo_nivel
                nivel_seleccionado = menu_niveles(PANTALLA, nuevo_nivel)
                
                if nivel_seleccionado != -1:
                    self.nivel_actual = nivel_seleccionado
                    self.nivel = self.crear_nivel(self.nivel_actual)
            else:
                jugador = self.mostrar_pantalla_juego_ganado()
                insertar_jugador(jugador, self.puntaje)
                self.mostrando_pantalla_game_over = True

    def mostrar_pantalla_juego_terminado(self):

        # MENSAJE
        texto = FUENTE_38.render("  GAME OVER  ", True, (255, 255, 255))  # Texto blanco

        # rectángulo del texto
        texto_rect = texto.get_rect(center=(ANCHO / 2, ALTO / 2))

        # rectángulo y el texto en la pantalla
        pygame.draw.rect(PANTALLA, (0, 0, 0), texto_rect) 
        PANTALLA.blit(texto, texto_rect)

        pygame.display.flip()
        
        # Establece el estado de "GAME OVER" a True
        self.mostrando_pantalla_game_over = True

        # Espera unos segundos antes de continuar
        pygame.time.delay(2000)  #(2 segundos)

    def mostrar_pantalla_juego_ganado(self):

        #FONDO
        fondo_ganador = pygame.image.load(r"fondos\fondo_ganador.png").convert()
        PANTALLA.blit(fondo_ganador, (0,0))
        
        #SONIDO
        ganador.play()
        
        #VARIABLE
        jugador = ""
        
        while True:
            # Bliteo el fondo del área de texto con color blanco para borrar el texto anterior
            pygame.draw.rect(PANTALLA, BLANCO, (230, 150, 800, 50))
            
            texto_superficie = FUENTE_36.render(" Ingresa tu nombre : " + jugador, True, ROSA)
            rectangulo_texto = texto_superficie.get_rect()
            rectangulo_texto.topleft = (230, 150)
            
            PANTALLA.blit(texto_superficie, rectangulo_texto)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return jugador
                    elif event.key == pygame.K_BACKSPACE:
                        jugador = jugador[:-1]
                    else:
                        jugador += event.unicode
            pygame.display.flip()

    def mostrar_pausa(self):
        self.pausa = not self.pausa
        
        # MENSAJE
        texto = FUENTE_38.render(" PAUSA ", True, (255, 255, 255))  # Texto blanco

        # rectángulo del texto
        texto_rect = texto.get_rect(center=(ANCHO / 2, ALTO / 2))

        # rectángulo y el texto en la pantalla
        pygame.draw.rect(PANTALLA, (0, 0, 0), texto_rect) 
        PANTALLA.blit(texto, texto_rect)

        pygame.display.flip()
                        
    def actualizar(self):
        if not self.pausa: 
            self.nivel.actualizar()
            self.ui.mostrar_vidas(self.vidas_actual, self.max_vidas)
            self.ui.mostrar_monedas(self.monedas) 
            self.verificar_game_over()


##############################INICIALIZACIONES##########################################

pygame.init()


def ejecutar_juego():

    while True:
        # NIVEL SELECCIONADO
        nivel_seleccionado = menu_principal(PANTALLA)

        while nivel_seleccionado != -1:
            
            # INSTANCIO EL JUEGO
            juego = Juego(nivel_seleccionado)
           

            # BUCLE PRINCIPAL
            while True:
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit(0)           

                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_TAB:
                            cambiar_modo()

                        elif evento.key == pygame.K_p:
                            juego.mostrar_pausa()

      
                juego.actualizar()

                # Verifica si el juego está en estado de "Game Over"
                if juego.mostrando_pantalla_game_over:
                    juego.reiniciar_juego()
                    nivel_seleccionado = menu_principal(PANTALLA) 
                    break 


                pygame.display.update()
                RELOJ.tick(FPS)

        pygame.display.update()
        RELOJ.tick(FPS)


ejecutar_juego()

