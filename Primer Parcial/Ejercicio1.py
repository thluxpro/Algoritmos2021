#Punto A

personajes = ['Darth Vader', 'Arturito', 'Jedi Walter', 'Yoda', 'Chubaca']
pos = 0
def barrido(personajes, pos):
    if(pos < len(personajes)):
       print (personajes[pos])
       barrido(personajes,pos+1)

barrido (personajes,0)

#Punto B
def encontrar_personaje(personajes,pos):
    if(pos< len(personajes)):
        
        if(personajes[pos] == 'Yoda'): 
            return pos
        else:
            return encontrar_personaje(personajes, pos+1)
    else:
        print ('Yoda no ha sido encontrado')
        return -1

encontrar_personaje (personajes,0)

print ('Yoda esta en la posicion;: ',(encontrar_personaje(personajes, 0)))