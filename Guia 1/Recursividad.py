 
 # Ejercicio 5
 
romanos = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 
 		    'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900,'M': 1000}
def romano_a_decimal (numero, romanos):
     if (numero == 'I'):
         return 1
     elif numero in romanos: 
         return romanos[numero]
     elif romanos[numero[0]]>=romanos[numero[1]]: 
         return romanos[numero[:1]] + romano_a_decimal(numero[1:], romanos)
     else:
         return romanos[numero[:2]] + romano_a_decimal(numero[2:], romanos) 

numero = input('Ingrese el número Romano que desea convertir en decimal: ')
numero = numero.upper()
print (numero, 'en decimal es', romano_a_decimal(numero, romanos))

# Ejercicio 8
def decimal_a_binario(num):
     if num == 0:
        return ""
     else:
         return  decimal_a_binario(num//2) + str(num % 2) 
num = input('Ingrese el número que desea tranformar a binario ')
print(decimal_a_binario(int(num)))

# Ejercicio 22
mochila = ['Pan', 'Capa', 'otro', 'Sable de luz']

def usar_fuerza(mochila, pos):
     if(pos< len(mochila)):
         if(mochila[pos] == 'Sable de luz'):
             return pos
         else:
             return usar_fuerza(mochila, pos+1)
     else:
         return -1

print(usar_fuerza(mochila, 0))



# Ejercicio 23
def salida_laberinto(matriz, x, y, caminos=[]):
    """Salida del laberinto."""
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            # print("mover este")
            salida_laberinto(matriz, x, y+1, caminos)
            # print("mover oeste")
            salida_laberinto(matriz, x, y-1, caminos)
            # print("mover norte")
            salida_laberinto(matriz, x-1, y, caminos)
            # print("mover sur")
            salida_laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1


lab = [[1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 1],
       [1, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 2]]
    
salida_laberinto(lab, 0, 0)