class Cliente():
    
    def __init__(self, nombre, apellido, edad, interes):
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = int(edad)
        self.interes = interes

    def __str__(self):
        return f"Se ha registrado un nuevo cliente: Bienvenido {self.nombre}"

    def get_edad(self):
        return self.__edad
    
    def get_datos_interes (self):
        return f"Los datos de interes de {self.nombre} son los siguiendes: {self.interes}"

    

