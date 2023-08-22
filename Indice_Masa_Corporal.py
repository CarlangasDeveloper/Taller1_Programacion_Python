print("---RIESGO ENFERMADADES CORONARIAS---")
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))
edad = int(input("Ingrese su edad: "))

masa = float(peso / (estatura ** 2))

if edad >= 45 :
    if masa >= 22.0:
        print("Riesgo de sufrir enfermedades coronarias ALTO")
    else:
        print("Riesgo de sufrir enfermedades coronarias MEDIO")
else:
    if masa >= 22.0:
        print("Riesgo de sufrir enfermedades coronarias MEDIO")
    else:
        print("Riesgo de sufrir enfermedades coronarias BAJO")


