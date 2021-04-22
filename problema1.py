import re

# Leemos el archivo txt
inputFile = open("input_problema1.txt", "r")

# Tomar los varoles por linea y eliminar caracterelcs especiales
values = inputFile.readline().split()
# Eliminamos caracteres especiales del texto
m1 = re.sub('[^A-Za-z0-9]+', '', inputFile.readline())
m2 = re.sub('[^A-Za-z0-9]+', '', inputFile.readline())
message = inputFile.readline()
cleanMessage = ""

# Limbiar duplicados del string
for char in message:
    if len(cleanMessage) == 0:
        cleanMessage = char

    elif len(cleanMessage) > 0 and cleanMessage[len(cleanMessage)-1] != char:
        cleanMessage += char

# Crear archivo output
outputFile = open("output.txt", "w+")
outputFile.write(("SI\n" if cleanMessage.find(m1) >= 0 else "NO\n") + ("SI" if cleanMessage.find(m2) >= 0 else "NO"))
outputFile.close()
