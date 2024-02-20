import pygame

from Class_Personaje import *
from Class_Enemigo import Enemigo
from Class_Plataforma import Plataforma
from Class_Item import Item

from configuraciones import *
from animaciones import *
from constantes import *
from items import *

################ FONDO NIVEL 1 #####################

fondo_nivel_02 = pygame.image.load(r"fondos\fondo_nivel_02.png").convert()#Acelera el juego y hace que consuma menos recursos
fondo_nivel_02 = pygame.transform.scale(fondo_nivel_02, (ANCHO,ALTO))


################ PLATAFORMAS #######################

piso_01 = Plataforma("", 550, 20, 0, 0)
piso_02 = Plataforma("", 361, 65, 743, 390)
piso_03 = Plataforma("", 140, 65, 1216, 478)
plataforma_llave = Plataforma("", 70, 65, 836, 143, tiene_llave=True)
plataforma_cajones = Plataforma("", 140, 70, 858, 320)
plataforma_vida = Plataforma("", 70, 70, 587, 104, tiene_vida=True)
plataforma_ladrillo = Plataforma("", 71, 33, 341, 277)
plataforma_ladrillo_01 = Plataforma("", 210, 33, 127, 239)
plataforma_ladrillo_02 = Plataforma("", 155, 35, 1035, 229)
plataforma_ladrillo_03 = Plataforma("", 5, 10, 1035, 225)
plataforma_ladrillo_04 = Plataforma("", 5, 10, 1161, 211)
plataforma_ladrillo_05 = Plataforma("", 5, 10, 550, 466)
plataforma_movible = Plataforma("fondos/plataforma_movible.png", 160, 40, 570, 30, es_visible = True, mover_vertical = True)

lista_plataformas = [
    piso_01,
    piso_02,
    piso_03,
    plataforma_llave,
    plataforma_ladrillo_01,
    plataforma_ladrillo,
    plataforma_ladrillo_02,
    plataforma_ladrillo_03,
    plataforma_ladrillo_04,
    plataforma_ladrillo_05,
    plataforma_cajones,
    plataforma_vida,
    plataforma_movible
]

################### PERSONAJE ###############################

posicion_inicial_x = 50
posicion_inicial_y = 380
rosi = Personaje(rosi, posicion_inicial_x, posicion_inicial_y)
piso_01.rectangulo.top = rosi.rectangulo.bottom

################ CREACION DE ENEMIGOS ########################

enemigo_arana = Enemigo(enemigo_arana, 380, 419, direccion_aleatoria=True)
enemigo_mosca = Enemigo(enemigo_mosca, 300, 135,direccion_aleatoria=True)
enemigo_babosa = Enemigo(enemigo_babosa, 1040, 202)

lista_enemigos = [
    enemigo_arana,
    enemigo_mosca,
    enemigo_babosa
]

############################ MONEDAS ##############################

grupo_monedas_01 = Item.generar_monedas(4, premio["moneda"], 124, 150, 70)
grupo_monedas_02 = Item.generar_monedas(3, premio["moneda"], 1025, 143, 70)

monedas = [grupo_monedas_01, grupo_monedas_02]
############################# LLAVE ##############################

llave = Item(premio["llave"], 836, 76)
llave.rectangulo.bottom = plataforma_llave.rectangulo.top

######################## EXTRA VIDA ##############################

vida_extra = Item(premio["vida"], 588, 39)
vida_extra.rectangulo.bottom = plataforma_vida.rectangulo.top

########################## PUERTA ABIERTA ########################

puerta = Item(premio["puerta"], 1264, 368)

############ NIVEL 1 ##########################

nivel_02_data = {
    "nivel": 2,
    "plataformas" : lista_plataformas, 
    "enemigos": lista_enemigos, 
    "llave": llave, 
    "vida_extra": vida_extra,
    "puerta": puerta,
    "monedas": monedas,
    "fondo": fondo_nivel_02, 
    "pantalla": PANTALLA,
    "personaje": rosi,
    "boss" : False,
    "posicion_x": posicion_inicial_x,
    "posicion_y" : posicion_inicial_y
}


