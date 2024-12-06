import numpy as np

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def softmax(logits):
    # Calculamos la exponencial de cada valor
    exp_logits = np.exp(logits)
    
    # Normalizamos dividiendo cada valor por la suma de todas las exponenciales
    return exp_logits / np.sum(exp_logits)
