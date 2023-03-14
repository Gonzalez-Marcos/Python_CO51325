def comprar(cliente, edad):
        if edad < 18:
            print(f"{cliente.nombre} debes ser mayor de edad para poder continuar.")

        elif edad > 70:
            print(f"{cliente.nombre} debes tenes menos de 70 años, por favor comuniquese vía telefónica.")

        else:
            print(f"{cliente.nombre} puedes continuar con su compra.")
            print(cliente.get_datos_interes())
            

        