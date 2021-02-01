class Serie():

  genero = None
  actores = None
  presupuesto = None
  camaras = None
  num_equipo_maquillaje = None
  guion = None
  reparto = None
  num_estudio = None 
  vestuario = None
  reflectores = None


  def __init__(self):
    print("Clase Serie Tv")

  def iniciar_grabacion (self):
    print("Metodo Inicio grabacion")
  def terminar_grabacion (self):
    print("Metodo Temina grabacion")
  def cortar_grabacion (self):
    print("Metodo cortar grabacion")
  def editar_grabacion (self):
    print("Metodo Editar grabacion")
  def repetir_escena (self):
    print("Metodo Repetir escena")

terror = Serie()

terror.actores = "Bill Skarsgård"
terror.camaras = "infraroja"
terror.num_equipo_maquillaje = 6
terror.genero = "Terror"
terror.guion = "guion cinematografico"
terror.num_estudio = 8
terror.presupuesto = "1.1 m"
terror.reparto = "principal"
terror.vestuario = "payaso"
terror.reflectores = "Blanco"

print(terror.actores)
print(terror.camaras)
print(terror.genero)
print(terror.guion)
print(terror.num_equipo_maquillaje)
print(terror.num_estudio)
print(terror.presupuesto)
print(terror.reflectores)
print(terror.reparto)
print(terror.vestuario)

terror.cortar_grabacion()
terror.editar_grabacion()
terror.iniciar_grabacion()
terror.repetir_escena()
terror.terminar_grabacion()