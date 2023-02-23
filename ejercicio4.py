
""" 
4. Que son las expresiones regulares en Python? """

print("\nQue son las expresiones regulares en Python?")
print(" Son unas secuencias de caracteres que forma un patrón de búsqueda,\n las cuales son formalizadas por medio de una sintaxis específica.\n Los patrones se interpretan como un conjunto de instrucciones")
print(f"---Ejemplo---\n ")
"""importamos el modulo "re" """
import re 

texto="profe esto lo estoy haciendo yo XD, pero claramente me estoy apoyando de internet"
patron = re.compile('esto lo estoy haciendo yo')

print(patron.match(texto))
print(patron.search(texto))#la diferencia entre search y match es que match me devuel un None en consola si la
                           #cadena que busco no se encuenra el inicio y el search me muestra el texto asi no este en el inicio
