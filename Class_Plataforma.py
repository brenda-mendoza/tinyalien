import pygame
from random import randint
from constantes import *

class Plataforma:
    def __init__(self, path, ancho, alto, x, y, es_visible:bool = False, tiene_llave:bool = False, tiene_vida: bool = False, mover_vertical:bool = False, mover_horizontal:bool = False) -> None: #constructor
        
        self.es_visible = es_visible

        if self.es_visible:
            self.imagen = pygame.image.load(path)
            self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        else:
            self.imagen = pygame.Surface((ancho, alto))
    
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.velocidad_y = 3
        self.velocidad_x = 3
        self.premio = tiene_llave
        self.tiene_vida = tiene_vida
        self.mover_vertical = mover_vertical
        self.mover_horizontal = mover_horizontal

        # Dirección actual de la plataforma (1 para derecha, -1 para izquierda)
        self.direccion_actual = 1

    def mover_plataforma(self):
        if self.mover_horizontal:
            self.rectangulo.x += self.velocidad_x * self.direccion_actual

            # Si la plataforma llega a 600 píxeles, cambia de dirección
            if self.rectangulo.x >= 600 and self.direccion_actual == 1:
                self.direccion_actual = -1  # Cambia la dirección a la izquierda

            # Si la plataforma choca con el borde izquierdo, cambia de dirección
            elif self.rectangulo.x <= 0 and self.direccion_actual == -1:
                self.direccion_actual = 1  # Cambia la dirección a la derecha

        elif self.mover_vertical:
            self.rectangulo.y += self.velocidad_y
            # Si la plataforma se va del alto de la pantalla, vuelve a aparecer en la parte superior
            if self.rectangulo.y > ALTO:
                self.rectangulo.y = - self.rectangulo.height
    
    def actualizar(self):
        if self.mover_horizontal or self.mover_vertical:
            self.mover_plataforma()
        if self.es_visible:
            PANTALLA.blit(self.imagen, self.rectangulo)