import numpy as np
import random

def calcular_suma_ponderada(capa):
    neuronas = capa.retornar_neuronas
    pesos =  capa.retornar_pesos
    return { neurona: [(peso*neurona.activacion) + neurona.sesgo for peso in pesos] for neurona in neuronas}

def hacer_minibatches(x_train,y_train,batches):
    return np.array_split(x_train, batches), np.array_split(y_train, batches)


def calcular_costo(predicciones, etiqueta):
    predicciones = predicciones
    esperado = np.array([0 if not i == etiqueta else 1 for i in range(len(predicciones)) ])
    costo = np.mean(np.square(predicciones - esperado))
    print(predicciones,esperado)
    return costo
print(calcular_costo( np.array([random.random() for _ in range(10)]) , 2))