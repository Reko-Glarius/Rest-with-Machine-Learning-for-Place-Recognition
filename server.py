"""
Nombre del proyecto: API REST WITH MACHINE LEARNING

Equipo Desarrollador:
    -Ricardo Aliste G. (Desarrollador)

Resumen del proyecto:
    El proyecto consta del desarrollo de una API REST, la cual conste de N servicios:

    1)[BLANK]: Direccion inicial, entrega la informacion de las rutas disponibles actualmente

    2)Prediction: Tras recibir una imagen de 100X100, un modelo de redes neuronales estima que lugar es entre
                  5 posibilidades: Montaña, Ciudad, Bosque, Cuerpo de Agua y Desconocido

* Para mas informacion, consultar el README del repositorio '' *
"""

from flask import Flask, escape, request, jsonify
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import os
from utils import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST','GET','PUT'])
def index_page():
    return jsonify({
        'Mensaje': 'Bienvenido a mi primer servicio REST con Machine Learning, a continuacion se presentan las rutas del mismo',
        'Ruta 1': '/prediction (Metodo POST)'
    })

@app.route('/prediction', methods=['POST'])
def generar_top():
    if (request.method == 'POST'):
        #image=request.files['file'].read()
        image = request.files['file']
        filename = secure_filename(image.filename)  # save file
        image.save('IMG/'+filename)
        image = plt.imread('IMG/'+filename)
        os.remove('IMG/'+filename)
        image = transformation([image])
        print(image.shape)
        result = prediction([image])
        Jsons=place_data(result)
        return jsonify(Jsons), 200

if(__name__=='__main__'):
    app.run()