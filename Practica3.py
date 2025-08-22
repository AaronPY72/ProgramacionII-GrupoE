s=0
while True:
    i=int(input("Ingrese numero positivo para continuar o negativo para terminar: "))
    if i>=0:
        s+=i
    else:
        print(f"la suma de los numeros es {s}")
        break