import numpy as np
import pandas as pd

class Neuronas:
    def __init__(self, valor) -> None:
        self.activacion = valor

    def cambiar_activacion(self,valor):
        self.activacion = valor
        pass

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
        
    def agregar_capa(self, neuronas):
        nueva_capa = Capa(neuronas=neuronas)
        if self.capas:
            self.capas[-1].proxima_capa = nueva_capa
            nueva_capa.anterior_capa = self.capas[-1]
            self.capas[-1].inicializar_pesos()
        self.capas.append(nueva_capa)

    def entrenar(self):

        pass

# Ejemplo de uso
modelo = Modelo()
modelo.agregar_capa(5)  # Agrega una capa con 3 neuronas
modelo.agregar_capa(2)  # Agrega una capa con 2 neuronas y inicializa los pesos
modelo.agregar_capa(1)
modelo.agregar_capa(1)
for idx, capa in enumerate(modelo.capas):
    print(f"Capa {idx + 1}:")
    print(pd.DataFrame(capa.retornar_capa()))
    print("\n")