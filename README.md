# Proyecto de Álgebra Lineal Computacional

Este proyecto implementa y analiza el modelo de insumo-producto de Leontief utilizando álgebra lineal computacional. El trabajo incluye la resolución de sistemas de ecuaciones lineales con descomposición LU y simulación de shocks económicos en diferentes sectores.

## Estructura del Proyecto

El proyecto está organizado en cuatro directorios principales:
1. /data/

Este directorio contiene los datos de entrada necesarios para realizar los cálculos. 

    Contenido:
        MIP_Latinoamericana_2011.xlsx: Archivo descargado de CEPAL con flujos entre sectores de la economía de varios países.
        Otros archivos de entrada que se requieran.

2. /notebooks/

Contiene los Jupyter Notebooks que implementan y explican los pasos de la resolución del trabajo práctico. Aquí se encuentran tanto el análisis teórico como los cálculos y gráficos generados.

    Contenido:
        TP1_Resuelto.ipynb: Notebook principal que incluye la resolución completa del trabajo práctico.
        Otros notebooks adicionales para experimentos o análisis complementarios.

3. /results/

Este directorio almacena los resultados generados por el código, tales como matrices invertidas, gráficos y conclusiones sobre el análisis realizado.

    Contenido:
        Subdirectorios como graficos/ o matrices/ pueden organizar los resultados según sea necesario.
        Archivos de texto, imágenes o matrices generadas durante el proyecto.

4. /src/

Aquí se encuentra todo el código fuente utilizado en el proyecto. Este directorio contiene las funciones implementadas para resolver el modelo, realizar cálculos matriciales y otros procedimientos necesarios.

    Contenido:
        funciones.py: Contiene las funciones principales, como la descomposición LU e inversión de matrices.
        main.py: Script principal que ejecuta el análisis general del proyecto.

Requisitos

Para ejecutar este proyecto, necesitas las siguientes librerías de Python:

    numpy
    pandas
    scipy
    matplotlib (opcional, para gráficos)

Ejecución del Proyecto

    Coloca los archivos de datos en el directorio /data/.
    Ejecuta los notebooks de /notebooks/ para realizar el análisis del trabajo práctico.
    Los resultados se generarán y almacenarán automáticamente en el directorio /results/.
    Para trabajar con el código fuente, puedes modificar y ejecutar los scripts en /src/.
