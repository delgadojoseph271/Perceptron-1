import numpy as np

def propagacion(capa):
    pesos = capa.pesos[0]
    activacion = capa.neuronas[0]
    sesgos = capa.sesgos
    funcion_activacion = capa.funcion_activacion
    z = np.dot(pesos, activacion) + sesgos
    return funcion_activacion(z)