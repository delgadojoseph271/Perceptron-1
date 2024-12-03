import numpy as np

class Capa:
    def __init__(self, neuronas):
        self.neuronas = [0 for _ in range(neuronas)]
        self.pesos = None
        self.proxima_capa = None 
        self.anterior_capa = None
        
    def inicializar_pesos(self):
        if self.proxima_capa is not None:
            self.pesos = [np.random.uniform(0, 1, self.proxima_capa.retornar_cantidad_neuronas()) 
                          for _ in range(self.retornar_cantidad_neuronas())]
        
    def retornar_cantidad_neuronas(self):
        return len(self.neuronas)  # Calcula la cantidad de neuronas
    
    def retornar_pesos(self):
        return self.pesos  # Devuelve los pesos actuales de la capa

class Modelo:
    def __init__(self):
        self.capas = []
        
    def agregar_capa(self, neuronas):
        nueva_capa = Capa(neuronas=neuronas)
        if self.capas:
            self.capas[-1].proxima_capa = nueva_capa
            nueva_capa.anterior_capa = self.capas[-1]
            self.capas[-1].inicializar_pesos()
        self.capas.append(nueva_capa)
