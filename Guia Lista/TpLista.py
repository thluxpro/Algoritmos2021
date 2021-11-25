from lista import Lista

#ejercicio 6

heroes = [{'nombre':'Spider Man', 'año_aparicion':1962, 'editorial':'Marvel', 'biografia':'Biografia de Spider Man'},
          {'nombre':'Iron Man', 'año_aparicion':1963, 'editorial':'Marvel', 'biografia':'Biografia de la armadura de Iron Man'},
          {'nombre':'Batman', 'año_aparicion':1939, 'editorial':'DC', 'biografia':'Biografia del traje de Batman'},
          {'nombre':'Flash', 'año_aparicion':1940, 'editorial':'DC', 'biografia':'Biografia de Flash'},
          {'nombre':'Linterna Verde', 'año_aparicion':1940, 'editorial':'DC', 'biografia':'Biografia de Linterna Verde'},
          {'nombre':'Wolverine', 'año_aparicion':1974, 'editorial':'Marvel', 'biografia':'Biografia de Wolverine'},
          {'nombre':'Dr. Strange', 'año_aparicion':1963, 'editorial':'DC', 'biografia':'Biografia de Dr. Strange'},
          {'nombre':'Mujer Maravilla', 'año_aparicion':1941, 'editorial':'DC', 'biografia':'Biografia de la Mujer Maravilla'},
          {'nombre':'Capitana Marvel', 'año_aparicion':1967, 'editorial':'Marvel', 'biografia':'Biografia de la Capitana Marvel'},
          {'nombre':'Star-Lord', 'año_aparicion':1980, 'editorial':'Marvel', 'biografia':'Biografia de Star Lord'}]

lista_heroes=Lista()

for elemento in heroes:
    lista_heroes.insertar(elemento, 'nombre')

#punto a
buscado = lista_heroes.busqueda('Linterna Verde', 'nombre')
if (buscado != -1):
    lista_heroes.eliminar(lista_heroes.obtener_elemento(buscado)['nombre'], 'nombre')
#punto b
buscado = lista_heroes.busqueda('Wolverine', 'nombre')
if (buscado != -1):
    print('Wolverine aparecio en el año:', lista_heroes.obtener_elemento(buscado)['año_aparicion'])
#punto c
buscado = lista_heroes.busqueda('Dr. Strange', 'nombre')
if (buscado != -1):
    lista_heroes.obtener_elemento(buscado)['editorial'] = 'Marvel'
# punto d
print('Estos son los personajes que contienen "traje" o "armadura" en su biografia')
for i in range(lista_heroes.tamanio()):
    personaje = lista_heroes.obtener_elemento(i)
    if ('traje' in personaje['biografia'] or 'armadura' in personaje['biografia']):
        print(personaje['nombre'])
print()

#punto e
print('Superheores que aparecieron antes de 1963 son:')

for i in range (lista_heroes.tamanio()):
    personaje = lista_heroes.obtener_elemento(i)
    if personaje['año_aparicion'] < 1963:
        print(personaje['nombre'], '', personaje['editorial'])
print()

#punto f
def casas (lista, personaje):
    """Muestra la editorial del personaje dado."""
    pos = lista.busqueda(personaje, 'nombre')
    if pos != -1:
        print ('La editorial de', personaje, 'es', lista.obtener_elemento(pos)['editorial'])

casas(lista_heroes, 'Capitana Marvel')
casas(lista_heroes, 'Mujer Maravilla')
print()

#punto g
buscado = lista_heroes.busqueda('Flash', 'nombre')
if buscado != -1:
    print(lista_heroes.obtener_elemento(buscado))

buscado = lista_heroes.busqueda('Star-Lord', 'nombre')
if buscado != -1:
     print(lista_heroes.obtener_elemento(buscado))

#punto h e i
cont_Marvel = 0
cont_DC = 0
print('Superheroes cuyo nombre comienza con B, M, o S')
for i in range(lista_heroes.tamanio()):
    personaje = lista_heroes.obtener_elemento(i)
    if (personaje['nombre'][0] == 'B' or personaje['nombre'][0] == 'M' or personaje['nombre'][0] == 'S'):
        print(personaje['nombre'])
    if (personaje['editorial'] == 'Marvel'):
        cont_Marvel += 1
    else:
        cont_DC += 1

print('Cantidad de superheroes de DC:', cont_DC)
print('Cantidad de superheroes de Marvel:', cont_Marvel)


#lista_heroes.barrido()
#print()

#ejercicio 7

lista1 = Lista()
lista2 = Lista()
lista_concatenada = Lista()

for i in range (0,10):
    lista1.insertar(i)

for i in range (0,10):
    lista2.insertar(i*2)

# lista1.barrido()
# print()
# lista2.barrido()
# print()

