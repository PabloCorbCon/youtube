![Flask Logo](https://github.com/PabloCorbCon/youtube/blob/master/flask-api/images/flask-logo.png "Flask Logo")
## Rest api con Flask
En [este video](URL DEL VIDEO) publicado en [mi canal de YouTube](URL DEL CANAL) os explico con un ejemplo práctico como podeís desarrollar un REST API utilizando Python, concretamente el microframework de [Flask](https://palletsprojects.com/p/flask/).

El **código del video** se encuentra en [la carpeta src](https://github.com/PabloCorbCon/youtube/blob/master/flask-api/src)

Para ilustrar la teoría del video, creamos un **REST API para** simular que somos dueños de **una academia de idiomas**, en la que tenemos información sobre diferentes alumnos, como su nombre, el idioma que estudian, el precio que pagan por estudiar en nuestra academia...

A diferencia de la mayor parte de APIS reales, en este video **no utilizamos conexiones con el servidor** es decir, en ningun momento connectamos con una base de datos SQL o NO-SQL para trabajar con los datos de los alumnos. En su lugar trabajamos con una lista de diccionarios que simula el papel de base de datos, cada uno de estos diccionarios contiene cada uno de los atributos de los alumnos. Por lo que si tenemos 3 estudiantes, el código podría ser el siguiente:
```python
estudiantes = [
	{'nombre':'pepe', 'edad':20, 'idioma':'frances'},
	{'nombre':'ana', 'edad':34, 'idioma':'chino'},
	{'nombre':'juan', 'edad':17, 'idioma':'ingles'}
]
```
##### Requisitos para seguir este video
Para seguir este tutorial de forma exitosa, es necesario conocer unos requisitos mínimos en algunas areas. Estas son:

* Concocimientos básicos en Python (archivos  `.py`, variables, funciones, decoradores básicos, estructuras de datos básicas...)
* Python (3) instalado (No vamos a instalarlo en este video)
* Un Editor de texto o un IDE (a menos que quieras utilizar el blog de notas)
* PIP (el gestor de paquetes de Python) instalado, ya que con el vamos a instalar paquetes como Flask.

Si necesitas consultar la transcripción del video, puedes hacerlo en el archivo [guide.md](https://github.com/PabloCorbCon/youtube/blob/master/flask-api/guide.md) del repositorio (El archivo está en Español).