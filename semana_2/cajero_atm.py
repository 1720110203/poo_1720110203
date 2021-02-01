class Cajero():

  color = None
  nombre_banco = None
  tarjeta_credito = None
  num_clientes = None
  num_cuenta = None
  modelo_cajero = None
  anio = None
  pantalla = None
  num_serie_lector = None
  modelo_pantalla = None


  def __init__(self):
    print("Clase Cajero ATM")
  
  def iniciar (self):
    print("Metodo Iniciar")
  def retiro (self):
    print("Metodo Retiro")
  def deposito (self):
    print("Metodo Deposito")
  def ver_saldo (self):
    print("Metodo Saldo")
  def hacer_pago (self):
    print("Metodo Pago")

santander = Cajero()

santander.anio = 2014
santander.color = "Rojo"
santander.modelo_cajero = "Rl5000"
santander.modelo_pantalla = "IK-91"
santander.nombre_banco = "Santander"
santander.num_clientes = 5
santander.num_cuenta = "1548 4586 4851 5115"
santander.num_serie_lector = "NCR SelfServ"
santander.pantalla = "Tactil"
santander.tarjeta_credito = "No"

print(santander.anio)
print(santander.color)
print(santander.modelo_cajero)
print(santander.modelo_pantalla)
print(santander.nombre_banco)
print(santander.num_clientes)
print(santander.num_cuenta)
print(santander.num_serie_lector)
print(santander.pantalla)
print(santander.tarjeta_credito)

santander.deposito()
santander.hacer_pago()
santander.iniciar()
santander.retiro()
santander.ver_saldo()