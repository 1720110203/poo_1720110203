class Estudiante():

#propiedades
  nombre = None
  telefono = None
  num_materias = None
  horario = None
  seguro = None
  fecha_naci = None 
  domicilio = None 
  tutor = None
  matricula = None
  uniforme_deportivo = None

#constructor
  def __init__(self):
    print("**Clase Estudiante**")
#metodos
  def asignar_grupo(self):
    print("Metodo Asignacion Grupo")
  def asignar_beca(self):
    print("Metodo Beca")
  def dar_calif(self):
    print("Metodo Dar Calificacion")
  def hacer_examen(self):
    print("Metodo Hacer Examen")
  def ingresar_matricula(self):
    print("Metodo Matricula")

regular = Estudiante()

#valores
regular.domicilio = "Colonia Vicente Guerrero #211"
regular.fecha_naci = "19/10/11"
regular.horario = "Matutino"
regular.matricula = "VerP11720110203"
regular.nombre = "Veronica Pelcastre"
regular.num_materias = 8
regular.seguro = 84151065
regular.telefono = 7751257856
regular.tutor = "Padre"
regular.uniforme_deportivo = "Tiene"

#mostrar en pantalla
print(regular.domicilio)
print(regular.fecha_naci)
print(regular.horario)
print(regular.matricula)
print(regular.nombre)
print(regular.num_materias)
print(regular.seguro)
print(regular.telefono)
print(regular.tutor)
print(regular.uniforme_deportivo)

#invocar metodos
regular.asignar_beca()
regular.asignar_grupo()
regular.dar_calif()
regular.hacer_examen()
regular.ingresar_matricula()
 