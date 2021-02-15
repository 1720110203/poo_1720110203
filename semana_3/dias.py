'''
Nombre: Maria del Pilar Lopez Morales 
Grupo: TI21
Fecha: 14/02/21
Descripccion: Se utilizara el bucle for para realizar el programa de días
'''
class Dias:

  def __init__ (self): # se hace el constructor
    pass 

  def bucleDia (self):
    calculo = 0 # variable 
    calculo = int(input("Numeros de calculo a realizar: "))
    for rdia in range (calculo):
        print ("Dia: ")
        ndia=int(input())
        rdia=(((ndia*24)/1)*3600)/1
        print(rdia)
    print ("***FIN***")

dia = Dias()
dia.bucleDia()