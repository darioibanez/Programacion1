# Ingreso datos por Teclado
nombre = input("Ingrese su nombre: ")

#convertir a letras mayusculas
apellido = input("Ingrese su Apellido: ").upper()


edad = int(input("Ingrese su edad: "))
precio = float(input("Ingrese el precio: "))
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Edad:", edad)
print("Precio:", precio)
print(f" Tu nombre es : {nombre} y tienes : {edad} años")

#convertir a letras mayusculas
print("nombre:", nombre.upper())

#convertir a letras mayusculas
print("longitud:", nombre.__len__())
print("longitud:", len(nombre))

if edad >= 18:
    print ("mayor de edad")
else:
    print ("menor de edad")


#listas
frutas = ["uva", "pera"]

for fruta in frutas:
    print(fruta)

#incrememto de 2 en 2 
for i  in range (0,20,2):
    print (i)