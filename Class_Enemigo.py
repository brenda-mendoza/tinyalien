from configuraciones import *
from random import randint
from constantes import *

class Enemigo:
    def __init__(self, animaciones, posicion_x, posicion_y, mover_horizontal=True, mover_vertical=False, direccion_aleatoria =False) -> None:
        self.animaciones = animaciones
        self.animacion_actual = self.animaciones["Derecha"][0]
        self.rectangulo = self.animaciones["Derecha"][0].get_rect()
        self.velocidad_y = randint(1,4)
        self.velocidad_x = randint(1,4)
        self.indice_animacion = 0
        self.velocidad_animacion = 0.15
        self.mover_horizontal = mover_horizontal
        self.mover_vertical = mover_vertical

        # Posicion inicial
        self.rectangulo.x = posicion_x
        self.rectangulo.y = posicion_y

        # Estado
        self.estado_vivo = True
        # dirección del enemigo
        self.direccion_derecha = True
        self.direccion_aleatoria = direccion_aleatoria

        # Tiempo antes de cambiar de dirección
        self.tiempo_cambio_direccion = randint(50, 200)
        self.contador_cambio_direccion = 0

    def cambiar_direccion_aleatoriamente(self):
        # Cambiar la dirección después de un tiempo aleatorio
        if self.direccion_aleatoria:
            self.contador_cambio_direccion += 1
            if self.contador_cambio_direccion >= self.tiempo_cambio_direccion:
                self.invertir_direccion_horizontal()
                self.cambiar_imagen_direccion()
                self.tiempo_cambio_direccion = randint(50, 200)
                self.contador_cambio_direccion = 0

    def invertir_direccion_horizontal(self):
        self.velocidad_x *= -1
        self.direccion_derecha = not self.direccion_derecha

    def cambiar_imagen_direccion(self):
        if self.direccion_derecha:
            self.animacion_actual = self.animaciones["Derecha"]
        else:
            self.animacion_actual = self.animaciones["Izquierda"]

    def invertir_direccion_vertical(self):
        self.velocidad_y *= -1

    def cambiar_direccion_al_chocar_limites(self):
        if self.rectangulo.left < 0 or self.rectangulo.right > ANCHO:
            self.invertir_direccion_horizontal()
        if self.rectangulo.top < 0 or self.rectangulo.bottom > ALTO:
            self.invertir_direccion_vertical()

    def cambiar_direccion_al_colisionar_plataformas(self, plataformas):
        for plataforma in plataformas:
            if self.rectangulo.colliderect(plataforma.rectangulo):
                #Verificar colisión específica con lados izquierdo o derecho
                if self.mover_horizontal:
                    if (self.rectangulo.right > plataforma.rectangulo.left and
                        self.rectangulo.left < plataforma.rectangulo.right):
                        self.invertir_direccion_horizontal()
                        self.cambiar_imagen_direccion()
                        break
                if self.mover_vertical:
                    # Verificar colisión específica con partes superior o inferior
                    if (self.rectangulo.bottom > plataforma.rectangulo.top and
                            self.rectangulo.top < plataforma.rectangulo.bottom):
                        self.invertir_direccion_vertical()
                        break

    def avanzar(self):
        if self.mover_horizontal:
            self.rectangulo.x += self.velocidad_x
        elif self.mover_vertical:
            self.rectangulo.y += self.velocidad_y

    def animar(self):
        if self.estado_vivo:
            if self.direccion_derecha:
                animaciones = self.animaciones["Derecha"]
            else:
                animaciones = self.animaciones["Izquierda"]
        else:
            animaciones = self.animaciones["Muerto"]

        self.indice_animacion += self.velocidad_animacion
        if self.indice_animacion >= len(animaciones):
            self.indice_animacion = 0

        self.animacion_actual = animaciones[int(self.indice_animacion)]
 
    def actualizar(self, pantalla, plataformas):
        self.cambiar_direccion_al_chocar_limites()
        self.cambiar_direccion_aleatoriamente()
        self.cambiar_direccion_al_colisionar_plataformas(plataformas)
        self.avanzar()
        self.animar()
        pantalla.blit(self.animacion_actual, self.rectangulo)
