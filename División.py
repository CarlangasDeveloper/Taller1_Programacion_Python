print("---DIVISIÓN---")
print("Ingrese dos números enteros para calcular la división y saber si es exacta o no")
print("Ingrese Dividendo: ")
dividendo = int(input())
print("Ingrese Divisor: ")
divisor = int(input())

cociente = int(dividendo / divisor)
residuo = dividendo % divisor

if residuo > 0:
    print("La división entre "+str(dividendo)+" y "+str(divisor)+" NO es exacta")
else:
    print("La división entre "+str(dividendo)+" y "+str(divisor)+" SI es exacta")

print("El cociente de la división es: "+str(cociente))
print("El residuo de la division es: "+str(residuo))