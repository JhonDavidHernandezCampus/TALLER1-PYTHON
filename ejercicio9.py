from datetime import datetime
now = datetime.now()
año = now.year
""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

nombre=input("Cual es el nombre del empleado: ")
apell=input("Cuales son sus apellidos: ")
añoIgreso=int (input("En que año ingreso a la empresa: "))
tel=float(input("Cual es el numero de telefono del empleado: "))
edad=int (input("cuantos años tiene el empleado: "))

print(f'El empleado {nombre} {apell} tiene {año-añoIgreso} de antiguedad')