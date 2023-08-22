print("---LETRA O NÚMERO---")
print("Ingrese el caracter para identificar si es una letra mayuscula o minuscula o si es un número")
caracter = input("Caracter: ")

if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
    if 'A' <= caracter <= 'Z':
        print("Es letra mayúscula")
    else:
        print("Es letra minúscula")
elif '0' <= caracter <= '9':
    print("Es un número")
else:
    print("No es ni una letra ni un número.")
