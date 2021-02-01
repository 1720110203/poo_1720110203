class Vacaciones():

  lugar_viajar =  None
  personas_viajar = None
  hora_llegada = None
  comida = None
  turistas = None
  compras = None
  recorrido_turistico = None
  estacion_anio = None
  lugar_donde_queda = None
  dias_estadia = None

  def __init__(self):
    print("Clase Vacaciones")

  def inician (self):
    print("Metodo Inician")
  def comprar_boletos_avion(self):
   print("Metodo Comprar boletos")
  def terminan (self):
    print("Metodo Terminan")
  def reservar_hotel (self):
    print("Metodo Reserva hotel")
  def tiempo_hotel (self):
    print("Metodo Tiempo Hotel")

verano = Vacaciones()

verano.comida = "Bufed"
verano.compras = "Ropa para playa"
verano.dias_estadia = 5
verano.estacion_anio = "Verano"
verano.hora_llegada = "7:00am"
verano.lugar_donde_queda = "Hotel"
verano.lugar_viajar = "Playa del carmen"
verano.personas_viajar = 6
verano.recorrido_turistico = "Playa"
verano.turistas = 12

print(verano.comida)
print(verano.compras)
print(verano.dias_estadia)
print(verano.estacion_año)
print(verano.hora_llegada)
print(verano.lugar_donde_queda)
print(verano.lugar_viajar)
print(verano.personas_viajar)
print(verano.recorrido_turistico)
print(verano.turistas)

verano.comprar_boletos_avion()
verano.inician()
verano.reservar_hotel()
verano.terminan()
verano.tiempo_hotel()
