import pygame

class Boton:
    def __init__(self, x, y, texto, path_imagen, fuente, color_texto, habilitado=True):
        self.texto = texto
        self.imagen = pygame.image.load(path_imagen)
        self.rectangulo = self.imagen.get_rect(topleft=(x, y))
        self.habilitado = habilitado  # Nuevo atributo para indicar si el botón está habilitado

        # Fuente para renderizar el texto
        self.fuente = fuente
        self.color_texto = color_texto
        self.texto_renderizado = self.fuente.render(texto, True, self.color_texto)

        # Redimensionar la imagen al tamaño del texto
        self.imagen = pygame.transform.scale(self.imagen, (self.texto_renderizado.get_width() + 20, self.texto_renderizado.get_height() + 20))
        self.rectangulo = self.imagen.get_rect(topleft=(x, y))

    def draw(self, pantalla):
        if self.habilitado:
            pantalla.blit(self.imagen, self.rectangulo)
            # ------------------------ Alinea el texto en el centro del botón
            pantalla.blit(self.texto_renderizado, (self.rectangulo.x + 10, self.rectangulo.y + 10))
        else:
            # Si el botón no está habilitado, muestra una versión grisada del botón
            superficie = pygame.Surface((self.rectangulo.width, self.rectangulo.height), pygame.SRCALPHA)
            superficie.fill((128, 128, 128, 100))  # Agrega una capa de color gris transparente
            pantalla.blit(superficie, self.rectangulo.topleft)
