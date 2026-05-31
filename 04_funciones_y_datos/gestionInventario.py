inventarioTienda = {"Manzanas": 50, "Peras": 30}

def actualizarStock(producto, cantidad):
    inventarioTienda[producto] = inventarioTienda.get(producto, 0) + cantidad

actualizarStock("Manzanas", 10)
print(inventarioTienda)