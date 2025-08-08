from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from MatriculadorDAO.Consulta import obtener_datos, insertar_tarjeta

def obtener_autorizacion():
    autorizantes = obtener_datos()

    ids = [fila[0] for fila in autorizantes]
    nombre_usuarios =[fila[1]for fila in autorizantes]

    for id_persona,autoriza in zip(ids,nombre_usuarios):
        print(f"Numero {id_persona} persona: {autoriza}")

    try:
            indice = int(input("Por favor ingrese el número de persona que autoriza: "))
            if indice not in ids:
                print("El valor ingresado no corresponde a ningún autorizado para crear usuarios.")
                return None
            else:
                print("Autorización válida.")
                return indice
    except ValueError:
        print("⚠️ Entrada inválida. Por favor ingrese un número entero.")
        return None
    
Padron = obtener_autorizacion()

if Padron is not None:
    print(f"ID autorizado: {Padron}")


descripcion = input("Descripcion de la persona: ")

if not descripcion or not Padron:
    print("Falta informacion para poder crear el registro")

else:
    print("Por favor acerque su tarjeta a registrar ")
    GPIO.setwarnings(False)
    reader = SimpleMFRC522()
    num_tarjeta, text = reader.read()

    #Formateo de informacion
    num_tarjeta = int(num_tarjeta)
    descripcion = descripcion.upper()

    if not num_tarjeta:
        print("Falta el numero de tarjeta a registrar")
    else:
        print(f"Tarjeta: {num_tarjeta}, padron: {Padron}, Descripcion: {descripcion}")
        insertar_tarjeta(num_tarjeta, descripcion, Padron)