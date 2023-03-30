from paquete_marcos_gonzalez.cliente import Cliente

from paquete_marcos_gonzalez.funciones_comprar import *

nuevo_cliente = Cliente("Marcos", "Gonzalez", 17, ["Deporte", "tecnología"])

print(nuevo_cliente)

comprar(nuevo_cliente, nuevo_cliente.get_edad())
