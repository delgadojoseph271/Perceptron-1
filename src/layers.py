import numpy as np
import pandas as pd
import activation
from forward import propagacion
from utils import hacer_minibatches

class Neuronas:
    def __init__(self, valor = 0) -> None:
        self.activacion = valor
        self.sesgo = 0

    def cambiar_activacion(self,valor):
        self.activacion = valor
        pass
    def cambiar_sesgo(self):
        self.sesgo = 0

class Capa:
    def __init__(self, neuronas=0,funcion_activacion = None):
        self.neuronas = np.array([0 for _ in range(neuronas)])
        self.sesgos  = np.array([ 0 for _ in range(neuronas)])
        self.pesos = None
        self.proxima_capa = None 
        self.anterior_capa = None
        self.funcion_activacion = funcion_activacion
        
    def inicializar_pesos(self):
        if self.proxima_capa is not None:
            self.pesos = [np.random.uniform(0, 1, self.proxima_capa.retornar_cantidad_neuronas()) 
                            for _ in range(self.retornar_cantidad_neuronas())]
        
    def aplicar_funcion_activacion(self,x):
        if self.funcion_activacion:
            return self.funcion_activacion(x)
        return x

    def retornar_cantidad_neuronas(self):
        return len(self.neuronas)  # Calcula la cantidad de neuronas
    
    def retornar_neuronas(self):
        return self.neuronas    
    
    def retornar_pesos(self):
        return self.pesos  # Devuelve los pesos actuales de la capa
    
    def retornar_capa(self):
        if self.pesos is not None:
            # Representar neuronas y sus pesos como pares clave-valor
            capa_formateada = {
                f"Neurona {i+1}": {
                    "Pesos hacia próxima capa": list(self.pesos[i])
                }
                for i in range(len(self.neuronas))
            }
            return capa_formateada
        else:
            # Si no hay pesos, solo mostrar neuronas
            return {"Neurona": [f"Neurona {i+1}" for i in range(len(self.neuronas))]}

class Modelo:
    def __init__(self):
        self.capas = []
        
    def agregar_capa(self, neuronas,funcion):
        nueva_capa = Capa(neuronas=neuronas,funcion_activacion=funcion)
        if self.capas:
            self.capas[-1].proxima_capa = nueva_capa
            nueva_capa.anterior_capa = self.capas[-1]
            self.capas[-1].inicializar_pesos()
        self.capas.append(nueva_capa)

    def entrenar(self, x_train, y_train, x_test, y_test, epocas):
        batches= 32
        x_train,y_train = hacer_minibatches(x_train,y_train, batches)
        for i in range(epocas):
            
            pass

# Ejemplo de uso
# modelo = Modelo()
# modelo.agregar_capa(5)  # Agrega una capa con 3 neuronas
# modelo.agregar_capa(2)  # Agrega una capa con 2 neuronas y inicializa los pesos
# modelo.agregar_capa(1)
# modelo.agregar_capa(1)
# for idx, capa in enumerate(modelo.capas):
#     print(f"Capa {idx + 1}:")
#     print(pd.DataFrame(capa.retornar_capa()))
#     print("\n")

