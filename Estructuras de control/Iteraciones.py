# El usuario ingresa el límite de datos recopilados 
limit = int(input("Ingresa un número mayor a 3")) 
# Muestra los números positivos en múltiplos de 3 
print("los multiplos de tres", limit, "son:") 
for i in range(3, limit + 1, 3): 
    print(i)

MIN = 1 
MAX = 20 
#La instrucción end="" al final del argumento de print, evita que el programa continue a la siguiente línea 
print(" ", end="") 
for i in range(MIN, MAX + 1): 
    print("%4d" % i, end="") 
print() 
for i in range(MIN, MAX + 1): 
    print("%4d" % i, end="") 
for j in range(MIN, MAX + 1): 
    print("%4d" % (i * j), end="") 
print()