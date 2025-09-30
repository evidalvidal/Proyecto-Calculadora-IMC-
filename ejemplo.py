#Inicia programa para medir IMC
print("CALCULADORA DE IMC")

#Saludar al usuario y pedir que ingrese los datos de la manera correcta
print("Bienvenido, es importante que ingreses los datos de manera adecuada")

#Ingresar identidad de usuario
identida_usu =""

#Bucle para identificar que se ejecutará mientras el usuario no ingrese solo letras en el nombre
while not identida_usu.isalpha():

    #Pedimos al usuario que ingrese su nombre
    identida_usu = input("Por favor, ingresa tu nombre: ")

    if not identida_usu.isalpha():
        print("Ingresa tu nombre, solo letras: ")

print(f"¡Bienvenido, {identida_usu}!")

#Ingresar primer apellido
prim_ape =""

#Realizamos otro bucle para que el primer apellido sea solo letras
while not prim_ape.isalpha():

    #Pedimos al usuario que ingrese su primer apellido
    prim_ape = input("Ingresa tu primer apellido: ")

    if not prim_ape.isalpha():
        print("Tipo no valido, ingresa solamente caracteres alfabeticos")

print(f"¡Gracias,")

#En esta entrada pediremos el segundo apellido al usuario, una vez más ocuparemos la función while

segun_ape = ""

while not segun_ape.isalpha():

    segun_ape = input("Continua con tu segundo apellido en caracteres aceptados: ")

    if not segun_ape.isalnum():
        print("Ingresa tu segundo apellido con caracteres alfabeticos, por favor: ")

print(f"Pasemos a la siguiente sección, {identida_usu}") 

#En esta sección pediremos los datos necesarios al usuario para calcular el IMC

estatura = float(input("Indicanos tu estatura: "))
peso = int(input("Indicanos tu peso: "))
edad = int(input("Indicanos tu edad: "))
a_nacimiento = int(input("Indicanos tu año de nacimiento: "))

#Avisamos al usuario que tenemos calculado su IMC pero que si es un niño tiene que estar en compañía de un adulto para poder verlo.

#Calculamos el IMC:

IMC = peso/estatura**2

#Hacemos la distinción entre usuarios mayores de edad y usuarios menores de edad

if(a_nacimiento>2008):
    print("Muchas gracias, pero usted es menor de edad, le enviaremos la información a sus padres")

else:
    print("Su IMC es: " + str(IMC))

    #Finalmente, hacemos las siguientes distinciones y le damos información complementaria al usuario

    if IMC >= 0 and IMC <= 15.99 :
        print (" Usted tiene delgadez severa, le sugerimos confirmar con un especialista y seguir las indicaciones dadas")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Usted tiene delgadez moderada, acuda a un especialista para confirmar la informacion")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Usted se encuentra en estado Normal, le sugerimos acudir a un especialista para confirmar esta información")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")

        #Una vez terminado el programa nos despedimos del usuario.

print("Gracias por ocupar la calculadora de IMC," + str(identida_usu))

print("¡Excelente día!")

input()



















