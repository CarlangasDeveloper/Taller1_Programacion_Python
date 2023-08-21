print("---Años Bisiestos---")
print("Ingrese un año para saber si es bisiesto o no: ")
año = int(input())

if año >= 1582:
    if año % 400 == 0:
        print("El año "+str(año)+" SI es bisiesto")
    else:
        print("El año "+str(año)+" NO es bisiesto")

else:
    if año % 4 == 0:
        print("El año "+str(año)+" SI es bisiesto")
    else:
        print("El año "+str(año)+" NO es bisiesto")
