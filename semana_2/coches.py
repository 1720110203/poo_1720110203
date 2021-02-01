class Coches ():

  color = None
  placas = None
  kilometraje = None
  num_puertas = None
  transmision = None
  tipo_motor = None
  cilindros = None
  quema_cocos = None
  equipo_audio = None 
  modelo = None


  def __init__(self):
    print ("Clase Coches")

  def encender (self):
    print("Metodo Encender")
  def apagar (self):
    print("Metodo Apagar")
  def reversa (self):
    print("Metodo Reversa")
  def cambio_velocidad (self):
    print("Metodo Cambio Velocidad")
  def gira_izquierda (self):
    print("Metodo Gira Izquierda")

chevy = Coches ()

chevy.cilindros = 4
chevy.color = "Rojo"
chevy.equipo_audio = "JBL"
chevy.kilometraje = 150000
chevy.modelo = 2014
chevy.num_puertas = 4
chevy.placas = "H156H5"
chevy.quema_cocos = "Si"
chevy.tipo_motor = "4 Tiempos"
chevy.transmision = "Standar"

print(chevy.cilindros)
print(chevy.color)
print(chevy.equipo_audio)
print(chevy.kilometraje)
print(chevy.modelo)
print(chevy.num_puertas)
print(chevy.placas)
print(chevy.quema_cocos)
print(chevy.tipo_motor)
print(chevy.transmision)

chevy.apagar()
chevy.cambio_velocidad()
chevy.encender()
chevy.gira_izquierda()
chevy.reversa()

