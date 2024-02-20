import pygame


pygame.init()
# Crear la ventana
ANCHO = 1360
ALTO = 680

FPS = 25 #para desacelerar la pantalla

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles


TIEMPO_LIMITE = 90  # 90 segundos

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (49, 79, 103)
ROSA = (241, 156, 183)
ROSA_OSCURO = (209, 82, 127)
VERDE = (92, 206, 106)
ROJO = (174, 30, 27)
NARANJA = (255,153,3)

# Fuente para el texto
FUENTE_32 = pygame.font.Font("imagenes_interfaz\Fonts\kenvector_future.ttf", 32)
FUENTE_36 = pygame.font.Font("imagenes_interfaz\Fonts\kenvector_future.ttf", 36)
FUENTE_38 = pygame.font.Font("imagenes_interfaz\Fonts\kenvector_future.ttf", 38)
FUENTE_30 = pygame.font.Font("imagenes_interfaz\Fonts\kenvector_future_thin.ttf", 30)