from pila import Pila
import random

# Ejercicio 14
pila_numeros = Pila()
pila_aux = Pila()

datos = [random.randint(0,1000) for _ in range(10)]


for i in range (0, len(datos)):
    numero = datos[i]

    if (pila_numeros.pila_vacia()):
        pila_numeros.apilar(numero)
    else:
        if (numero >= pila_numeros.elemento_cima()):
            pila_numeros.apilar(numero)
        else:
            while (not pila_numeros.pila_vacia() and pila_numeros.elemento_cima() > numero):
                pila_aux.apilar(pila_numeros.desapilar())
            
            pila_numeros.apilar(numero)
            
            while(not pila_aux.pila_vacia()):
                pila_numeros.apilar(pila_aux.desapilar())
while (not pila_numeros.pila_vacia()):
    print(pila_numeros.desapilar())

#Ejercicio 16
pila_empire = Pila()
pila_awakens = Pila()
pila_interseccion = Pila()
pila_aux = Pila()

empire = ['Han Solo', 'Luke Skywalker', 'Leia Organa', 'Lando Calrissian', 'Darth Vader', 
           'Chewbacca', 'Yoda', 'Boba Fett','Obi-Wan Kenobi', 'R2-D2', 'C-3PO']
awakens = ['Rey', 'Finn', 'Poe Dameron' ,'Leia Organa', 'Luke Skywalker', 'Han Solo', 'Kylo Ren',
            'Chewbacca', 'R2-D2', 'C-3PO', 'Maz Kanata']

for elemento in empire:
    pila_empire.apilar(elemento)

for elemento in awakens:
    pila_awakens.apilar(elemento)

while not pila_empire.pila_vacia():
    e = pila_empire.desapilar()
    
    while not pila_awakens.pila_vacia():
        a = pila_awakens.desapilar()
        if (e == a):
            pila_interseccion.apilar(e)
        else:
            pila_aux.apilar(a)

    while not pila_aux.pila_vacia():
        pila_awakens.apilar(pila_aux.desapilar())

print ('Los personajes que aparecen en ambas películas son:')
while not pila_interseccion.pila_vacia():
    print ('-', pila_interseccion.desapilar())


pila_din = Pila()
pila_fett = Pila()
pila_aux = Pila()

datos_din = [('Genoba', 'Leia Organa', 60000), ('Dagobah', 'Maz Kanata', 32000), ('Naboo', 'Rey', 25000), 
             ('Kashyyk', 'Chewbacca', 150000)]
datos_fett = [('Naboo', 'R2-D2', 80000),('Kashyyk', 'Lando Calrissian', 75000),('Naboo', 'Leia Organa', 60000),
             ('Genoba', 'Chewbacca', 150000),('Tatooine', 'Han Solo', 224190),('Dagobah', 'Finn', 90000)]

for elemento in datos_din:
    pila_din.apilar(elemento)

for elemento in datos_fett:
    pila_fett.apilar(elemento)

total_din = 0
while(not pila_din.pila_vacia()):
    x = pila_din.desapilar()
    pila_aux.apilar(x)
    total_din += x[2]

print ('capturas de Din Djarin:', pila_aux.tamanio())
print ('Planetas visitados:')
while (not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    print (x[0]) 
    pila_din.apilar
print ()

total_fett = 0
while(not pila_fett.pila_vacia()):
    x = pila_fett.desapilar()
    pila_aux.apilar(x)
    total_fett += x[2]
    if x[1] == 'Han Solo':
         print ('El número de la mision de captura de Han Solo es', pila_fett.tamanio())

print ('apturas de Boba Fett:', pila_aux.tamanio())
print ('Planetas visitados:')

while (not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    print (x[0]) 

print ()

print ('Total creditos de Din Djarin:', total_din)
print ('Total creditos de Boba Fett:', total_fett)

if (total_din>total_fett):
     print ('Din Djarin recaudo mas dinero')
elif (total_din<total_fett):
     print ('Boba Fett recaudo mas dinero')
else:
    print ('Recaudaron lo mismo.')

# Ejercicio 24
pila_MCU = Pila ()
pila_aux = Pila ()
pila_5 = Pila()
pila_CDG = Pila()

personajes = [('Iron Man', 11),('Captain America', 11),('Groot', 4),('Black Widow', 10),('Thor', 8),
            ('Hulk', 8),('Hawkeye', 5),('Bucky Barnes', 7),('Wanda Maximoff', 5),('Captain Marvel', 2),
            ('Star-Lord', 4),('Rocket Raccoon', 4),('Gamora', 4),('Black Panther', 4)]

for elemento  in personajes:
    pila_MCU.apilar(elemento)

while not pila_MCU.pila_vacia():
    x = pila_MCU.desapilar()
    pila_aux.apilar(x)
    if x[0] == 'Rocket Raccoon' or x[0] == 'Groot':
        print (x[0], 'se encuentra en la posicion', pila_aux.tamanio())

while not pila_aux.pila_vacia():
    pila_MCU.apilar(pila_aux.desapilar())

while not pila_MCU.pila_vacia():
    x = pila_MCU.desapilar()
    pila_aux.apilar(x)
    if x[1] > 5:
        print( x[0], 'Aparece en', x[1], 'peliculas')

while not pila_aux.pila_vacia():
    pila_MCU.apilar(pila_aux.desapilar())

while not pila_MCU.pila_vacia():
    x = pila_MCU.desapilar()
    pila_aux.apilar(x)
    if x[0] == 'Black Widow':
        print ('Black Widow aparecio en', x[1], 'peliculas.')

while not pila_aux.pila_vacia():
    pila_MCU.apilar(pila_aux.desapilar())

while not pila_MCU.pila_vacia():
    x = pila_MCU.desapilar()
    pila_aux.apilar(x)
    if x[0][0] == 'C' or x[0][0] == 'D' or x[0][0] == 'G': 
        print(x[0], 'Empiza con la letra C, D o G')
while not pila_aux.pila_vacia():
    pila_MCU.apilar(pila_aux.desapilar())