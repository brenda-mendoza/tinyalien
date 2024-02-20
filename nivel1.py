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

fondo_nivel_01 = pygame.image.load(r"fondos\fondo_nivel_01.png").convert()#Acelera el juego y hace que consuma menos recursos
fondo_nivel_01 = pygame.transform.scale(fondo_nivel_01, (ANCHO,ALTO))


################ PLATAFORMAS #######################

piso_01 = Plataforma("", 755, 20, 0, 0)
piso_02 = Plataforma("", 320, 20, 902, 472)
piso_03 = Plataforma("", 204, 20, 1152, 410)
piso_04 = Plataforma("", 5, 10, 893, 460)
piso_05 = Plataforma("", 5, 10, 1222, 460)
plataforma_llave = Plataforma("", 70, 65, 1015, 264, tiene_llave=True)
plataforma_vida = Plataforma("", 70, 65, 324, 270, tiene_vida=True)
plataforma_cajon = Plataforma("", 75, 65, 539, 418)
plataforma_ladrillo_01 = Plataforma("", 70, 65, 252, 270)
plataforma_ladrillo_02 = Plataforma("", 140, 65, 558, 145)
plataforma_ladrillo_03 = Plataforma("", 70, 65, 948, 264)
plataforma_ladrillo_04 = Plataforma("", 70, 65, 396, 270)

lista_plataformas = [
    piso_01,
    piso_02,
    piso_03,
    piso_04,
    piso_05,
    plataforma_llave,
    plataforma_cajon,
    plataforma_ladrillo_01,
    plataforma_ladrillo_02,
    plataforma_ladrillo_03,
    plataforma_ladrillo_04,
    plataforma_vida,
]

################### PERSONAJE ###############################
posicion_inicial_x = 50
posicion_inicial_y = 388
rosi = Personaje(rosi, posicion_inicial_x, posicion_inicial_y)
piso_01.rectangulo.top = rosi.rectangulo.bottom


############################# LLAVE ##############################

llave = Item(premio["llave"], 1015, 150)
llave.rectangulo.bottom = plataforma_llave.rectangulo.top

################ CREACION DE ENEMIGOS ########################

enemigo_babosa = Enemigo(enemigo_babosa, 910, 446)
enemigo_abeja = Enemigo(enemigo_abeja, 400, 60, False, True)
enemigo_caracol = Enemigo(enemigo_caracol, 300, 449, direccion_aleatoria=True)

lista_enemigos = [
    enemigo_abeja,
    enemigo_babosa,
    enemigo_caracol]

############################ MONEDAS ##############################

grupo_monedas_01 = Item.generar_monedas(4, premio["moneda"],500, 30, 70)
grupo_monedas_02 = Item.generar_monedas(3, premio["moneda"],728, 340, 70)

monedas = [grupo_monedas_01, grupo_monedas_02]


######################## EXTRA VIDA ##############################
vida_extra = Item(premio["vida"], 325, 200)
vida_extra.rectangulo.bottom = plataforma_vida.rectangulo.top

########################## PUERTA ABIERTA ########################

puerta = Item(premio["puerta"], 1238, 300)
############ NIVEL 1 ##########################

nivel_01_data = {
    "nivel" : 1,
    "plataformas" : lista_plataformas, 
    "enemigos": lista_enemigos, 
    "llave": llave, 
    "vida_extra": vida_extra,
    "puerta": puerta,
    "monedas": monedas,
    "fondo": fondo_nivel_01, 
    "pantalla": PANTALLA,
    "personaje": rosi,
    "boss": False,
    "posicion_x": posicion_inicial_x,
    "posicion_y" : posicion_inicial_y

}


