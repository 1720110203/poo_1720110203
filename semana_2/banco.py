class Banco(): 

  #propiedades
  nom_cliente = None
  rfc_cliente = None
  Nom_banco = None
  color_banco = None
  accesibilidad = None
  salas_espera = None
  prestamos = None
  num_cuenta_cliente = None
  vencimiento_tarjeta = None
  ubicacion = None
   
  #Creamos el constructor
  def __init__(self):
    print("Clase Banco")

  #definimos los metodos
  def retiro (self):
    print("Metodo retiro")
  def deposito (self):
     print("Metodo deposito")
  def pago (self):
     print("Metodo pago")
  def crear_cuenta (self):
     print("Metodo Creacion de Cuenta")
  def giro (self):
     print("Metodo Giro")

bbva = Banco()

#damos valor a las propiedades
bbva.color_banco = "Azul"
bbva.Nom_banco = "Bancomer"
bbva.nom_cliente = "Evelyn Orduña"
bbva.num_cuenta_cliente = "1475 5487 5556 5555"
bbva.prestamos = "No hay prestamos"
bbva.rfc_cliente = "OE00864A"
bbva.salas_espera = "Llena"
bbva.ubicacion = "Tulancingo"
bbva.vencimiento_tarjeta = "07/24"
bbva.accesibilidad = "Rapida"

#motramos en pantalla
print(bbva.accesibilidad)
print(bbva.color_banco)
print(bbva.Nom_banco)
print(bbva.nom_cliente)
print(bbva.num_cuenta_cliente)
print(bbva.prestamos)
print(bbva.rfc_cliente)
print(bbva.salas_espera)
print(bbva.ubicacion)
print(bbva.vencimiento_tarjeta)

#mandamos a llamar a los metodos
bbva.retiro()
bbva.crear_cuenta()
bbva.deposito()
bbva.giro()
bbva.pago()

print("FIN")