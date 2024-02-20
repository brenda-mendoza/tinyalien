import pygame
from constantes import *
from configuraciones import *
from Class_Item import Item
from Class_Enemigo import Enemigo

from nivel1 import nivel_01_data
from nivel2 import nivel_02_data
from nivel3 import nivel_03_data


class Nivel:
    def __init__(self, nivel_actual, actualizar_monedas, actualizar_vidas, verificar_siguiente_nivel, tiempo_inicial, mostrar_pantalla_juego_terminado):
    
        # Nivel data 
        self.nivel_completo = nivel_actual
        self.nivel = nivel_actual["nivel"]
        self.plataformas = nivel_actual["plataformas"]
        self.enemigos = nivel_actual["enemigos"]
        self.llave = nivel_actual["llave"]
        self.vida_extra = nivel_actual["vida_extra"]
        self.puerta = nivel_actual["puerta"]
        self.monedas = nivel_actual["monedas"]
        self.fondo = nivel_actual["fondo"]
        self.pantalla = nivel_actual["pantalla"]
        self.personaje = nivel_actual["personaje"]
        self.boss = nivel_actual["boss"]
        self.posicion_x = nivel_actual["posicion_x"]
        self.posicion_y = nivel_actual["posicion_y"]
        self.tiempo_inicial = tiempo_inicial

        # Interfaz de usuario // metodos que hereda de Class Juego
        self.actualizar_monedas = actualizar_monedas
        self.actualizar_vidas = actualizar_vidas
        self.verificar_siguiente_nivel = verificar_siguiente_nivel
        self.mostrar_pantalla_juego_terminado = mostrar_pantalla_juego_terminado

    def actualizar_tiempo(self):
        # Actualizar el tiempo transcurrido
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - self.tiempo_inicial) // 1000

        # Muestra el tiempo en pantalla
        tiempo_restante = max(TIEMPO_LIMITE - tiempo_transcurrido, 0)
        texto_tiempo = FUENTE_38.render(f"Tiempo: {tiempo_restante}", True, (255, 255, 255))
        PANTALLA.blit(texto_tiempo, (10, 10))

        if tiempo_restante == 0:
            self.mostrar_pantalla_juego_terminado()

    def reiniciar_nivel(self):

        # Reiniciar enemigos y monedas según el nivel actual
        if self.nivel == 1:
            self.enemigos = nivel_01_data["enemigos"]
            self.monedas = nivel_01_data["monedas"]
        elif self.nivel == 2:
            self.enemigos = nivel_02_data["enemigos"]
            self.monedas = nivel_02_data["monedas"]
        elif self.nivel == 3:
            self.enemigos = nivel_03_data["enemigos"]
            self.monedas = nivel_03_data["monedas"]

        # Reiniciar plataformas, llave y vida_extra
        self.plataformas = self.nivel_completo["plataformas"]
        self.llave = self.nivel_completo["llave"]
        self.vida_extra = self.nivel_completo["vida_extra"]

        # Obtener las coordenadas iniciales del personaje para este nivel
        pos_x_inicial = self.nivel_completo["posicion_x"]
        pos_y_inicial = self.nivel_completo["posicion_y"]

        # Reiniciar el personaje con las nuevas coordenadas iniciales
        self.personaje.reiniciar_personaje(pos_x_inicial, pos_y_inicial)


    ############ COLISIONES ####################
    def verificar_colision_horizontal(self):
        nueva_posicion = self.personaje.rectangulo.x + self.personaje.direccion.x * self.personaje.velocidad
        
        #Verifica si la nueva posicion no se excede de los limites del ancho de la pantalla
        if nueva_posicion > 0 and nueva_posicion <= (self.pantalla.get_width() - self.personaje.rectangulo.width):
            self.personaje.rectangulo.x += self.personaje.direccion.x * self.personaje.velocidad

        for plataforma in self.plataformas:
            plataforma.actualizar()
            if plataforma.rectangulo.colliderect(self.personaje.rectangulo):
                #Personaje se esta moviendo a la Izquierda
                if self.personaje.direccion.x < 0: 
                    self.personaje.rectangulo.left = plataforma.rectangulo.right
                #entonces colocamos el lado izquierdo del rectangulo del personaje con el izq de la plataforma
                
                #self.Personaje se esta moviendo a la Derecha
                elif self.personaje.direccion.x > 0: 
                    self.personaje.rectangulo.right = plataforma.rectangulo.left
                 #entonces colocamos el lado derecho del rectangulo del personaje con el izq de la plataforma
    
    def verificar_colision_vertical(self):
        #Inicia aplicando la gravedad sobre el eje Y
        self.personaje.aplicar_gravedad()

        for plataforma in self.plataformas:
            if plataforma.rectangulo.colliderect(self.personaje.rectangulo):

                #Personaje se esta moviendo hacia abajo
                if self.personaje.direccion.y > 0: 
                #entonces colocamos el lado inferior del rectangulo del personaje 
                # con el superior de la plataforma
                    self.personaje.rectangulo.bottom = plataforma.rectangulo.top
                    self.personaje.direccion.y = 0 
                    #Para que la gravedad se cancele 
                    #y no siga aumentando la direccion
                    self.personaje.esta_saltando = False
                
                elif self.personaje.direccion.y < 0:     

                ######## Colision con Llave y Vida Extra #########
                    if plataforma.premio:
                        self.llave.descubierto = True
                        plataforma.premio = False
                        print("llave descubierto")             
                    elif plataforma.tiene_vida:
                        self.vida_extra.descubierto = True
                        plataforma.tiene_vida = False
                        print("vida descubierto")
                #entonces colocamos el lado superior del rectangulo del personaje 
                # con el inferior de la plataforma
                    self.personaje.rectangulo.top = plataforma.rectangulo.bottom
                    self.personaje.direccion.y = 0 
                    #Para que el salto se cancele y no siga la direccion en negativo

    def verificar_colision_disparos_personaje(self):
        disparos_a_eliminar = []

        for disparo in self.personaje.lista_disparos:
            disparo.dibujar(self.pantalla)
            for plataforma in self.plataformas:
                if disparo.rectangulo.colliderect(plataforma.rectangulo):
                    disparos_a_eliminar.append(disparo)
            for enemigo in self.enemigos:
                if disparo.rectangulo.colliderect(enemigo.rectangulo):
                    disparos_a_eliminar.append(disparo)
                    enemigo.estado_vivo = False
                    self.enemigos.remove(enemigo)
            if self.boss:
                if disparo.rectangulo.colliderect(self.boss.rectangulo):
                    disparos_a_eliminar.append(disparo)
                    self.boss.perder_vida()
            

        # Eliminar disparos después de la iteración
        for disparo in disparos_a_eliminar:
            self.personaje.lista_disparos.remove(disparo)

    def verificar_colision_disparos_boss(self):
        if self.boss:
            disparos_a_eliminar = []

            for disparo in self.boss.lista_disparos:
                disparo.dibujar(self.pantalla)
                if disparo.rectangulo.colliderect(self.personaje.rectangulo):
                    print("colisiono disparo con personaje")
                    disparos_a_eliminar.append(disparo)
                    self.actualizar_vidas(-1)

            # Eliminar disparos después de la iteración
            for disparo in disparos_a_eliminar:
                self.boss.lista_disparos.remove(disparo)

    def verificar_colision_monedas(self):
        for lista_monedas in self.monedas:
            for moneda in lista_monedas:
                if moneda.rectangulo.colliderect(self.personaje.rectangulo):
                    monedas.play()
                    lista_monedas.remove(moneda)
                    self.actualizar_monedas(1)

    def verificar_colision_enemigo_plataformas(self):
        for enemigo in self.enemigos:
            for plataforma in self.plataformas:
                if enemigo.rectangulo.colliderect(plataforma.rectangulo):
                    # Verificar colisión específica con lados izquierdo o derecho
                    if (enemigo.rectangulo.left <= plataforma.rectangulo.right and
                        enemigo.rectangulo.right >= plataforma.rectangulo.left):
                        break

    def verificar_muerte_caida(self):
        if self.personaje.rectangulo.y >= ALTO:         
            self.actualizar_vidas(-3)
            self.reiniciar_nivel()
    
    def verificar_colision_enemigo_personaje(self):
        for enemigo in self.enemigos:
            if self.personaje.rectangulo.colliderect(enemigo.rectangulo):
                #Obtengo los rectangulos del enemigo y personaje que me interesan
                enemigo_centro = enemigo.rectangulo.centery
                enemigo_top = enemigo.rectangulo.top
                personaje_bottom = self.personaje.rectangulo.bottom

                #Si colisiona con el bottom del personaje y viene desde arriba lo mata
                if enemigo_top < personaje_bottom < enemigo_centro and self.personaje.direccion.y >= 0:
                    golpe.play()
                    self.personaje.direccion.y = -15
                    enemigo.estado_vivo = False
                    self.enemigos.remove(enemigo)
                
                #Si colisiona con otra parte del rectangulo le quita vida al personaje
                elif not self.personaje.invencible:
                    self.personaje.puede_disparar = False
                    self.actualizar_vidas(-1)
                    self.personaje.invencible = True
                    self.personaje.tiempo_herido = pygame.time.get_ticks()

        
        #Actualizo el tiempo de invencibilidad
        self.personaje.temporizador_invencibilidad()

    def verificar_colision_llave(self):
        if self.llave.descubierto:
            if self.personaje.rectangulo.colliderect(self.llave.rectangulo):
                llave.play()
                self.llave.recolectado = True
                self.llave.descubierto = False
                self.personaje.tiempo_anterior = pygame.time.get_ticks()
                self.personaje.apertura_portal = True
    
    def verificar_colision_vida(self):
        if self.vida_extra.descubierto:
            if self.personaje.rectangulo.colliderect(self.vida_extra.rectangulo):
                llave.play()
                self.vida_extra.recolectado = True
                self.vida_extra.descubierto = False
                self.actualizar_vidas(1)
     
    def dibujar_llave(self):
        if self.llave.descubierto and not self.llave.recolectado:
            self.pantalla.blit(self.llave.imagen, self.llave.rectangulo)
    
    def dibujar_estrella_vida(self):
        if self.vida_extra.descubierto and not self.vida_extra.recolectado:
            self.pantalla.blit(self.vida_extra.imagen, self.vida_extra.rectangulo)
    
    def dibujar_enemigos(self):
        if self.enemigos:
            for enemigo in self.enemigos:
                enemigo.actualizar(self.pantalla,self.plataformas)

    def dibujar_boss(self):
        if self.boss:
            if self.boss.estado_vivo:
                self.boss.actualizar(self.pantalla,self.plataformas)

    def verificar_colision_boss(self):
         if self.boss:
            boss_rectangulo = self.boss.rectangulo
            personaje_rectangulo = self.personaje.rectangulo
                    #Si colisiona con el bottom del personaje y viene desde arriba lo mata
            if boss_rectangulo.colliderect(personaje_rectangulo) and self.personaje.direccion.y >= 0:
                
                self.boss.perder_vida()
                self.personaje.direccion.y = -15
                print("colisiono con boss")

    def verificar_apertura_portal(self):
        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual > self.personaje.tiempo_apertura_portal + self.personaje.tiempo_anterior:
            self.personaje.apertura_portal = False

        if self.personaje.apertura_portal:
            self.pantalla.blit(self.puerta.imagen, self.puerta.rectangulo)
            if self.personaje.rectangulo.colliderect(self.puerta.rectangulo):
                print("colisiono con la puerta")
                self.verificar_siguiente_nivel()
                return True
            
    def actualizar(self):
        self.pantalla.blit(self.fondo, (0,0))
        self.personaje.actualizar(self.pantalla)
        self.actualizar_tiempo()

        if self.personaje.puede_disparar:
            self.verificar_colision_disparos_personaje()
        self.verificar_colision_vertical()
        self.verificar_colision_horizontal()
        self.verificar_colision_monedas()
        self.verificar_colision_enemigo_personaje()
        self.verificar_colision_enemigo_plataformas()
        self.verificar_colision_llave()
        self.verificar_colision_vida()
        self.verificar_muerte_caida()
        self.verificar_apertura_portal()

        self.dibujar_llave()
        self.dibujar_estrella_vida()
        self.dibujar_enemigos()
        
        if self.boss:
            self.dibujar_boss()
            self.verificar_colision_disparos_boss()
            self.verificar_colision_boss()
        
        Item.dibujar(self.pantalla, self.monedas[0])
        Item.dibujar(self.pantalla, self.monedas[1])




        