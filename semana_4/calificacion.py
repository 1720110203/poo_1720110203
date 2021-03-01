'''
Nombre: Maria del Pilar Lopez Morales 
Grupo: TI21
Fecha: 21/02/21
Descripccion: Desarrollar un programa en Python que indique si un alumno tiene derecho o no tiene derecho a presentar evaluación ordinaria
'''
class Calificaciones():
    
    def __init__(self):
      pass
    
    def califica (self):
      # variables
      materia = None
      num_alumno = None
      nom_alumno = None
      num_clases = None
      faltas = None
      retardo = None
      # i=0
      
      while True:
        #i += 1
        materia = input("Materia: ")
        num_alumno = int(input("Numero de alumno:  "))
        nom_alumno = input("Nombre del alumno: ")
        num_clases = int(input("Numero de clases:  "))
        faltas = int(input("Numero de faltas: "))
        retardo = int(input("Numero de retados: "))
        while retardo <= 3:
          asistencia = num_clases - faltas
          porcentaje = (asistencia/num_clases)*100
          print("Porcentaje de Asistencia {} : ".format(porcentaje)) #format devuelve valor
          if porcentaje <= 80:
            print ("RESULTADO: No tiene derecho a evaluacion")
          else:
            print ("RESULTADO: Tiene derecho a evaluacion")
            
          # hacemos condicional para cerrar el programa 
          cerrar = input("Desea ingresar otra evaluacion: S/N  ")
          
          if cerrar != "S":
            print ("***Fin***")
          break
   
calif = Calificaciones()
calif.califica()