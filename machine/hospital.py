'''
Nombre: Maria del Pilar Lopez Morales 
Grupo: TI21
Fecha: 28/02/21
Descripccion: Crear una aplicación en Python que utilice el modelo entrenado y pregunte N cantidad de veces al usuario un texto y muestre el resultado de la clasificación.
'''
import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "1a626740-7a24-11eb-bfc3-5da53ada4701a34e3d04-140b-41b5-b88d-e3d7eebf0a3f"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

num = int(input("¿Cuantas preguntas hara? ")) 
for i in range (num):
  ask = input ("¿Cual es su pregunta? ")
  demo = classify(ask)

  label = demo["class_name"]
  confidence = demo["confidence"]


  # CHANGE THIS to do something different with the result
  print ("result: '%s' with %d%% confidence" % (label, confidence))