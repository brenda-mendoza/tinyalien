import pygame

from Class_Personaje import *
from Class_Enemigo import Enemigo
from Class_Plataforma import Plataforma
from Class_Item import Item
from Class_Boss import Boss


from configuraciones import *
from animaciones import *
from constantes import *
from items import *

################ FONDO NIVEL 1 #####################

fondo_nivel_02 = pygame.image.load(r"fondos\fondo_nivel_03.png").convert()#Acelera el juego y hace que consuma menos recursos
fondo_nivel_02 = pygame.transform.scale(fondo_nivel_02, (ANCHO,ALTO))


################ PLATAFORMAS #######################

piso_01 = Plataforma("", 298, 20, 0, 0)
piso_02 = Plataforma("", 292, 65, 534, 461)
piso_03 = Plataforma("", 107, 65, 1134, 463)
plataforma_llave = Plataforma("", 70, 70, 772, 131, tiene_llave=True)
plataforma_vida = Plataforma("", 70, 70, 512, 207, tiene_vida=True)
plataforma_ladrillo_01 = Plataforma("", 70, 70, 441, 207)
plataforma_ladrillo_02 = Plataforma("", 70, 70, 703, 131)
plataforma_movible = Plataforma("fondos/plataforma_movible1.png", 160, 40, 134, 328, es_visible = True, mover_horizontal= True)

lista_plataformas = [
    piso_01,
    piso_02,
    piso_03,
    plataforma_llave,
    plataforma_ladrillo_01,
    plataforma_ladrillo_02,
    plataforma_vida,
    plataforma_movible
]

################### PERSONAJE ###############################
posicion_inicial_x = 70
posicion_inicial_y = 369

rosi = Personaje(rosi, posicion_inicial_x, posicion_inicial_y)
piso_01.rectangulo.top = rosi.rectangulo.bottom

################ CREACION DE ENEMIGOS ########################

enemigo_murcielago = Enemigo(enemigo_murcielago, 380, 402, direccion_aleatoria=True)
enemigo_fantasma = Enemigo(enemigo_fantasma, 300, 120, direccion_aleatoria=True)
boss = Boss(enemigo_boss, 1050, 330)

lista_enemigos = [
    enemigo_murcielago,
    enemigo_fantasma,
]

enemigo_boss = boss

############################ MONEDAS ##############################

grupo_monedas_01 = Item.generar_monedas(4, premio["moneda"], 460, 140, 50)
grupo_monedas_02 = Item.generar_monedas(4, premio["moneda"], 534, 402, 50)
############################# LLAVE ##############################

llave = Item(premio["gema"], 788, 76)
llave.rectangulo.bottom = plataforma_llave.rectangulo.top

######################## EXTRA VIDA ##############################

vida_extra = Item(premio["vida"], 512, 137)
vida_extra.rectangulo.bottom = plataforma_vida.rectangulo.top

########################## PUERTA ABIERTA ########################

puerta = Item(premio["puerta03"], 1136, 349)


############ NIVEL 1 ##########################

nivel_03_data = {
    "nivel": 3,
    "plataformas" : lista_plataformas, 
    "enemigos": lista_enemigos, 
    "llave": llave, 
    "vida_extra": vida_extra,
    "puerta": puerta,
    "monedas": [grupo_monedas_01, grupo_monedas_02],
    "fondo": fondo_nivel_02, 
    "pantalla": PANTALLA,
    "personaje": rosi,
    "boss": enemigo_boss,
    "posicion_x": posicion_inicial_x,
    "posicion_y" : posicion_inicial_y
}


