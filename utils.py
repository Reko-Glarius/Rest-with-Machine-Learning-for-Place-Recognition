import keras
from keras.models import load_model
from keras.utils import to_categorical

import numpy as np

#def create_model():
#    model = load_model("PPM.h5py")
#    return model

def transformation(image):
    image = np.array(image, dtype=np.uint8)
    image = image.astype('float32')
    image = image/255
    return image

def prediction(image):
    model = load_model("PPM.h5py")
    result = model.predict(image)
    result = np.argmax(result[0])
    return int(result)

def place_data(id):
    if(id==0):
        return { 'ID': 1, 'Resultado': 'Montaña'}
    elif (id == 1):
        return { 'ID': 2, 'Resultado': 'Desconocido'}
    elif (id == 2):
        return { 'ID': 3, 'Resultado': 'Cuerpo de Agua'}
    elif (id == 3):
        return { 'ID': 4, 'Resultado': 'Ciudad'}
    elif (id == 4):
        return { 'ID': 5, 'Resultado': 'Bosque'}