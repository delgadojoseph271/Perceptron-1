# **1. Introduccion** 
- Este archivo sirve como resgistro del progreso durante el desarrollo de mi red neuronal desde cero. Aqui anotare ideas, decisiones tecnicas, problemas encontrados y como los resolvi 
# **2. Progreso por Etapas**

# Capas 
- Inicio 11/30/2024 
- Finalizacion 

- Decisones clave:
    - primero dividi las capas en capa de entrada, salida y oculta pero luego simplemente decidi hace una sola clase para hacerlo mas simple
    - los pesos y neuronas los dividi en 2 listas distintas pero que se podrian unir quedaria algo similas a una matriz de neuronas y pesos

- Problemas encontrados:
    - tuve dificultades iniciales al decidir si las entradas deberian ser vectores o objetos al igual que las neuronas

# Propagacion hacia Adelante
- implementacion de la propagacion hacia adelante.
- Funcion de activacion elegida y razones
- Ejemplo de salida inicial y fu
# Restropropagacion
- Cómo implementaste el cálculo del gradiente y los ajustes de  pesos.
- Pruebas iniciales con la retropropagación y resultados.
- Reflexión sobre la tasa de aprendizaje y optimización.

# **3. Decisiones Tecnicas**
- decidi numpy para mayor optimizacion al trabajar con matrices y generar los pesos
- dividi el codigo en modulos para mayor legibilidad y escalabilidad. 
- al momento de inicializar los pesos aleatorios me decante por una **inicializacion Uniforme** con un rango de [0,1].
- utilizare mini-batches para el entrenamiento dek modelo


# **4. Problemas y Soluciones**
- al momento de crear las capas se hace inviable porque no se crean por separdo pero son dependientes una de otras
    - cree una sola clase modelo donde se gestione las capas y haga las conexiones neuronales
- al tratar de hacer el sistema de propagacion se vuelve complicado dar seguimiento a las conexiones 

# **5. Notas de Aprendizaje**
- al parecer hay forma de normalizaicon de datos aunque no indague mucho es bueno saberlo para la parte del entrenamiento(eso sera problema de otro dia)
- en el propagacion lo unico que cambian son las activaciones de la neuronas mientras que en la retropropagacion si se cambian los pesos y sesgos del modelo
- funciones de activacion punto a punto y dependientes

- Al pareccer todos los pesos son aleatorios aletorios, lo deduces facil aunque no sabia que habia distintas formas de inicializacion, **¿las distintas maneras de inicializar los pesos aleatorios afectaran en la precision del modelo?**
- Respuesta:
    si si luego lo veremos 

- las distintas tecnicas de entrenamiento de un modelo, como batch completo, Mini-batch, estocastico sus ventajas y desventajas

- paso a paso de como funciona una epoca y que procesos pasan en cada uno de de ellas


- **Proceso de Entrenamiento:**
    ___
    1. **Division en Mini-Batch**
        - El conjunto de datos de entremaniento se divide en bloques mas pequeños (mini-batches)
    2. **Para cada Mini-Batch**
        - **Propagacion hacia adelante(Forwrd Propagation):**
            - Los datos pasan por la red.
            - Se generan las activaciones y predicciones para ese mini-batch.
        - **Calculo del costo:**
            - Se compara la salida de la red con las etiquetas reales del mini-batch.
            - Se utiliza una funcion de costo (e.g., entropia cruzada, erros cuadratico medio) para calcular el error.
        - **Retropropagacion (Back Propagation):
            - Se calculan los gradientes del error respecto a los pesos y sesgos.
            - Los pesos y sesgos se actualizan utilizando el algoritmo de optimizacion elegido (e.g.,SGD,Adam).
    3. **Repetir para cada Mini-Batch:**
        - El proceso se repite hasta que se hayan procesado todos los mini-batches del conjunto de entrenamiento
    4. **Final de la Epoca:**
        - Una vez que se procesan todos los datos de entrenamiento, la red ha completado una epoca 
        ___

- **Evaluacion Despues De Una Epoca:**
    1. **Uso de los Datos de Prueba:**
        - Se utilizan los datos de prueba, que **NO** se incluyen en el entrenamiento.

        - Los datos de prueba pasan por la red usanfo **propagacion hacia adelante**.

        - Las salidas se comparan con las etiquetas reales de prueba.
    2. **Calculo de metricas:**
        - se evalua el desempeño de la red:
            - **Precisoim, F1-Score** para clasifiacacion.
            - **Error cuadratico medio (MSE)** para regresion
        - Esto indica que tan bien la red generaliza a datos nuevos.



# **6. Siguiente Pasos**
- testear el correcto funcionamiento de las capas e integracion entre ellas 
- crear el agoritmo de aprendizaje de la red

# **7. Registro Cronologico**
### [fecha: 11/30/2024]  [fecha finalizacion: 12/01/2024 ]
- creacion de la capa de entrada
### [ fecha: 01/12/2024 ] [fecha finalizacion: 02/12/2024 ]
- testo de las capas
### [ fecha: 03/12/2024 ] [fecha finalizacion: 03/12/2024 ]
- ajuste de la logica de manejo de capas y pesos
### [ fecha: 03/12/2024 ] [ fecha finalizacion: 06/12/2024 ]
- creacion de la propagacion de las neuronas y testeo 
### [ fecha: 06/12/2024] [ fecha finalizacion: 06/12/2024 ]
- creacion de las funciones de activacion y testeo 
## [ fecha: 27/12/2024 ] [ fecha finalizacion: 27/12/2024 ]
- creamos la funcion del calculo del costo y mini-batches
