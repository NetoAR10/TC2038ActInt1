import numpy as np
import os
#Funcion poara buscar palindromo
def buscar_palindromo_mas_largo(texto):
    texto_modificado = '#' + '#'.join(texto) + '#'
    n = len(texto_modificado)
    p = [0] * n
    centro = 0
    radio = 0
    max_longitud = 0
    max_pos = 0

    for i in range(n):
        espejo = 2 * centro - i
        if i < radio:
            p[i] = min(radio - i, p[espejo])

        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and texto_modificado[i + p[i] + 1] == texto_modificado[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > radio:
            centro = i
            radio = i + p[i]

        if p[i] > max_longitud:
            max_longitud = p[i]
            max_pos = i

    inicio = (max_pos - max_longitud) // 2
    fin = inicio + max_longitud - 1
    return inicio + 1, fin + 1 

# Leer texto transmission 1 y transmission 2
arhivo1=False
archivo2=False
texto=""
texto2=""
#Leer primer archivo
filename = "transmission01.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        contenido = f.read().replace("\n", "")
        texto=contenido
        arhivo1=True
print("Archivo Transmission1")
print(texto)

#Leer segundo archivo
filename = "transmission02.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        contenido = f.read().replace("\n", "")
        texto2=contenido
        archivo2=True
print("\nArchivo Transmission2")
print(texto2)

patrones=[]
#Obtener patrones maliciosos
for i in range(1,4):
    patron=""
    filename = f"mcode0{i}.txt"
    #Leer archivo de codigo malcioso 
    if os.path.exists(filename):
        with open(filename, "r") as f:
            patron = f.read().replace("\n", "")
            patrones.append(patron)
    else:
        patrones.append(0)
    print(f'\nArchivo mcode{i}')
    print(patron)

print("\nT R A N S M I S S I O N 1")
for i in range(len(patrones)):
    patro=patrones[i]
    if (not texto):
        print(f'\nmcode{i+1} Archivo transmission no válido')
    elif (patro==0):
        print(f'\nmcode{i+1} Archivo mcode no válido')
    elif (texto and patro!=0):
        print(f'\nmcode{i+1}')
        # Buscar patron con algoritmo z
        z=patro+"$"+texto
        Resultados=[]
        y=0
        for a in range(1,len(z)):
            cont=0
            x=a
            y=0
            while(y<len(patro) and x<len(z) and z[x]==patro[y]):
                cont+=1
                x+=1
                y+=1
            else:
                if(len(patro)==cont):
                    Resultados.append(a-len(patro))
        if(Resultados):
            for i in Resultados:
                print("(true) Posición inicial: "+str(i)+" Posición final: "+str(i+len(patro)-1))
        else:
            print("(false) cadena no encontrada en la transmision")

print("\nT R A N S M I S S I O N 2")
for i in range(len(patrones)):
    patro=patrones[i]
    if (not texto2):
        print(f'\nmcode{i+1} Archivo transmission no válido')
    elif (patro==0):
        print(f'\nmcode{i+1} Archivo mcode no válido')
    elif (texto2 and patro!=0):
        print(f'\nmcode{i+1}')
        # Buscar patron con algoritmo z
        z=patro+"$"+texto2
        Resultados=[]
        y=0
        for a in range(1,len(z)):
            cont=0
            x=a
            y=0
            while(y<len(patro) and x<len(z) and z[x]==patro[y]):
                cont+=1
                x+=1
                y+=1
            else:
                if(len(patro)==cont):
                    Resultados.append(a-len(patro))
        if(Resultados):
            for i in Resultados:
                print("(true) Posición inicial: "+str(i)+" Posición final: "+str(i+len(patro)-1))
        else:
            print("(false) cadena no encontrada en la transmision")


def buscar_palindromo_mas_largo(texto): #Algoritmo Manacher O(n)
    texto_modificado = '#' + '#'.join(texto) + '#'
    n = len(texto_modificado)
    p = [0] * n
    centro = 0
    radio = 0
    max_longitud = 0
    max_pos = 0

    for i in range(n):
        espejo = 2 * centro - i
        if i < radio:
            p[i] = min(radio - i, p[espejo])

        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and texto_modificado[i + p[i] + 1] == texto_modificado[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > radio:
            centro = i
            radio = i + p[i]

        if p[i] > max_longitud:
            max_longitud = p[i]
            max_pos = i

    inicio = (max_pos - max_longitud) // 2
    fin = inicio + max_longitud - 1
    palindromo = texto[inicio:fin+1]
    
    return inicio + 1, fin + 1, palindromo 

# Palindromos
print("\nP A L I N D O R M O S")
if arhivo1:
    inicio, fin, palindromo = buscar_palindromo_mas_largo(texto)
    print(f"Palíndromo más largo en Transmission1: {palindromo} (Inicio: {inicio}, Fin: {fin})")

if archivo2:
    inicio, fin, palindromo = buscar_palindromo_mas_largo(texto2)
    print(f"Palíndromo más largo en Transmission2: {palindromo} (Inicio: {inicio}, Fin: {fin})\n")
        

# Buscar cadena más grande entre dos textos
if (arhivo1 and archivo2):
    maximo=0
    cadenas1=[]
    cadenas2=[]
    a=np.zeros((len(texto),len(texto2))).astype(int)
    for j in range(len(texto)):
        for k in range(len(texto2)):
            if (texto[j]==texto2[k]):
                if j > 0 and k > 0:
                    a[j][k] = 1 + a[j-1][k-1]
                    if (a[j][k]>maximo):
                        maximo=a[j][k]
                        cadenas1=[]
                        cadenas2=[]
                        if(j not in cadenas1):
                            cadenas1.append(j)
                        if(k not in cadenas2):
                            cadenas2.append(k)
                    elif(maximo==a[j][k]):
                        if(j not in cadenas1):
                            cadenas1.append(j)
                        if(k not in cadenas2):
                            cadenas2.append(k)
                else:
                    a[j][k] = 1  # Si es la primera fila o columna, inicializar con 1
    subString=""
    for i in range(len(cadenas1)):
        if (i==0):
            for a in reversed(range(maximo)):
                subString=subString+texto[cadenas1[0]-a]
            print("Sub-String más largo: "+subString)
            print("\nPosiciones en la Transmission1:")
        subString=""
        print("Posición inicial: "+str(cadenas1[i]-maximo+2)+" Posición final: "+str(cadenas1[i]+1))
    print("\nPosiciones en la Transmission2:")
    for i in range(len(cadenas2)):
        print("Posición inicial: "+str(cadenas2[i]-maximo+2)+" Posición final: "+str(cadenas2[i]+1))
else:
    print("No se encontró un substring compartido en ambas transmiciones")