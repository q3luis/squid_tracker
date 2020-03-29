# squid_tracker

# Instalacion :

## Descarga el proyecto :

Para descargar el proyecto necesitamos usar git, si usas windows el instalable 
esta aqui [Git_Windos](https://gitforwindows.org)

Una vez instalado Git , solo nos tenemos que bajar el repositorio, para esto 
desde el terminal vamos a la carpeta donde lo queramos descargar y ejecutamos:
* git clone git@github.com:q3luis/squid_tracker.git

## Environment

Configuramos el entorno usando [Anaconda](https://www.anaconda.com/distribution/) 

### Instalamos dependencias:

Una vez instalado anaconda solo tenemos que ejecutar el siguiente comando desde 
el terminal para para instalar las dependencias :

* conda create -n squid_tracker python=3.6 opencv=3.4

### Activamos el entorno :

* conda activate squid_tracker 

Una vez que tenemos el entorno ya podemos ejecutar ,

# Ejecución

Para ejecutar el proyecto nos pónemos en el directorio principal del proyecto y ejecutamos:
* python tracker/main.py -path "path_del video"






