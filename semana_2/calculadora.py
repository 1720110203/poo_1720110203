class Calculadora():

    tamano = None
    num_serie = None
    tipo = None
    color = None
    solar = None
    num_ingresar = None
    letras = None
    tipo_pila = None
    marca = None
    tamano_pantalla = None

    def __init__(self):
        print("Clase Calculadora")

    def opera_suma(self):
        print("Metodo Suma")

    def opera_resta(self):
        print("Metodo Resta")

    def opera_multiplicacion(self):
        print("Metodo Multiplicacion")

    def opera_division(self):
        print("Metodo Division")

    def prender(self):
        print("Metodo Prender")


operacion = Calculadora()

operacion.color = "Gris"
operacion.letras = "A B C X Y X Z N M"
operacion.marca = "Casio"
operacion.num_ingresar = "0123456789"
operacion.num_serie = "DX-189"
operacion.solar = "Si"
operacion.tamano = "23.5 x 17.2"
operacion.tamano_pantalla = "LCD"
operacion.tipo = "Cientifica"
operacion.tipo_pila = "Redonda"

print(operacion.color)
print(operacion.letras)
print(operacion.marca)
print(operacion.num_ingresar)
print(operacion.num_serie)
print(operacion.solar)
print(operacion.tamano)
print(operacion.tamano_pantalla)
print(operacion.tipo)
print(operacion.tipo_pila)

operacion.opera_division()
operacion.opera_multiplicacion()
operacion.opera_resta()
operacion.opera_suma()
operacion.prender()
