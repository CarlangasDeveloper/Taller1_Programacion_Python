print("---Años Bisiestos---")
año = int(input("Ingrese un año para saber si es bisiesto o no: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 100 == 0) and (año % 400 == 0):
    print("El año "+str(año)+" SI es bisiesto")
else:
    print("El año "+str(año)+" NO es bisiesto")
