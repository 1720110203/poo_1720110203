class Futbolista():

  nombre = None
  num_jugador = None
  equipo = None
  color_uniforme = None
  tacos = None 
  posicion = None 
  estatura = None
  peso = None 
  seguro = None 
  cambio_jugador = None


  def __init__(self):
    print("Clase Futbolista")

  def iniciar_calentamiento (self):
    print("Metodo Calantamiento")
  def correr (self):
    print("Metodo Correr")
  def pasar_balon (self):
    print("Metodo Pasas Balon")
  def entrenar (self):
    print("Metodo entrenar")
  def jugar (self):
    print("Metodo Jugar")

futbol = Futbolista()

futbol.cambio_jugador = 18
futbol.color_uniforme = "Negro con blanco"
futbol.equipo = "Juventus"
futbol.estatura = "1.87"
futbol.nombre = "Cristiano Ronaldo"
futbol.num_jugador = 7
futbol.peso = 84
futbol.posicion = "Delantero"
futbol.seguro = 168165165
futbol.tacos = "Nike Mercuria"

print(futbol.cambio_jugador)
print(futbol.color_uniforme)
print(futbol.equipo)
print(futbol.estatura)
print(futbol.nombre)
print(futbol.num_jugador)
print(futbol.peso)
print(futbol.posicion)
print(futbol.seguro)
print(futbol.tacos)

futbol.correr()
futbol.entrenar()
futbol.iniciar_calentamiento()
futbol.jugar()
futbol.pasar_balon()