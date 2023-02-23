""" 2. En la jerarquía de operadores, cuáles son los que más
prioridad tienen cuando el intérprete de Python los evalúa? """


print("los operadores de mayor gerarquia son :\n1.Parentesis:()\n2.Potencia :** ")
print("3.Multiplicacion: *\n4.Division: /\n5.Módulo o residuo: %\n6.Divicion entera: //\n ------Ejemplo------")
num1=4

num2=6
num3=2
print(f'Acontinuacion se realizara la siguiente operacion ({num1}+{num2}*{num3})**{num3} = {((num1+num2*num3)**num3)/2}')

print("---Explicacion---\n primero se resuelve lo que esta dentro de los parentesis\n y dentro de los parentesis se resuelve primero la multiplicacion (6*2=12)")
print("seguido hacemos la suma (4+12=16) y para finalizar realizamos \nlo que esta fuera de los parentesis (16**2)= 256 y seguido dividimos todo en 2= 128.8 ")
 
print()