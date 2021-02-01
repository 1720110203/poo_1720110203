class Coche():
  #valor a las propiedades
  color = None
  matricula = None
  freno_mano = None
  llantas = None

  #definimos el constructor 
  def __init__(self):
    print("Clase coche")
  #definimos el metodo
  def arrancar (self):
    print("Metdodo Arrancar")
  def apagar (self):
    print("Metdodo Apagar")


#creamos el objeto
vocho = Coche()
#les damo valor a las propiedades
vocho.color = "rojo"
vocho.matricula = 6481
vocho.freno_mano = "si"
vocho.llantas = 4
#mostramos los valores 
print(vocho.color)
print(vocho.matricula)
print(vocho.freno_mano)
print(vocho.llantas)

#lo invocamos
vocho.arrancar()
vocho.apagar()