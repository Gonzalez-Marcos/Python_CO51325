from login_entrega_1 import *

list_users = [] #Creamos una lista vacia

while True: #Iniciamos un while con 4 opciones donde en cada una de ellas se aplica la funcion segun corresponda.

    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Admin")
    print("4. Salir")

    entrar = input('Ingrese una opción: ')

    if entrar == "1":

      user = input('Ingrese su nombre: ')

      password = input('Ingrese una contraseña: ')

      

      registrar_usuario(user, password, list_users) #Guardamos el usuario registrado en la lista

      guardar_datos(route, "/Users.txt", list_users ) #Guardamos los usuarios de la lista en la base de datos.

      print(f'Bienvenid@ al sistema {user}')
      
    elif entrar == "2":
      user = input('Ingrese su nombre: ')

      password = input('Ingrese una contraseña: ')

      if comprobar_usuario(user, password, list_users): #Validamos si el usuario existe en la base, sino imprime el error.

        print(f'Bienvenid@ {user}')

        # mostrar_usuario(user)
      
        break

      else:
        print('Usuario o contraseña inválida.')

    elif entrar == "3":
        
      user = input('Ingrese su nombre: ')
      password = input('Ingrese una contraseña: ')

      if comprobar_usuario(user, password, list_users):#Opcion en caso de administrador, falta implementar el usuario admin.

        print('a. Ver lista de usuarios registrados')
        print('b. Salir')
        opcion = input('Ingrese la opción: ')
        
        if opcion == "a":

          list_users = obtener_datos(route, "/Users.txt")

          print(list_users)

          break

        elif opcion == "b":

          break

        else:

          print('Opcion invalida.')
    
    elif entrar == "4":

      break

    else:

      print("Opcion invalida")
