import pygame
from constantes import *
from configuraciones import *
from random import randint
from Class_Enemigo import Enemigo
from Class_Bola_fuego import BolaDeFuego

class Boss(Enemigo):
    def __init__(self, animaciones, x, y):
        super().__init__(animaciones, x, y, mover_horizontal=True, mover_vertical=False, direccion_aleatoria=False)

        self.animacion_actual = self.animaciones["Izquierda"][0]
        self.animacion_actual = pygame.transform.scale(self.animacion_actual, (80,160))
        self.rectangulo = self.animacion_actual.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.vidas = 6
        
        # DISPARO
        self.lista_disparos = []
        self.disparo_actual = None
        self.tiempo_entre_disparos = randint(10, 50)
        self.ultimo_disparo = pygame.time.get_ticks()
        self.direcciones_disparo = ["Izquierda", "Diagonal", "Arriba"]
        self.indice_direccion = 0

    def disparar(self):
        explosion.play()
        pos_x_disparo = self.rectangulo.centerx
        pos_y_disparo = self.rectangulo.y + randint(20, 50) 

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_disparo > self.tiempo_entre_disparos:
            direccion_actual = self.direcciones_disparo[self.indice_direccion]
            disparo_actual = BolaDeFuego(pos_x_disparo, pos_y_disparo, direccion_actual)
            self.lista_disparos.append(disparo_actual)
            self.ultimo_disparo = tiempo_actual
            self.indice_direccion = (self.indice_direccion + 1) % len(self.direcciones_disparo)
            self.tiempo_entre_disparos = randint(1000, 5000) 

    def perder_vida(self):
        self.vidas -= 1
        if self.vidas <= 0:
            self.estado_vivo = False

    def actualizar(self, pantalla, plataformas):
        super().actualizar(pantalla, plataformas)
        self.disparar()
        self.actualizar_disparos(pantalla)

    def actualizar_disparos(self, pantalla):
        for disparo in self.lista_disparos:
            disparo.mover_disparo()
            disparo.animar()
            disparo.dibujar(pantalla)


###############################################################################

