import re

# Leemos el archivo txt
inputFile = open("input_problema2.txt", "r")

# Tomamos la cantidad de rondas e iteramos por las lineas del archivo
winner = ""
bestScore = 0

for line in range(int(inputFile.readline())):
    # Convertir valores de cada ronda a enteros
    values = inputFile.readline().split(" ")
    values[0] = int(values[0])
    values[1] = int(values[1])
    
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

