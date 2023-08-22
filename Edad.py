from time import localtime
t = localtime()
dia = t.tm_mday
mes = t.tm_mon
año = t.tm_year

print("---EDAD---")
print("Ingrese su fecha de nacimiento")
dia2 = int(input("Dia: "))
mes2 = int(input("Mes: "))
año2 = int(input("Año: "))

edad = año-año2 - ((mes, dia) < (mes2, dia2))

print("Su edad es: "+str(edad)+" años")
