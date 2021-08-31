from pila import Pila
from cola import Cola
class alerta(object):
    hora_alertas, nombre,  mensaje =  '', '', ''

    def __init__(self, hora_alertas, nombre, mensaje):
            self.hora_alertas = hora_alertas
            self.nombre = nombre
            self.mensaje = mensaje
            
            

alerta1 = alerta("08:30", "Twitter", "Me gusto la nueva pelicula")
alerta2 = alerta("20:15", "Facebook", "la abue subio nueva fotos") 
alerta3 = alerta("13:45", "Instagram", "Te Likearon la foto") 
alerta4 = alerta("23:00", "Instagram", "Pedro comenzo a seguirte")
alerta5 = alerta("10:20", "Twitter", "Nuevo curso de Python")

cola_alertas = Cola()
pila_alertas = Pila()

cola_alertas.arribo(alerta1)
cola_alertas.arribo(alerta2)
cola_alertas.arribo(alerta3)
cola_alertas.arribo(alerta4)
cola_alertas.arribo(alerta5)


# Punto C
def eliminacion_alertas():     
    for n in range(0, cola_alertas.tamanio()):
        aux = cola_alertas.atencion()
        if ("Facebook" != aux.nombre):
            cola_alertas.arribo(aux)
        
# Punto D
def MensajeTwitter():       
    for i in range (0, cola_alertas.tamanio()):
        aux = cola_alertas.atencion()
        if (aux.nombre == "Twitter"):
            buscado = "Python"
            mensaje = aux.mensaje
            if (0 == mensaje.find(buscado)):
                print(mensaje)
        cola_alertas.arribo(aux)

print()
MensajeTwitter()

# Punto E
def MensajeIG():        
    for n in range (0, cola_alertas.tamanio()):
        aux = cola_alertas.atencion()
        if (aux.nombre == "Instagram"):
            pila_alertas.apilar(aux)
    while (not pila_alertas.pila_vacia()):
        print(pila_alertas.elemento_cima().mensaje, "a las: ", pila_alertas.elemento_cima().hora_alertas)
        pila_alertas.desapilar()

print()
MensajeIG()