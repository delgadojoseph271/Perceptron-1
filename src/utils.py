def calcular_suma_ponderada(capa):
    neuronas = capa.retornar_neuronas
    pesos =  capa.retornar_pesos
    return { neurona: [(peso*neurona.activacion) + neurona.sesgo for peso in pesos] for neurona in neuronas}
