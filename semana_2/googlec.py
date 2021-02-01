class Googlec ():

  nombre_alumno = None
  nombre_profesor = None
  matricula = None
  correo = None
  compania = None
  capacidad  = None
  nombres_materia = None
  anuncios = None
  calendario = None
  anio = None


  def __init__(self):
    print("Clase Classroom")

  def iniciar_sesion (self):
    print("Metodo Incion Sesion")
  def subir_tarea (self):
    print("Metodo Subir Tarea")
  def hacer_comentario (self):
    print("Metodo Comentario")
  def dar_calificacion (self):
    print("Metodo Calificacion")
  def registro_clase (self):
    print("Metodo registro")

estudiante = Googlec()

estudiante.anio = 2019
estudiante.anuncios = "Sin Anuncio"
estudiante.calendario = "2019-2020"
estudiante.capacidad = 250
estudiante.compania = "Utec"
estudiante.correo = "1720112554@utectulancing.mx"
estudiante.matricula = 1720112554
estudiante.nombre_alumno = "Erick"
estudiante.nombre_profesor = "Eduardo"
estudiante.nombres_materia = "Ecologia"

print(estudiante.anio)
print(estudiante.anuncios)
print(estudiante.calendario )
print(estudiante.capacidad)
print(estudiante.compania)
print(estudiante.correo)
print(estudiante.matricula)
print(estudiante.nombre_alumno)
print(estudiante.nombre_profesor)
print(estudiante.nombres_materia)

estudiante.dar_calificacion()
estudiante.hacer_comentario()
estudiante.iniciar_sesion()
estudiante.registro_clase()
estudiante.subir_tarea()
