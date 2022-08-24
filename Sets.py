vainilla = { "Juan", "Marina", "Tomas", "Paula" }
chocolate = { "Pedro", "Paula", "Marina" }
dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }

print("Las personas que les gustan todos los helados son: ", vainilla&chocolate&dulceDeLeche)

print("La/s persona/s a la/s que le/s gusta/n la vainilla y no el dulce de leche es/son:", vainilla-dulceDeLeche)

print("Todas las personas son: ", vainilla|chocolate|dulceDeLeche)
input()