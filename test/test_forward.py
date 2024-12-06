import sys
import os

# Añadir el directorio src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Ahora puedes hacer importaciones relativas
from layers import *  # O lo que necesites
from activation import *
from forward import propagacion
capa = Capa()            # Sesgos (vector de longitud 2)    # Función de activación)
capa.pesos=[[0.2, 0.4], [0.5, 0.6]],  # Matriz de pesos (2x2)
capa.sesgos=[0.1, 0.2],               # Sesgos (vector de longitud 2)
capa.neuronas=[1, 0.5],               # Activaciones de entrada (vector de longitud 2)
capa.funcion_activacion=activation.sigmoid      

# Propagar hacia adelante
resultado = propagacion(capa)
print(resultado)