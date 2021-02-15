'''
Nombre: Maria del Pilar Lopez Morales 
Grupo: TI21
Fecha: 14/02/21
Descripccion: Se utilizara el bucle for para realizar un ciclo de temperatura
'''
class Temperatura:

  def __init__(self): # constructor
    pass
  
  def convertidorTemperatura (self):
    tempcalcu = 0 # cuantos hara 
    guardar_temp = [] # se creara lista
    suma = 0
    tempcalcu = int(input("Numero de temperaturas al calcular")) # leemos dato
    for temp_cel in range (tempcalcu):
      print ("Temperatura", temp_cel+1 ,": " ) # se pone +1 para iniciar en 1
      temp_cel = int(input())
      guardar_temp.append(temp_cel) # para guardar informacion append
      suma = suma+temp_cel
      temp_far = (suma *1.8)+32
      #print(temp_cel)
    res1 = suma/tempcalcu
    temp_far = (res1 *1.8)+32
    print (temp_far)
      


temp = Temperatura()
temp.convertidorTemperatura()