class Avion():

#propiedades 
  num_serie = None
  num_pasajeros = None
  azafatas = None
  peso = None
  nombre_compania = None
  color = None
  tamaño = None
  capacidad = None
  turbinas = None
  alerones = None 

  def __init__(self):
    print("Clase Avion")
#metodos 
  def llenar_tanque (self):
    print("Metodo Llenar Tanque")
  def encender (self):
    print("Metodo Encender")
  def avanzar (self):
    print("Metodo Avanzar")
  def guardar_llantas (self):
    print("Metodo Guardar Llantas")
  def despegar (self):
    print("Metodo Despegar")

aereo = Avion()

#valores
aereo.alerones = "Alta velocidad"
aereo.azafatas = 3
aereo.capacidad = 156
aereo.color = "Blanco con Azul"
aereo.nombre_compania = "Interjet"
aereo.num_pasajeros = 99
aereo.num_serie = "Airbus 319"
aereo.peso = "7200 kg"
aereo.tamaño = "57m de longitud"
aereo.turbinas = "Turbo reactor"

#Llamamos
print(aereo.alerones)
print(aereo.azafatas)
print(aereo.capacidad)
print(aereo.color)
print(aereo.nombre_compania)
print(aereo.num_pasajeros)
print(aereo.num_serie)
print(aereo.peso)
print(aereo.tamaño)
print(aereo.turbinas)

#invocamos metodos

aereo.avanzar()
aereo.despegar()
aereo.encender()
aereo.guardar_llantas()
aereo.llenar_tanque()