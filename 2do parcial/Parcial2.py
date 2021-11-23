from arbol_binario import Arbol
from grafo import Grafo

# El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
# resolver los siguientes requerimientos:
# 1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
# conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
# por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
# distintos, los códigos no pueden ser repetidos (tenga cuidado);
# 2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
# código;
# 3. realizar un barrido en orden del árbol ordenado por nombre;
# 4. mostrar toda la información del dinosaurio 00792;
# 5. mostrar toda la información de todos los T-Rex que hay en la isla;
# 6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
# cargado, su nombre correcto es Stygimoloch;
# 7. mostrar la ubicación de todos los Raptores que hay en la isla;
# 8. contar cuantos Diplodocus hay en el parque;
# 9. debe cargar al menos 15 elementos.

dinosaurios = Arbol()
dinosaurios_codigo = Arbol()

datos_dinosaurios = [{'nombre': 'T-Rex', 'codigo' : '12345', 'zona' : '7C'},
                     {'nombre': 'Raptor', 'codigo' : '23456', 'zona' : '3G'},
                     {'nombre': 'Stegosaurus', 'codigo' : '45623', 'zona' : '4B'},
                     {'nombre': 'T-Rex', 'codigo' : '78945', 'zona' : '5A'},
                     {'nombre': 'Raptor', 'codigo' : '45653', 'zona' : '1Z'},
                     {'nombre': 'Sgimoloch', 'codigo' : '159456', 'zona' : '3H'},                     
                     {'nombre': 'Diplodocus', 'codigo' : '12356', 'zona' : '1Z'},
                     {'nombre': 'T-Rex', 'codigo' : '78945', 'zona' : '5D'},
                     {'nombre': 'Raptor', 'codigo' : '75312', 'zona' : '2A'},
                     {'nombre': 'Diplodocus', 'codigo' : '15978', 'zona' : '4T'},
                     {'nombre': 'Stegosaurus', 'codigo' : '45623', 'zona' : '1C'},
                     {'nombre': 'Velociraptor', 'codigo' : '00792', 'zona' : '5V'},
                     {'nombre': 'Triceratops', 'codigo' : '0153', 'zona' : '3F'},
                     {'nombre': 'Raptor', 'codigo' : '00666', 'zona' : '5T'},
]

# Punto 2 
for dinosaurio in datos_dinosaurios:
    dinosaurios = dinosaurios.insertar_nodo(dinosaurio['nombre'], dinosaurio)

for dinosaurio in datos_dinosaurios:
    dinosaurios_codigo = dinosaurios_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

# Punto 3 
#print('Barrido ordenado por nombre:')
#dinosaurios.inorden()
#print()

# Punto 4 
#print('Informacion del dinosaurio 00792')
#dinosaurios_codigo.mostrar_dinosaurio('00792')
#print()

# Punto 5 
#print('Información de todos los T-Rex:')
#dinosaurios.mostrar_por_nombre('T-Rex')
#print()

# Punto 6 
#dinosaurios.cambiar_nombre('Sgimoloch', 'Stygimoloch')
#dinosaurios_codigo.cambiar_nombre('Sgimoloch', 'Stygimoloch')
#dinosaurios.inorden()
#dinosaurios_codigo.inorden()

# Punto 7 
#print('Ubicacion los raptores:')
#dinosaurios.mostrar_ubicacion_dinosaurio('Raptor')
#print()

# Punto 8 
#cantidad = dinosaurios.contador_dinosaurios('Diplodocus')
#print('La cantidad de Diplodocus es', cantidad)
#print()


# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
# necesarios para resolver las tareas, listadas a continuación:
# 1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# 2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;
# 3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;
# 4. encontrar el árbol de expansión mínima;
# 5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;
# 6. debe utilizar un grafo no dirigido.

red = Grafo(dirigido=False)

red.insertar_vertice('Switch 1', data = 'Switch')
red.insertar_vertice('Switch 2', data = 'Switch')
red.insertar_vertice('Router 1', data = 'Router')
red.insertar_vertice('Router 2', data = 'Router')
red.insertar_vertice('Router 3', data = 'Router')
red.insertar_vertice('Debian', data = 'Notebook')
red.insertar_vertice('Red Hat', data = 'Notebook')
red.insertar_vertice('Arch', data = 'Notebook')
red.insertar_vertice('Ubuntu', data = 'PC')
red.insertar_vertice('Mint', data = 'PC')
red.insertar_vertice('Manjaro', data = 'PC')
red.insertar_vertice('Parrot', data = 'PC')
red.insertar_vertice('Fedora', data = 'PC')
red.insertar_vertice('Guarani', data = 'Servidor')
red.insertar_vertice('MongoDB', data = 'Servidor')
red.insertar_vertice('Impresora', data = 'Impresora')

red.insertar_arista(17, 'Switch 1', 'Debian')
red.insertar_arista(18, 'Switch 1', 'Ubuntu')
red.insertar_arista(22, 'Switch 1', 'Impresora')
red.insertar_arista(80, 'Switch 1', 'Mint')
red.insertar_arista(29, 'Switch 1', 'Router 1')
red.insertar_arista(37, 'Router 1', 'Router 2')
red.insertar_arista(43, 'Router 1', 'Router 3')
red.insertar_arista(50, 'Router 2', 'Router 3')
red.insertar_arista(25, 'Router 2', 'Red Hat')
red.insertar_arista(9, 'Router 2', 'Guarani')
red.insertar_arista(61, 'Switch 2', 'Router 3')
red.insertar_arista(40, 'Switch 2', 'Manjaro')
red.insertar_arista(12, 'Switch 2', 'Parrot')
red.insertar_arista(5, 'Switch 2', 'MongoDB')
red.insertar_arista(56, 'Switch 2', 'Arch')
red.insertar_arista(3, 'Switch 2', 'Fedora')

# # Punto 2
pos = red.buscar_vertice('Red Hat')
print('Barrido en profundidad y amplitud desde Red Hat:')
red.barrido_profundidad(pos)
red.marcar_no_visitado()
print()

red.barrido_amplitud(pos)
red.marcar_no_visitado()
print()

pos = red.buscar_vertice('Debian')
print('Barrido en profundidad y amplitud desde Debian:')
red.barrido_profundidad(pos)
red.marcar_no_visitado()
print()

red.barrido_amplitud(pos)
red.marcar_no_visitado()
print()

pos = red.buscar_vertice('Arch')
print('Barrido en profundidad y amplitud desde Arch:')
red.barrido_profundidad(pos)
red.marcar_no_visitado()
print()

red.barrido_amplitud(pos)
red.marcar_no_visitado()
print()

# # Punto 3
red.camino_mas_corto('Debian', 'MongoDB')
print()
red.camino_mas_corto('Red Hat', 'MongoDB')
print()

# # Punto 4
red.arbol_expansion_minimo()
print()


# # Punto 5
red.eliminar_vertice('Impresora')
red.barrido_profundidad(0)