for i in range (lista1.tamanio()):
    lista_concatenada.insertar(lista1.obtener_elemento(i))
for i in range(lista2.tamanio()):
    lista_concatenada.insertar(lista2.obtener_elemento(i))

print('Listas concatenadas:')
lista_concatenada.barrido()
print()

cont_repetido = 0
for i in range(lista2.tamanio()):
    elemento = lista2.obtener_elemento(i)
    pos = lista1.busqueda(elemento)
    if pos == -1:
        lista1.insertar(elemento)
    else:
        cont_repetido += 1

print('Listas concatenadas sin valores repetidos:')
lista1.barrido()
print()

print('Cantidad de valores repetidos en ambas listas:', cont_repetido)

for i in range(lista1.tamanio()):
    while i < lista1.tamanio():
        print(lista1.eliminar(lista1.obtener_elemento(i)))


#Ejercicio 15

lista_entrenadores = Lista()


entrenadores = [
     {'name':'juan','torneos_ganados': 12, 'batallas_perdidas' : 5, 'batallas_ganadas': 32, 'pokemons': Lista()},
     {'name':'enzo','torneos_ganados': 2, 'batallas_perdidas' : 8, 'batallas_ganadas': 20, 'pokemons': Lista()},
     {'name':'maria','torneos_ganados': 4, 'batallas_perdidas' : 15, 'batallas_ganadas': 28, 'pokemons': Lista()},
]

pokemons = [{'name':'tyrantrum', 'nivel': 12 ,'tipo':'fuego', 'subtipo':'planta', 'entrenador': 'juan' },
            {'name':'wingull', 'nivel': 180 ,'tipo':'agua','subtipo':'volador', 'entrenador': 'juan'},
            {'name':'wolverine', 'nivel':3  ,'tipo':'fuego'  ,'subtipo':'terreno', 'entrenador': 'enzo' },
            {'name':'tyrantrum'  , 'nivel': 12 ,'tipo':'fuego'  ,'subtipo':'planta', 'entrenador': 'maria' },
            {'name':'wingull' , 'nivel': 18 ,'tipo':'agua'  ,'subtipo':'volador', 'entrenador': 'enzo' },
            {'name':'tyrantrum,'  , 'nivel': 12 ,'tipo':'fuego'  ,'subtipo':'planta', 'entrenador': 'maria' },
            {'name':'gigante' , 'nivel': 21 ,'tipo':'agua','subtipo':'volador', 'entrenador': 'juan' },
            {'name':'rayo' , 'nivel':3  ,'tipo':'fuego'  ,'subtipo':'terreno', 'entrenador': 'enzo' }
]


for entrenador in entrenadores:
    lista_entrenadores.insertar(entrenador, 'name')

for pokemon in pokemons:
    pos = lista_entrenadores.busqueda(pokemon['entrenador'], 'name')
    if(pos > -1):
        del pokemon['entrenador']
        lista_entrenadores.obtener_elemento(pos)['pokemons'].insertar(pokemon, 'name')


pos = lista_entrenadores.busqueda('enzo', 'name')

if(pos > -1):
    print(lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio())

# lista_entrenadores.barrido()



# Punto a
entre= input('ingrese el entrenador')
pos = lista_entrenadores.busqueda(entre, 'name')

if(pos > -1):
    print('la cantidad de pokemon de',entre, 'es:',lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio())

# Punto B
for i in range(lista_entrenadores.tamanio()):
    if(lista_entrenadores.obtener_elemento(i)['torneos_ganados'] > 3):
        print('los entrenadores con mas de 3 torneos ganados son:', lista_entrenadores.obtener_elemento(i)['name'])   


#punto C

maximo = 0
pos_maximo = -1

for i in range(lista_entrenadores.tamanio()):
    if(lista_entrenadores.obtener_elemento(i)['torneos_ganados'] > maximo):
        maximo = lista_entrenadores.obtener_elemento(i)['torneos_ganados'] 
        pos_maximo = i

nivel_max = 0
pos_nivel_max = -1
entrenador_max = lista_entrenadores.obtener_elemento(pos_maximo)
print('El entrenador con mayor torneos ganados es',entrenador_max['name'])

for i in range(entrenador_max['pokemons'].tamanio()):
    if(entrenador_max['pokemons'].obtener_elemento(i)['nivel'] > nivel_max):
        nivel_max = entrenador_max['pokemons'].obtener_elemento(i)['nivel']
        pos_nivel_max = i

print('Su pokemon con mayor nivel es:',entrenador_max['pokemons'].obtener_elemento(pos_nivel_max)['name'])


print(entrenador_max['name'], entrenador_max['torneos_ganados'], entrenador_max['batallas_ganadas'], entrenador_max['batallas_perdidas'])
print('pokemons: ')
entrenador_max['pokemons'].barrido()

