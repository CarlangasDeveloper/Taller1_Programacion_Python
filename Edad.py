from time import localtime
t = localtime()
dia_actual = t.tm_mday
mes_actual = t.tm_mon
año_actual = t.tm_year

print("---EDAD---")
print("Ingrese su fecha de nacimiento")
dia_nacimiento = int(input("Dia: "))
mes_nacimiento = int(input("Mes: "))
año_nacimiento = int(input("Año: "))

edad = año_actual - año_nacimiento - ((mes_actual, dia_actual) < (mes_nacimiento, dia_nacimiento))

if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    print("No ha cumplido años aún")
else:
    print("Ya cumplió años")


print("Su edad es: "+str(edad)+" años")
