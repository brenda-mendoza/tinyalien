
class Item:
    def __init__(self, item, pos_x, pos_y) -> None:
    
        self.imagen = item[0]
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y

        self.descubierto = False
        self.recolectado = False

    @staticmethod
    def generar_monedas(num_monedas, item, inicio_x, inicio_y, espacio_entre_monedas):
        monedas = []
        for i in range(num_monedas):
            nueva_moneda = Item(item, inicio_x + i * espacio_entre_monedas, inicio_y)
            monedas.append(nueva_moneda)
        return monedas
     
    def dibujar(pantalla, item_list):
        for item in item_list: 
            if not item.recolectado:
                pantalla.blit(item.imagen, item.rectangulo)

