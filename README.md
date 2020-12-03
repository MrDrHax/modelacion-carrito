# Instrucciones de uso de codigo

Dentro de esta carpeta, podras encontrar distintos archivos, de los cuales, muchos son solo de procesos secundarios.

Para correr el app, es necesario tener preinstalados:

* pyglet
* numpy
* python 3.8+

Y para mayoes opciones, es recomendado tambien tener instalado `streamlit`.

el instalador proporcionado automaticamente corre todas las dependecncias necesarias para poder correr el app. De la misma forma, se asegura de que el usuario tenga la version correcta de python instalada. 

Para correr el instalador abra una terminal y navegue a la carpeta donde descomprimio todo, de ahi, corra `python3 setup.py`, una vez corrido, le preguntara si desea instalar las dependencias necesarias. 

Para correr el app principal, puede usar `python3 app.py` en consola, y la simulacion iniciara.

La simulacion incluye los siguientes controles:

1. W *se usa para accelerar el carro*

2. S *se usa para desaccelerar el carro*

3. Barra espaciadora *se usa para forzar un choque*

4. R *se usa para reiniciar*

Si se desea crear una nueva pista, se puede hacer corriendo `streamlit run graficador.py`

Dentro de ahi, podras hacer una nueva pista, al precionar guardar a JSON, y correr app.py nuevamente, el app tomara los puntos especiales nuevos y creara la nueva pista.