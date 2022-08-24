def verificarLetraEnPalabra(palabra, letra):
    if letra in palabra:
        return letra
    else:
        return False

def ahorcado(palabra):
    contador = 0
    adivinar = False
    while adivinar!=True:
        contador += 1
        letra = input("Ingrese una letra: ")
        letraIngresada = verificarLetraEnPalabra(palabra, letra)
        if letraIngresada != False:
            palabra = palabra.replace(letraIngresada, "")
        if len(palabra) == 0:
            adivinar = True
    return contador
    
palabra = input("Ingrese una palabra: ")
contador = ahorcado(palabra)
print(contador)