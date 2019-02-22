import math

# Ejercicio 1

a = 1
b = 8
c = 4

d = 4

multiplicacion = a*b*c
doble = 2*a

print('Multiplicacion = ', multiplicacion)
print('Doble A = ', doble)

# Ejercicio 2

cuadradoB = b**2
raizB = math.sqrt(4)

print('El cuadrado de B = ', cuadradoB)
print('La raiz de D = ', raizB)

# Ejercicio 3

requisito = cuadradoB - 4*a*c

if requisito > 0:
    d = math.sqrt(cuadradoB)
    
    print(d)

    if d > 0:
        x1 = -b + math.sqrt(d) / 2*a
        x2 = -b - math.sqrt(d) / 2*a
    else:
        if d == 0:
            x1 = -b / 2*a

    print('La solucion es = ', x1, x2)
else:
    print('No se puede calacular')
