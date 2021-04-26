import re
import os

clear = lambda: os.system('cls')
clear()
exit = 1

while exit == 1:
    # Solicitamos el
    fileName = input("Ingresa el nombre del archivo de texto de entrada sin la extención:\n** El archivo debe de estar en la misma carpeta que el programa **\n") + ".txt"
    inputFile = open(fileName, "r")
    content = inputFile.read()

    lines = []
    for line in content.split("\n"):
        lines.append(re.sub('[^A-Za-z0-9 ]+', '', line))

    errors = ""
    # Validar datos del archivo
    values = lines[0].split(" ")
    
    errors += "El valor en M1 no esta entre 2 y 50\n" if int(values[0]) < 2 or int(values[0]) > 50 else ""
    errors += "El valor en M2 no esta entre 2 y 50\n" if int(values[1]) < 2 or int(values[1]) > 50 else ""
    errors += "El valor en N no esta entre 3 y 5000\n" if int(values[2]) < 3 or int(values[2]) > 5000 else ""
    errors += "El valor en M1 no corresponde al tamanio de la primera instruccion\n" if (int(values[0]) != len(lines[1])) else ""
    errors += "El valor en M2 no corresponde al tamanio de la segunda instruccion\n" if int(values[1]) != len(lines[2]) else ""
    errors += "El valor en N no corresponde al tamanio del mensaje \n" if int(values[2]) != len(lines[3]) else ""

    if errors != "":
        # Si hay errores, los imprimimos y reiniciamos el código
        print(errors)
    else:
        # Tomar los varoles por linea y eliminar caracterelcs especiales
        # Eliminamos caracteres especiales del texto
        message = lines[3]
        cleanMessage = ""

        # Limpiar duplicados del string
        for char in message:
            if len(cleanMessage) == 0:
                cleanMessage = char

            elif len(cleanMessage) > 0 and cleanMessage[len(cleanMessage)-1] != char:
                cleanMessage += char

        # Crear archivo output
        outputFile = open("output.txt", "w+")
        outputFile.write(("Si\n" if cleanMessage.find(lines[1]) >= 0 else "No\n") + ("Si" if cleanMessage.find(lines[2]) >= 0 else "No"))
        outputFile.close()

        print("Archivo Output creado con exito!\n")

    exit = int(input("¿Desea ingresar otro archivo? Ingrese una opción: \n- 0 = No\n- 1 = Si\nIngrese la opción deseada: "))
    clear()

print("Adiós!")