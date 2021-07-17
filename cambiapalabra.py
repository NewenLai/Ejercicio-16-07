import sys

argumentos = sys.argv

while len(argumentos) <4:
    if len(argumentos) < 2:
        try:
            x, y, z = input("Por favor introduzca nombre de fichero, palabra original y palabra nueva: ").split()
            argumentos.extend((x, y, z))
        except:
            print("Introduce todos los parametros por favor")
        
    elif len(argumentos) < 3:
        try:
            x, y = input("Por favor introduzca palabra original y palabra nueva: ").split()
            argumentos.extend((x, y))
        except:
            print("Introduce todos los parametros por favor") 
    else:
        argumentos.append(input("Por favor introduzca palabra nueva: "))

nombreF = argumentos[1]
original = argumentos[2]
nueva = argumentos[3]


f = open(nombreF, "r")  

texto_original = f.read()
f.close()

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreF, "w")
f.write(texto_sustituido)
f.close()