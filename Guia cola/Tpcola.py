from cola import Cola
from heap import HeapMax

cola_personajes = Cola()
cola_aux = Cola()

personajes=[('Han Solo', 'Corellia'),('Leia Organa', 'Alderaan'),('Boba Fett', 'Kamino'),('Lando Clarissan', 'Socorro'),
            ('Bbi Wan Kenobi', 'Stewjon'),('Padmé Amidala', 'Naboo'),('Yoda', 'Desconocido'),('Chewbacca', 'Kashyyyk'),('Jar Jar Binks', 'Naboo'),
            ('Darth Vader', 'Tatooine'),('Ewoks', 'Endor'),('Luke Skywalker', 'Tatooine')]

for elemento in personajes:
    cola_personajes.arribo(elemento)

# while not cola_personajes.cola_vacia():
#     x=cola_personajes.atencion()
#     cola_aux.arribo(x)

def mostrar_personajes (cola, planeta):
    print ('Lista de personajes de', planeta)
    while (not cola.cola_vacia()):
        x = cola.atencion()
        cola_aux.arribo(x)
        if (x[1] == planeta):
            print (x[0])
    while (not cola_aux.cola_vacia()):
        cola.arribo(cola_aux.atencion())

def planeta_natal (cola, personaje):
    while (not cola.cola_vacia()):
        x = cola.atencion()
        cola_aux.arribo(x)
        if (x[0] == personaje):
            print ('El planeta natal de', personaje, 'es', x[1])
    while (not cola_aux.cola_vacia()):
        cola.arribo(cola_aux.atencion())

def insertar_personaje_antes (cola, personaje1, personaje2):
    while (not cola.cola_vacia()):
        x = cola.atencion()
        if (x[0]==personaje1):
            cola_aux.arribo(personaje2)
        cola_aux.arribo(x)
    
    while (not cola.cola_vacia()):
        cola_aux.arribo(cola.atencion())
    while (not cola_aux.cola_vacia()):
        cola.arribo(cola_aux.atencion())

def eliminar_personaje_despues (cola, personaje):
    while (not cola.cola_vacia()):
        x = cola.atencion()
        cola_aux.arribo(x)
        if (x[0]==personaje):
            break
    cola.atencion()
    while (not cola.cola_vacia()):
        cola_aux.arribo(cola.atencion())
    while (not cola_aux.cola_vacia()):
        cola.arribo(cola_aux.atencion())


# Punto a
mostrar_personajes(cola_personajes, 'Alderaan')
print ()        
mostrar_personajes(cola_personajes, 'Endor')
print ()
mostrar_personajes(cola_personajes, 'Tatooine')
print ()

#Punto B
planeta_natal(cola_personajes, 'Luke Skywalker')
planeta_natal(cola_personajes, 'Han Solo')
print ()

#punto C
personaje2 = ('Rey', 'Jakku')
insertar_personaje_antes(cola_personajes, 'Yoda', personaje2)

# Punto D
eliminar_personaje_despues(cola_personajes, 'Jar Jar Binks')


while not cola_personajes.cola_vacia():
    print (cola_personajes.atencion())
print()


# Punto 12

cola1 = Cola()
cola2 = Cola()
cola3 = Cola()

datos1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
datos2 = [10, 11, 12, 13, 14, 15, 16]


for elemento in datos1:
    cola1.arribo(elemento)
    
for elemento in datos2:
    cola2.arribo(elemento)

while not cola1.cola_vacia():
    x = cola1.atencion()
    while not cola2.cola_vacia():
        if cola2.en_frente() <= x:
            cola3.arribo(cola2.atencion())
        else:
            break
    cola3.arribo(x)

while not cola2.cola_vacia():
    cola3.arribo(cola2.atencion())

while not cola3.cola_vacia():
    print (cola3.atencion())

print()


cola_prioridad = HeapMax()

# Punto A 
cola_prioridad.arribo('DocumentoEmpleado1', 1)
cola_prioridad.arribo('DocumentoEmpleado2', 1)
cola_prioridad.arribo('DocumentoEmpleado3', 1)


# Punto B 
print(cola_prioridad.atencion()[1])
print()


#Punto C 
cola_prioridad.arribo('DocumentoTI1', 2)
cola_prioridad.arribo('DocumentoTI2', 2)


# Punto D .
cola_prioridad.arribo('DocumentoGerente1', 3)

# Punto E 
print(cola_prioridad.atencion()[1])
print(cola_prioridad.atencion()[1])
print()

#Punto F
cola_prioridad.arribo('DocumentoEmpleado4', 1)
cola_prioridad.arribo('DocumentoEmpleado5', 1)
cola_prioridad.arribo('DocumentoGerente2', 3)

#Punto G 
while (not cola_prioridad.vacio()):
    print(cola_prioridad.atencion()[1])

print()


cola_heroes = Cola()
cola_Aux = Cola()



personajes=[('Peter Parker','Spider Man','M'),('Tony Stark','Iron Man','M'),('Steve Rogers','Captain America','M'),
            ('Thor Odinson','Thor','M'),('Wanda Maximoff','Scarlet Witch','F'),('Bruce Banner','Hulk','M'),('Natasha Romanoff','Black Widow','F'),
            ('Carol Danvers','Capitana Marvel','F'),('Gamora','Gamora','F'),('Scott Lang','Ant-Man','M')]

for elemento in personajes:
    cola_heroes.arribo(elemento)

while not cola_heroes.cola_vacia():
    x = cola_heroes.atencion()
    cola_Aux.arribo(x)
    if x[0] == 'Capitana Marvel':
        print ('El nombre de la', x[1],'es:', x[0])
while not cola_Aux.cola_vacia():
    cola_heroes.arribo(cola_Aux.atencion())

while not cola_heroes.cola_vacia():
    x = cola_heroes.atencion()
    cola_Aux.arribo(x)
    if x[2] == 'F':
        print ('Los SuperHeroes Femeninos son:', x[1])
while not cola_Aux.cola_vacia():
    cola_heroes.arribo(cola_Aux.atencion())

while not cola_heroes.cola_vacia():
    x = cola_heroes.atencion()
    cola_Aux.arribo(x)
    if x[2] == 'M':
        print ('Los Superheroes Masculinos son:', x[1])
while not cola_Aux.cola_vacia():
    cola_heroes.arribo(cola_Aux.atencion())    

while not cola_heroes.cola_vacia():
    x = cola_heroes.atencion()
    cola_Aux.arribo(x)
    if x[0] == 'Scott Lang':
        print ('El nombre de', x[1],'es:', x[0])
while not cola_Aux.cola_vacia():
    cola_heroes.arribo(cola_Aux.atencion())

while not cola_heroes.cola_vacia():
    x = cola_heroes.atencion()
    cola_Aux.arribo(x)
    if x[0][0] == 'S':
        print ('Los Heroes con S son:', x)
while not cola_Aux.cola_vacia():
    cola_heroes.arribo(cola_Aux.atencion())   

while not cola_heroes.cola_vacia():
    x = cola_heroes.atencion()
    cola_Aux.arribo(x)
    if x[0] == 'Carol Danvers':
        print ('El personaje', x[0],'se encuentra en la lista y su nombre de Super Heroe es:', x[1])
while not cola_Aux.cola_vacia():
    cola_heroes.arribo(cola_Aux.atencion())

