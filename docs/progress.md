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


# **4. Problemas y Soluciones**
- al momento de crear las capas se hace inviable porque no se crean por separdo pero son dependientes una de otras
    - cree una sola clase modelo donde se gestione las capas y haga las conexiones neuronales
- al tratar de hacer el sistema de propagacion se vuelve complicado dar seguimiento a las conexiones 

# **5. Notas de Aprendizaje**
- al parecer hay forma de normalizaicon de datos aunque no indague mucho es bueno saberlo para la parte del entrenamiento(eso sera problema de otro dia)

- Al pareccer todos los pesos son aleatorios aletorios, lo deduces facil aunque no sabia que habia distintas formas de inicializacion, **¿las distintas maneras de inicializar los pesos aleatorios afectaran en la precision del modelo?**
- Respuesta:
    si si luego lo veremos 

# **6. Siguiente Pasos**
- testear el correcto funcionamiento de las capas e integracion entre ellas 

# **7. Registro Cronologico**
### [fecha: 11/30/2024]  [fecha finalizacion: 12/01/2024]
- creacion de la capa de entrada
### [ fecha: 01/12/2024 ] [fecha finalizacion: 02/12/2024]
- testo de las capas
### [ fecha: 03/12/2024 ] [fecha finalizacion: 03/12/2024]
- ajuste de la logica de manejo de capas y pesos
### [ fecha: 03/12/2024 ] [fecha finalizacion: 03/12/2024]
- creacion de la propagacion de las neuronas

