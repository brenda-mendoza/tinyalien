import pygame
from configuraciones import *

########################## ROSI ############################################
rosi = {}
rosi['Quieto'] = [
    pygame.image.load("jugador/rosi/rosi_quieto.png")
]
rosi['Derecha'] = [
    pygame.image.load("jugador/rosi/rosi_caminando1.png"),
    pygame.image.load("jugador/rosi/rosi_caminando2.png")
]
rosi['Izquierda'] = girar_imagenes(rosi["Derecha"], True, False)

rosi['Herido'] = [
    pygame.image.load("jugador/rosi/rosi_herido.png"),
]
rosi['Agachado'] = [
    pygame.image.load("jugador/rosi/rosi_abajo.png"),
]
rosi["Salta"] = [
    pygame.image.load("jugador/rosi/rosi_saltando.png")
]
rosi["Trepa"] = [
    pygame.image.load("jugador/rosi/rosi_trepando1.png"),
    pygame.image.load("jugador/rosi/rosi_trepando2.png")
]

################################# ENEMIGO ############################

enemigo_babosa = {}

enemigo_babosa["Izquierda"] = [
    pygame.image.load("enemigos/babosa_camina1.png"),
    pygame.image.load("enemigos/babosa_camina2.png")
]
enemigo_babosa["Derecha"] = [
    pygame.transform.flip(enemigo_babosa["Izquierda"][0],True,False),
    pygame.transform.flip(enemigo_babosa["Izquierda"][1],True,False)
]
enemigo_babosa["Muerto"] = [
    pygame.image.load("enemigos/babosa_aplastado.png"),
]

#-----------------------------------------------------------------------##
enemigo_abeja = {}

enemigo_abeja["Izquierda"] = [
    pygame.image.load("enemigos/abeja1.png"),
    pygame.image.load("enemigos/abeja2.png")
]
enemigo_abeja["Derecha"] = [
    pygame.transform.flip(enemigo_abeja["Izquierda"][0],True,False),
    pygame.transform.flip(enemigo_abeja["Izquierda"][1],True,False),
]
enemigo_abeja["Muerto"] = [
    pygame.image.load("enemigos/abeja_muerta.png"),
]

#-----------------------------------------------------------------------##

enemigo_caracol = {}

enemigo_caracol["Izquierda"] = [
    pygame.image.load("enemigos/caracol1.png"),
    pygame.image.load("enemigos/caracol2.png")
]
enemigo_caracol["Derecha"] = [
    pygame.transform.flip(enemigo_caracol["Izquierda"][0],True,False),
    pygame.transform.flip(enemigo_caracol["Izquierda"][1],True,False),
]
enemigo_caracol["Muerto"] = [
    pygame.image.load("enemigos/caracol_muerto.png"),
]

#-----------------------------------------------------------------------##

enemigo_arana = {}

enemigo_arana["Izquierda"] = [
    pygame.image.load("enemigos/arana1.png"),
    pygame.image.load("enemigos/arana2.png")
]
enemigo_arana["Derecha"] = [
    pygame.transform.flip(enemigo_arana["Izquierda"][0],True,False),
    pygame.transform.flip(enemigo_arana["Izquierda"][1],True,False),
]
enemigo_arana["Muerto"] = [
    pygame.image.load("enemigos/arana_muerta.png"),
]

#-----------------------------------------------------------------------##

enemigo_mosca = {}

enemigo_mosca["Izquierda"] = [
    pygame.image.load("enemigos/mosca1.png"),
    pygame.image.load("enemigos/mosca2.png")
]
enemigo_mosca["Derecha"] = [
    pygame.transform.flip(enemigo_mosca["Izquierda"][0],True,False),
    pygame.transform.flip(enemigo_mosca["Izquierda"][1],True,False),
]
enemigo_mosca["Muerto"] = [
    pygame.image.load("enemigos/mosca_muerta.png"),
]
#-----------------------------------------------------------------------##

enemigo_fantasma = {}

enemigo_fantasma["Izquierda"] = [
    pygame.image.load("enemigos/fantasma1.png"),
    pygame.image.load("enemigos/fantasma2.png")
]
enemigo_fantasma["Derecha"] = [
    pygame.transform.flip(enemigo_fantasma["Izquierda"][0],True,False),
    pygame.transform.flip(enemigo_fantasma["Izquierda"][1],True,False),
]
enemigo_fantasma["Muerto"] = [
    pygame.image.load("enemigos/fantasma_muerto.png"),
]
#-----------------------------------------------------------------------##

enemigo_murcielago = {}

enemigo_murcielago["Izquierda"] = [
    pygame.image.load("enemigos\murcielago1.png"),
    pygame.image.load("enemigos/murcielago2.png")
]
enemigo_murcielago["Derecha"] = [
    pygame.transform.flip(enemigo_murcielago["Izquierda"][0],True,False),
    pygame.transform.flip(enemigo_murcielago["Izquierda"][1],True,False),
]
enemigo_murcielago["Muerto"] = [
    pygame.image.load("enemigos/murcielago_muerto.png"),
]

#-----------------------------------------------------------------------##

enemigo_boss = {}

enemigo_boss["Imagen"] = [
    pygame.image.load(r"enemigos\boss\0.png"),
    pygame.image.load(r"enemigos\boss\1.png"),
    pygame.image.load(r"enemigos\boss\2.png"),
    pygame.image.load(r"enemigos\boss\3.png"),
    pygame.image.load(r"enemigos\boss\4.png"),
    pygame.image.load(r"enemigos\boss\5.png"),
]

enemigo_boss["Izquierda"] = [
    pygame.transform.flip(enemigo_boss["Imagen"][0],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][1],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][2],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][3],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][4],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][5],True,False),
]
enemigo_boss["Derecha"] = [
    pygame.transform.flip(enemigo_boss["Imagen"][0],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][1],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][2],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][3],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][4],True,False),
    pygame.transform.flip(enemigo_boss["Imagen"][5],True,False),
]
enemigo_boss["Muerto"] = [
    pygame.image.load(r"enemigos\boss\5.png"),
]

####################### BOLA DE FUEGO ####################################

bola_de_fuego = [
    pygame.image.load(r"enemigos\boss\bola_fuego0.png"),
    pygame.image.load(r"enemigos\boss\bola_fuego1.png"),
    pygame.image.load(r"enemigos\boss\bola_fuego2.png"),
    pygame.image.load(r"enemigos\boss\bola_fuego3.png"),
    pygame.image.load(r"enemigos\boss\bola_fuego4.png"),
    pygame.image.load(r"enemigos\boss\bola_fuego5.png"),
    pygame.image.load(r"enemigos\boss\bola_fuego6.png"),
    pygame.image.load(r"enemigos\boss\bola_fuego7.png"),
    pygame.image.load(r"enemigos\boss\bola_fuego8.png"),
]


