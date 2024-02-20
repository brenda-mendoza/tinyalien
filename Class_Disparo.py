import pygame
from constantes import * 

class Disparo:
    def __init__(self, pos_x, pos_y, direccion) -> None:
        #Atributos
        self.imagen = pygame.image.load("items\disparo1.png")
        self.imagen = pygame.transform.scale(self.imagen,(50,50))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.centery = pos_y
        self.direccion = direccion
        
    def mover_disparo(self):
        if self.direccion == "Izquierda":
            self.rectangulo.x -= 10
        else:
            self.rectangulo.x += 10
    
    def dibujar(self, pantalla):
        self.mover_disparo()
        pantalla.blit(self.imagen, self.rectangulo)

