import pygame
from animaciones import *

import pygame
from animaciones import *

class BolaDeFuego:
    def __init__(self, pos_x, pos_y, direccion) -> None:
        self.animaciones = bola_de_fuego
        self.animacion_actual = bola_de_fuego[0]
        self.rectangulo = self.animacion_actual.get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.centery = pos_y
        self.indice_animacion = 0
        self.velocidad_animacion = 0.15        
        self.direccion = direccion
    
    def animar(self):
        animaciones = self.animaciones

        self.indice_animacion += self.velocidad_animacion
        if self.indice_animacion >= len(animaciones):
            self.indice_animacion = 0

        self.animacion_actual = animaciones[int(self.indice_animacion)]

    def mover_disparo(self):
        if self.direccion == "Izquierda":
            self.mover_disparo_izquierda()
        elif self.direccion == "Diagonal":
            self.mover_disparo_diagonal_arriba()
        elif self.direccion == "Arriba":
            self.mover_disparo_arriba()

    def mover_disparo_izquierda(self):
        self.rectangulo.x -= 8

    def mover_disparo_diagonal_arriba(self):
        self.rectangulo.x -= 8
        self.rectangulo.y -= 8

    def mover_disparo_arriba(self):
        self.rectangulo.y -= 8

    def dibujar(self, pantalla):
        self.mover_disparo()
        self.animar()
        pantalla.blit(self.animacion_actual, self.rectangulo)
