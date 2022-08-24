def promedio():
    nota = 0
    promedio = 0
    print("Ingrese 3 notas")
    for x in range(0,3,1):
        nota = float(input())
        if x == 0:
            nota=(20*nota)//100
        elif x == 1:
            nota=(50*nota)//100
        else:
            nota=(30*nota)//100
        promedio += nota
    return promedio

print("A continuacion, ingrese las notas de 3 alumnos:")

promedio1 = promedio()
if promedio1 >= 4:
    print("El alumno aprueba")
else:
    print("El alumno desaprueba")

promedio2 = promedio()
if promedio2 >= 4:
    print("El alumno aprueba")
else:
    print("El alumno desaprueba")


promedio3 = promedio()
if promedio3 >= 4:
    print("El alumno aprueba")
else:
    print("El alumno desaprueba")

input()