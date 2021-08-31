from lista import Lista
lista_marvel=Lista()
lista_auxiliar=Lista()



lista1 = [
        {'nombre': 'Iron man','Año de aparicion': 2008, 'Heroe': True},
        {'nombre': 'Spider Man','Año de aparicion': 2001, 'Heroe': True},
        {'nombre': 'Thor','Año de aparicion': 2011, 'Heroe': True},
        {'nombre': 'Thanos','Año de aparicion': 2012, 'Heroe': False},
        {'nombre': 'Scalet Witch','Año de aparicion': 2014, 'Heroe': True},
     ]
for marvel in lista1:
    lista_marvel.insertar(marvel,'nombre')


lista2 = [
        {'nombre': 'Black Widow','Año de aparicion': 2010, 'Heroe': True},
        {'nombre': 'Hulk','Año de aparicion': 2008, 'Heroe': True},
        {'nombre': 'Rocket Racoonn','Año de aparicion': 2014, 'Heroe': True},
        {'nombre': 'Loki','Año de aparicion': 2011, 'Heroe': False},
     ]
for marvel in lista2:
    lista_auxiliar.insertar(marvel,'nombre')

lista_marvel.barrido()
print()


#punto A
pos=lista_marvel.busqueda('Thor', 'nombre')
if (pos != -1):
    print('Thor esta en la posicion', pos)
else:
    print('Thor no esta en la lista')

print()
#punto B
pos=lista_marvel.busqueda('Scalet Witch', 'nombre')
if (pos != -1):
    lista_marvel.obtener_elemento(pos)['nombre'] = 'Scarlet Witch'
print()
#punto C
for i in range (lista_auxiliar.tamanio()):
    pos = lista_marvel.busqueda(lista_auxiliar.obtener_elemento(i)['nombre'], 'nombre')
    if pos == -1:
        lista_marvel.insertar(lista_auxiliar.obtener_elemento(i), 'nombre')
#lista_marvel.barrido()
#print()

#punto D
print ('Barrido ascendente')
lista_marvel.barrido()
print ()
print ('Barrido descendente')
for i in range(lista_marvel.tamanio()-1, -1 ,-1):
    aux = lista_marvel.obtener_elemento(i)
    print (aux)

#punto E
for i in range(lista_marvel.tamanio()):
    aux = lista_marvel.obtener_elemento(i)
    if (i == 7):
         print ('El personaje en la posicion 7 es:' + aux['nombre'])
print()

# punto F.
print('Los personajes que tienen C o S son:')
for i in range(lista_marvel.tamanio()):
    personaje = lista_marvel.obtener_elemento(i)
    if (personaje['nombre'][0]=='C' or personaje['nombre'][0]=='S'):
        print(personaje['nombre'])

print()

#punto G
NuevaLista = Lista()
for i in range(lista_marvel.tamanio()):
    NuevaLista.insertar(lista_marvel.obtener_elemento(i), 'Año de aparicion')

print('El barrido ondenado por nombre es:')
lista_marvel.barrido()
print()
print('Barrido ordenado por año es:')
NuevaLista.barrido()