#punto E y F
for i in range (lista_entrenadores.tamanio()):
    entrenador = lista_entrenadores.obtener_elemento(i)
    if (entrenador['batallas_ganadas']*100//(entrenador['batallas_perdidas']+entrenador['batallas_ganadas']) > 79):
        print('los entrenadores con 79% porcentaje de victoria son:',lista_entrenadores.obtener_elemento(i)['name'])
        for j in range (entrenador['pokemons'].tamanio()):
            pokemon = entrenador['pokemons'].obtener_elemento(j)
            if ((pokemon['tipo'] == 'fuego' and pokemon['subtipo'] == 'planta') or (pokemon['tipo'] == 'agua' and pokemon['subtipo']== 'olador')):
                print(entrenador['name']) 
# punto g
total=0
entren=input('ingrese entrenador')
pos = lista_entrenadores.busqueda(entren, 'name')
entrenador = lista_entrenadores.obtener_elemento(pos)
for j in range (entrenador['pokemons'].tamanio()):
    pokemon = entrenador['pokemons'].obtener_elemento(j)
    total += pokemon['nivel']

print('el promedio de niveles es:',total/entrenador['pokemons'].tamanio())

#punto j
for i in range (lista_entrenadores.tamanio()):
    entrenador = lista_entrenadores.obtener_elemento(i)       
    for j in range (entrenador['pokemons'].tamanio()):
        pokemon = entrenador['pokemons'].obtener_elemento(j)
        if pokemon['name'] == 'tyrantrum' or pokemon['name'] == 'terrakion' or pokemon['name'] == 'Wingull':
            print('Los entrenadores que poseen esos pokemon son:',entrenador['name'])

#Punto k
entren=input('ingrese entrenador')
poke=input('ingrese un pokemon')
pos = lista_entrenadores.busqueda(entren, 'name')
entrenador = lista_entrenadores.obtener_elemento(pos)
for j in range (entrenador['pokemons'].tamanio()):
    pokemon = entrenador['pokemons'].obtener_elemento(j)
    if pokemon['name'] == poke:
        print('los datos del entrenador son', entrenador)
        print('los datos del pokemon son',pokemon)



#Ejercicio 22

lista_jedis = Lista()
lista_especie = Lista()

## Puse la direccion del jedis.txt porque no lo reconocia 
file = open('/Users/lucas/OneDrive/Escritorio/aprendizaje/Guia Lista/jedis.txt', encoding="utf8")
lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1].title()
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].title().split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5].title()
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = float(jedi[7].split('\n')[0])
    if len(jedi) > 8:
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] =jedi[9]
    lista_jedis.insertar(jedi_data, 'name')
    lista_especie.insertar(jedi_data, 'species')

# punto a
# print('Listado ordenado por nombre:')
# for i in range(lista_jedis.tamanio()):
#     jedi= lista_jedis.obtener_elemento(i)
#     print(jedi['name'])
# print()

# print('Listado ordenado por especie:')
# for i in range(lista_especie.tamanio()):
#     especie= lista_especie.obtener_elemento(i)
#     print(especie['species'])
# print()

#Punto b
print('Información de Ahsoka Tano')
pos = lista_jedis.busqueda('Ahsoka Tano', 'name')
if pos != -1:
    tano = lista_jedis.obtener_elemento(pos)
    print(tano)

print('Información de Kit Fisto')
pos = lista_jedis.busqueda('Kit Fisto', 'name')
if pos != -1:
    kit = lista_jedis.obtener_elemento(pos)
    print(kit)

#punto c
print('Padawans de Luke Skywalker y Yoda:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if ('Luke Skywalker' in jedi['master'] or 'Yoda' in jedi['master']):
        print(jedi['name'], '- Master(s):', jedi['master'])
print()    

#punto d
print("Jedi humanos y twi'lek")
for i in range(lista_especie.tamanio()):
    jedi = lista_especie.obtener_elemento(i)
    if (jedi['species']=='human' or jedi['species'] == "twi'lek"):
        print(jedi['name'])

print()

#punto e
print('Jedi que comienzan con A:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if jedi['name'][0]=='A':
        print(jedi['name'])
print()
#punto f
print('Jedi que tuvieron sables de mas de un color')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if len(jedi['lightsaber_color'])>1:
        print(jedi['name'], ' - Colores:', jedi['lightsaber_color'])
print()

#punto g
print('Jedis que usaron un sable de luz amarillo o violeta:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if 'yellow' in jedi['lightsaber_color'] or 'purple' in jedi['lightsaber_color']:
        print(jedi['name'])

print()

#punto h
print('Padawans de Qui-Gon Jin y Mace Windu:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if ('Qui-Gon Jin' in jedi['master'] or 'Mace Windu' in jedi['master']):
        print(jedi['name'], '- Master(s):', jedi['master'])
print()