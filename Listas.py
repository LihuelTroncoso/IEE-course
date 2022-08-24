a = [2 * x for x in range(25)]
print(a)

palabra = str(input("Ingrese una palabra: "))
numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

listaPalabra = [palabra for palabra in palabra]
listaPalabra[numero], listaPalabra[numero2] = listaPalabra[numero2], listaPalabra[numero]

palabraNueva = "".join(listaPalabra)
print(palabraNueva)
input()