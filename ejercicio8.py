""" 
8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados. """

numero= int(input("diga un numero: "))

if numero > 0:
    if numero < 11:
        print("el numero esta entre 10 y 0")
    else:
        print("el numero es mayor a 10")
else:
    print('el numero es negativo')

