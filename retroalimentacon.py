#Tipos de datos
#a=5
#b=3.14
#c="hola"
#print(type(a))
#print(type(b))
#print(type(c))

#Conversion de tipos
#x=int(3.99)
#x1=round(3.99)
#y=str(123)
#z=float("45")
#print(x,type(x))
#print(x1,type(x1))
#print(y,type(y))
#print(z,type(z))

#operacion con cadenas
#texto="Python"
#print(texto.lower())
#print(texto.upper())
#print(texto.replace("y","i"))

#Positivo, negativo, Cero
#num=int(input("ingrese un numero: "))
#if num>0:
#    print("Positivo")
#elif num<0:
#    print("Negativo")
#else:
#    print("Cero")

#Descuento por compra
#compra=float(input("Total de compra: "))
#if compra >=100:
#    print("Descuento del 10%")
#else:
#    print("sin descuento")

#Funciones
#def suma(a,b):
#    return a+b

#print(suma(3,4))

#def esPrimo(n):
#    if n<2:
#        return False
#    for i in range(2,n):
#        if n%i==0:
#            return False
#    return True
#print(esPrimo(7))

#def contarVocales(texto):
#    contador=0
#    for letra in texto.lower():
#        if letra in "aeiou":
#            contador+=1
#    return contador

#print(contarVocales("hola mundo"))

#listas
edades=[12,18,25,30,16]
for edad in edades:
    print(edad)

#agregar eliminar
edades.append(25)
edades.remove(12)
print(edades)

