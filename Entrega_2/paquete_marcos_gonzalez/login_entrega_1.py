
import json

route = "D:\CoderHouse\Phyton_CO51325" #Asigno la ruta de mi google.Colab

def guardar_datos(ruta, nombre_archivo, base): #Creamos la funcion para guardar los datos en el archivo de Drive
  
  with open(ruta + nombre_archivo, "a") as f:

    for usuario in base:
      f.write(usuario["NOMBRE"] + "," + usuario["PASSWORD"]+"\n")

def obtener_datos(ruta, nombre_archivo): #Creamos la funcion para obtener los datos del archivo Drive

  with open(ruta + nombre_archivo, "r") as f:

    lista=f.readlines()

    base=[]
    
    for usuario in lista:

      users={}
      usuario_separado=usuario.split(",") #
      users["NOMBRE"]=usuario_separado[0]
      users["PASSWORD"]=usuario_separado[1]

      users["PASSWORD"]=usuario_separado[1].strip() #Eliminamos los espacios vacios

      
      base.append(users)

  return base

def comprobar_usuario(nombre, password, base): #Funcion para validar si el usuario existe

  for usuario in base:
    if usuario["NOMBRE"]==nombre and usuario["PASSWORD"]==password:
      return True
    
  return False

def registrar_usuario(nombre, password,base): #Funcion para registrar usuario

  d = {}

  d["NOMBRE"] = nombre
  d["PASSWORD"] = password

  base.append(d)
  return base

# def mostrar_usuario(usuario): #Funcion para mostrar usuario 

#   print("---------------------------")
#   print(f"    NOMBRE: {usuario[0]}")
#   print(f"    CONTRASEÑA: {usuario[1]}")
#   print("---------------------------")

