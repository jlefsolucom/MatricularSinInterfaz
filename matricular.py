from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from MatriculadorDAO.Consulta import obtener_datos, insertar_tarjeta

autorizantes = obtener_datos()

ids = [fila[0] for fila in autorizantes]
nombre_usuarios =[fila[1]for fila in autorizantes]

for ids,autoriza in zip(ids,nombre_usuarios):
    print(f"Numero {ids} persona: {autoriza}")

indice = int(input("Por favor ingrese el numero de persona que autoriza: "))
Padron = indice


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