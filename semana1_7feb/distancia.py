class DistanciaPuntos:

  

  def __init__(self):
    print ("Clase distancia entre dos puntos") #constructor

  def formula (self, punto_ax, punto_ay, punto_bx, punto_by):
    import math #importamos math
    paso1 = pow ((punto_bx - punto_ax), 2) #se resta y se eleva  x
    paso2 = pow((punto_by - punto_ay),2)#se resta y se eleva y
    resultado = paso1 + paso2 #se suma a y b
    resulta_fin = math.sqrt (resultado) #se saca la raiz
    return resulta_fin

puntos = DistanciaPuntos()
print (puntos.formula(7,4,1,2)) #prueba
print (puntos.formula(3.17, 4.78, 4.99, 7.88))
print (puntos.formula(7.15, 21.6, 1.93, 4.38))
print (puntos.formula(12.17, 10.4, 10.4, 29.3))
print (puntos.formula(39.4, 78.9, 68.3, 187.2))
print (puntos.formula(88.7, 118.3, 295.3, 18.4))

