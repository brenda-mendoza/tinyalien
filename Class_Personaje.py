from configuraciones import *
from Class_Disparo import Disparo

class Personaje:
    def __init__(self, animaciones, pos_x, pos_y):
        self.animaciones = animaciones
        self.animacion_actual = self.animaciones["Quieto"]
        self.rectangulo = animaciones["Quieto"][0].get_rect()
        self.indice_animacion = 0
        self.velocidad_animacion = 0.15
        #posicion inicial
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y

        #MOVIMIENTO DEL PERSONAJE
        self.velocidad = 8
        self.gravedad = 0.8
        self.velocidad_salto = -16
        self.esta_saltando = False
        # Variable direccion en formato vector: permite almacenar los valores de x e y
        # Me sirve de bandera para verificar ambas direcciones y no modificar directamente el rectangulo
        self.direccion = pygame.math.Vector2(0,0)

        # ESTADO DEL PERSONAJE
        self.estado = "Quieto"

        #### APERTURA DE PORTAL ####
        self.apertura_portal = False
        self.tiempo_apertura_portal = 15000
        self.tiempo_anterior = 0
        
        ## INVENCIBILIDAD ##
        self.invencible = False
        self.tiempo_invencibilidad = 3000
        self.tiempo_herido = 0
        self.visible = True

        # DISPARO
        self.lista_disparos = []
        self.puede_disparar = True
        self.disparo_actual = None
        self.tiempo_entre_disparos = 500  # Tiempo que debe pasar entre cada disparo
        self.ultimo_disparo = pygame.time.get_ticks()

    def disparar(self):
        disparo.play()
        pos_x_disparo = None
        pos_y_disparo = self.rectangulo.centery + 15

        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - self.ultimo_disparo > self.tiempo_entre_disparos:
            if self.estado == "Izquierda":
                pos_x_disparo = self.rectangulo.left - 100 
            else:
                pos_x_disparo = self.rectangulo.right + 5

        if pos_x_disparo is not None:    
            disparo_actual = Disparo(pos_x_disparo, pos_y_disparo, self.estado)
            self.lista_disparos.append(disparo_actual)
            self.ultimo_disparo = tiempo_actual

    def animar(self):

        #Setea animacion actual de acuerdo al estado
        animacion = self.animaciones[self.estado]

        # Al indice 0 lo incrementa de a 0.15
        self.indice_animacion += self.velocidad_animacion
        # Como maximo hasta que largo de la cant de elementos de la animacion
        if self.indice_animacion >= len(animacion):
             self.indice_animacion = 0 # resetea el contador
        
        # Va cambiando la variable de animacion actual paulatinamente de acuerdo aumente el indice de animacion
        self.animacion_actual = animacion[int(self.indice_animacion)]      

    def obtener_estado(self):
        #Brief: Verifica que accion esta realizando el personaje
        # de acuerdo al valor tomado por la variable direccion
        #Parameters: self
        #Return: no tiene

        if self.direccion.y != 0: 
            self.estado = "Salta"
        else:
            if self.direccion.x > 0:
                self.estado = "Derecha"
            elif self.direccion.x < 0:
                self.estado = "Izquierda"        
            else:
                self.estado = "Quieto"

    def obtener_tecla_presionada (self):
        # Settea movimiento segun teclas presionadas
        keys = pygame.key.get_pressed()

        #Movimiento Horizonal 
        if(keys[pygame.K_RIGHT]):
            self.direccion.x = 1
        elif(keys[pygame.K_LEFT]):
            self.direccion.x = -1
        else:
            self.direccion.x = 0
        #Movimiento vertical
        if(keys[pygame.K_SPACE]):
            self.saltar()
        #Disparar
        if(keys[pygame.K_d]):
            if self.puede_disparar:
                self.disparar()

    def aplicar_gravedad(self):
            # Modifica primero la variable direccion como intermediaria
            self.direccion.y += self.gravedad
            # Luego es esta variable la que modifica el movimiento del rectangulo
            self.rectangulo.y += self.direccion.y

    def saltar(self):
        if not self.esta_saltando:
            salta.play()
            self.direccion.y = self.velocidad_salto
            self.esta_saltando = True

    def temporizador_invencibilidad(self):
            
        if self.invencible:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_herido >= self.tiempo_invencibilidad:
                self.invencible = False
                self.visible = True
                print("ya no es invencible")
             # Alterna la visibilidad durante el parpadeo
            elif tiempo_actual % 200 < 100:  # Parpadeo cada 200 ms
                self.visible = not self.visible

    def reiniciar_personaje(self, pos_x, pos_y):
        #Brief: Reinicia la posicion en la que se encuentra el personaje
        #Parameters recibe las posiciones de x e y donde quiero ubicarlo
        #Return no tiene
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.direccion.x = 0
        self.direccion.y = 0

    def actualizar(self, pantalla):
        self.obtener_tecla_presionada()
        self.obtener_estado()
        self.animar()
        if self.visible:
            pantalla.blit(self.animacion_actual, self.rectangulo)
       