import pygame

################# SONIDOS ##########################
pygame.mixer.init()

ambiente = pygame.mixer.Sound("sonidos/ambiente.ogg")
ambiente.set_volume(0.05)

disparo = pygame.mixer.Sound("sonidos\disparo.ogg")
disparo.set_volume(0.03)

monedas = pygame.mixer.Sound("sonidos\monedas.mp3")
monedas.set_volume(0.05)

golpe = pygame.mixer.Sound("sonidos\golpe.ogg")
golpe.set_volume(0.05)

salta = pygame.mixer.Sound("sonidos\salta.ogg")
salta.set_volume(0.05)

click = pygame.mixer.Sound("sonidos\selecciono.ogg")
click.set_volume(0.03)

explosion = pygame.mixer.Sound("sonidos\explosion.mp3")
explosion.set_volume(0.03)

suspenso = pygame.mixer.Sound("sonidos\suspenso.mp3")
suspenso.set_volume(0.03)

ganador = pygame.mixer.Sound("sonidos\ganador.mp3")
ganador.set_volume(0.03)

llave = pygame.mixer.Sound("sonidos\llave.mp3")
llave.set_volume(0.03)

######################### FUNCIONES IMAGENES ###################################################

def girar_imagenes(lista_original:list,girar_horizontal:bool,girar_vertical:bool)->list:
    # Brief Gira imagenes vertical y horizontalmente
    # Parameters una lista de imagenes, un bool de acuerdo al giro que quiero realizar
    # Return la lista con las imagenes giradas
    lista_girada = []
    for img in lista_original:
        lista_girada.append(pygame.transform.flip(img, girar_horizontal, girar_vertical))
        
    return lista_girada

def reescalar_imagenes(diccionario_animaciones:dict, ancho:int, alto:int):
    # Brief Gira imagenes vertical y horizontalmente
    # Parameters una lista de imagenes, un bool de acuerdo al giro que quiero realizar
    # Return la lista con las imagenes giradas
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))
            
#######################  RENDERIZAR TEXTO  #################################################

def renderizar_texto(pantalla, texto, fuente, color, pos_x = 50, pos_y = 320):
    # Brief Renderiza en pantalla el texto
    # Parameters la superficie, el texto, la fuente, color y posicion donde quiero mostrar el texto
    # Return no tiene
    txt_render = fuente.render(texto, True, color)
    pantalla.blit(txt_render, (pos_x, pos_y))

###################  BLITEAR VARIABLE EN PANTALLA  ############################################

def blitear_variable_en_pantalla(superficie, variable, variable2, posicion:tuple, tamaño, color_fondo: tuple, color_texto:tuple, fuente:str):
    # Brief Renderiza en pantalla una variable y su valor
    # Parameters la superficie, la variable, color y posicion donde quiero mostrar el texto
    # Return no tiene
    
    
    # Define un rectángulo
    rectangulo = pygame.Rect(posicion, tamaño)  
    # Dibuja el rectángulo
    pygame.draw.rect(superficie, color_fondo, rectangulo, border_radius=6)
    
    # Renderiza el texto
    texto = fuente.render(f"{variable}   {variable2}", True, color_texto)
    pos_x = rectangulo.centerx - texto.get_width() // 2
    pos_y = rectangulo.centery - texto.get_height() // 2
    
    # Coloca el texto en el centro del rectángulo
    superficie.blit(texto, (pos_x,pos_y))