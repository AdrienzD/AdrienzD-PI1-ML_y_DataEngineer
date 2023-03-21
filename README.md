# <h1 align=center>PROYECTO INDIVIDUAL
## <h1 align=center> DATA SCIENCE </h1>


![](https://blog.soyhenry.com/content/images/2021/02/HEADER-BLOG-NEGRO-01.jpg)





## **INTRODUCCIÓN**


Para dar una idea al lector, voy a comentar antes de comenzar el desarrollo del proyecto algunas de las pautas de inicio del mismo.

- Rol a desarrollar: Data Scientist de una start-up que provee servicios de agregación de plataformas de streaming.

- Objetivo: Solucionar un problema de negocio, crear un sistema de recomendación.

- Propuesta de trabajo es la siguiente:

		Transformaciones: Es necesario realizar trabajo de Data Engenieer, con las bases de datos proporcionadas realizar un modelado y limpieza de los datos.

		Desarrollo de una API: Con el fin de disponibilizar los datos de la empresa usando el framework FastAPI.
		
		Deployment: Cargar los archivos creados, para que todos los usuarios puedan acceder de manera sencilla a ellos.

		Análisis exploratorio de los datos: Establecer un plan de manejo para descubrir puntos importantes para desarrollar un modelo de Machine Learning.

		Sistema de recomendación: El objetivo final es plantear la solución al problema con este sistema, debe quedar funcional y amigable, a punto de consumir.

		Video: Se encontrará la documentación en forma visual, para que sea fácil y rápida de entender y explorar.


### PLANTEO DEL PROBLEMA


Se observan los archivos que hay en la carpeta Datasets, y se decide trazar la ruta de trabajo, para día a día cumplir con pequenas tareas y poder entregar el producto a la empresa.


En resumen los pasos son a grandes rasgos: ETL-API-EDA-MODELO MACHINE LEARNING- DEPLOYS.


### ETL


El el proceso que consta de tres etapas: Extracciónn (Extraction), Transformación (Transformation) y Carga (Load). Ahora lo voy utilizar para mover y transformar datos desde su origen original a una ubicación donde puedan ser analizados y luego utilizados para una aplicación de Machine Learning con la que se busca dar solución al problema.

Cuento con bases de datos crudas, en formato CSV, paso a transformarlas haciendo uso de Python y sus librerías de recursos como lo son Pandas y Numpy. 


Una vez en formato amigable, empiezo la transformación, que incluye arreglo de fechas, tipos de datos, tratamiento de nulos, entre otras. Pero antes de empezar el camino hago una division importante de los datos, por un lado uno cuatro DataFrames que contiene información pertinente a las plataformas, y por el otro me quedo con un DataFrame que contiene los ocho restantes provenientes de los datos de usuarios.


De cara a la siguientes etapas, determino el campo *'scored'* resultante del calculo del promedio de los puntajes de los usuarios. Por otro lado, uno ambos DataFrames en uno solo, usando como punto de encuentro el campo *'id'* y sumando el anterior. 


## **DESARROLLO**
  
1.  El proceso se llevó a cabo de acuerdo a las especificaciones de la empresa, [ETL](https://github.com/AdrienzD/ML_y_DataEngineer/blob/main/ETL.ipynb) 

  
### API


Usando la herramienta **FastAPI** se crea una API, que básicamente es un interfaz de programación de aplicaciones, para una experiencia más visual de código de Python. Esta es una opción popular para construir APIs rápidas y escalables en Python, por eso manos a la obra con ella.


La API, sera usada para disponibilizar la información de la empresa y hacer consultas a la base de datos, cuando la desplieguen podrán buscar información obtenida de las siguientes funciones:


- **Película con mayor duración**: Esta función devuelve el título de la película o serie con la duración más larga que cumpla con ciertas condiciones. Tiene tres argumentos opcionales: year, platform y duration_type.


- **Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año**: Esta función recibe tres parámetros platform, scored y year, que son utilizados para filtrar el DataFrame que contiene información sobre pelídculas y se devuelve cantidad como la cantidad de veces que se cumplieron las condiciones.


- **Cantidad de películas por plataforma con filtro de PLATAFORMA**: Esta cuenta la cantidad de películas que hay en el DataFrame agrupadas por plataforma y luego devuelve la cantidad total de películas en una plataforma.


- **Actor que máss se repite segúan plataforma y año**: Esta función se encarga de encontrar el actor que más aparece en películas de una plataforma y añ específicos.

## **DESARROLLO**
  
  - **Ingreso al [link](https://consultas-en-deploy.onrender.com/docs) de consultas**
  
  En dicho enlace podremos hacer las consultas, dandole click a Try it out. y rellenando los cuadros que nos mencionan.
  
  - **Ingreso al [main](https://github.com/AdrienzD/ML_y_DataEngineer/blob/main/main.py)) de la Api **

### EDA


"Exploratory Data Analysis" o "Análisis Exploratorio de Datos" en español. Es un proceso clave en el desarrollo de modelos de Machine Learning ya que ayuda a comprender mejor los datos que se utilizarán para entrenar y validar el modelo.


Por esto con el DataSet completo que resulto del ETL, realizo una exploración exhaustiva de los datos mediante técnicas estadísticas y gráficas para comprender mejor la distribución, los patrones, las relaciones y las posibles inconsistencias en los datos, etc.


Finalmente puedo determinar así la variable objetivo para el Sistema de Recomendación, esta es el **'score'**, como también defino las variables que lo van a acompañar.


Debido a la cantidad de registros con los que cuento y los recursos que poseo, determino que la opción más viable para poder trabajar con el modelo de los datos es reducir el el Dataset completo a una *muestra representativa* del mismo. Mediante una función tomo la misma cantidad valores aleatorios de cada una de las plataformas y en colab para el entrenamiento y validación del modelo. 
 
  ## **ADJUNTO**
  - Archivo [EDA](https://github.com/AdrienzD/ML_y_DataEngineer/blob/main/EDA.ipynb)
 
  ### MACHINE LEARNING


El fin último de este trabajo era lograr desarrollar un modelo que realice predicciones sobre si a un usuario en particular le va a gustar o no una película por su título.


Para resolverlo propongo un modelo de Machine Learning conocido como **Sistemas de recomendación**.

Para implementarlo lo primero que hago es trabajar con la librería de Python **Surprise**, la cual me permite crear sistemas de recomendación basados en filtrado colaborativo. Lo que básicamente hace es utilizar las calificaciones que han dado antes los usuarios junto con las de otros con gustos similares y elaborar una predicción al respecto.


Entonces, dividendo el dataset en el objeto **Reader** que se utiliza para especificar cómo se deben leer los datos de entrada y cómo se deben tratar las calificaciones; y por otro lado agrupo las variables para reducir la complejidad del modelo y mejorar su precisión y eficiencia.


Instancio el modelo, siguiendo la documentación. Divido a mi conjunto en dos: traine(80%) y test(20%). Con el primero hago el entrenamiento del modelo, así este puede aprender. Con el segundo hago una validación del mismo.


Para corroborar aplico métricas de desempeño tales como son el error cuadrático medio (RMSE) y el error absoluto medio (MAE). También para la optimización de hiperparámetros aplico el método **'Cross Validation'**.


Conforme con los resultados obtenidos, guardo mi modelo en una variable, que luego me servirá para usar en una función.
  
  ## **ADJUNTO MODELO EN LOCAL**
  - Archivo [Machine_Learning](https://github.com/AdrienzD/ML_y_DataEngineer/blob/main/Modelo_ML_sugerenc.ipynb)
  
