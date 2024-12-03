import numpy as np

class Capa:
    def __init__(self, neuronas,):
        self.neuronas = neuronas

        self.pesos = [np.random.uniform(0, 1, self.proxima_capa.retornar_cantidad_neuronas()) 
                        for _ in range(self.retornar_cantidad_neuronas())]
    
    def retornar_cantidad_neuronas(self):
        return len(self.neuronas)  # Calcula la cantidad de neuronas
    
    def retornar_pesos(self):
        return self.pesos  # Devuelve los pesos actuales de la capa
