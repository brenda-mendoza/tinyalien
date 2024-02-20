import pygame
from constantes import *

class UI:
    def __init__(self, pantalla) -> None:
        
        self.pantalla = pantalla
        #vidas
        self.vidas = pygame.image.load("items/vida_2.png")
        
        # monedas
        self.moneda = pygame.image.load("items/moneda.png")
        self.moneda_rect = self.moneda.get_rect(topleft = (1100,10))
        self.fuente_score = FUENTE_30
    
    def mostrar_vidas(self, vida_actual, vidas_total):
        # Brief Muestra las vidas en pantalla
        # Parameters: vida actual y total
        # Return no tiene

        self.pantalla.blit(self.vidas, (1290, 16))

        if vida_actual == vidas_total:
            self.vidas = pygame.image.load("items/vida_2.png")
        elif vida_actual == 2:
            self.vidas = pygame.image.load("items/vida_1.png")
        elif vida_actual == 1:    
            self.vidas = pygame.image.load("items/vida_0.png")
      
    def mostrar_monedas(self, cantidad):
        # Brief Muestra las monedas recolectadas
        # Parameters: cantidad 
        # Return no tiene

        moneda_txt = self.fuente_score.render(str(cantidad).zfill(4), False, AZUL)
        moneda_txt_rect = moneda_txt.get_rect(topleft= (1176,30))
        
        #Blitea la moneda 
        self.pantalla.blit(self.moneda, self.moneda_rect)
        #Blitea el score
        self.pantalla.blit(moneda_txt, moneda_txt_rect)
