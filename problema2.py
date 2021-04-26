import re
import os

clear = lambda: os.system('cls')
clear()
exit = 1

while exit == 1:

    # Leemos el archivo txt
    fileName = input("Ingresa el nombre del archivo de texto de entrada sin la extención:\n** El archivo debe de estar en la misma carpeta que el programa **\n") + ".txt"
    inputFile = open(fileName, "r")
    content = inputFile.read()
    lines = []
        
    # Validamos la informacin del archivo
    try: 
        for line in content.split("\n"):
            values = [] 
            for value in line.split(" "):
                values.append(int(value))
            lines.append(values)
    except:
        print("\nHay valores que no son enteros en el archivo\n")
        exit = int(input("¿Desea ingresar otro archivo? Ingrese una opción: \n- 0 = No\n- 1 = Si\nIngrese la opción deseada: "))
        clear()

    errors = ""

    errors += "El valor en la linea 1 no corresponde al total de rondas capturadas en el archivo\n" if lines[0][0] != (len(lines)-1) else ""

    if errors != "":
        print(errors)
    else:

    # Tomamos la cantidad de rondas e iteramos por las lineas del archivo
        winner = ""
        bestScore = 0

        for index in range(lines[0][0]):
            # Convertir valores de cada ronda a enteros
            if index != 0:
                values = lines[index]
                
            # Calculamos el score de cada partida (siempre positivo)
            score = values[0] - values[1] if values[0] - values[1] > 0 else (values[0] - values[1]) * -1

            # Comparamos el score de la partida con el mejor score registrado
            if score > bestScore:
                bestScore = score    
                winner = "1" if values[0] - values[1] > 0 else "2"

        # Crear archivo output
        outputFile = open("output.txt", "w+")
        outputFile.write(str(winner) + " " + str(bestScore))
        outputFile.close()

        print("Archivo Output creado con exito!\n")
            
    exit = int(input("¿Desea ingresar otro archivo? Ingrese una opción: \n- 0 = No\n- 1 = Si\nIngrese la opción deseada: "))
    clear()

print("Adiós!")

