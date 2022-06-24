# Prueba tecnica Web Scrapper
Este proyecto es un API que recolecta informacion puntual solicitada en la prueba:

- URL
- Meta title y description de la página 
- URL de la foto
- Texto de la página

Tambien se solicito que esta informacion fuera entregada en formato JSON y que el script sea capaz de hacer crawling de los links dentro de la pagina.

Se decidio realizar el proyecto como un API por la versatilidad y la posible reutilizacion del mismo.

*El proyecto no esta pensado para un ambiente de produccion, es unicamente para pruebas*


# Requisitos para correr el proyecto

- Python 3.7+
- Instalar todas librerias de python listadas en el archivo requirements.txt

## Como ejecutar el proyecto

Se debe ejecutar el siguiente comando en consola para que el servidor web de desarrollo:
```bash
python manage.py runserver
```
## Como usar el web scrapper
Una vez ejecutado el proyecto el unico endpoint que esta disponible es el siguiente

>http://127.0.0.1:8000/api/scrapper/


El endpoint acepta un unico parametro "url" que se usara para devolver el resultado esperado para fines demostrativos se dara un ejemplo con la pagina https://es.gizmodo.com/

Utilizando el metodo GET de HTTP
> http://127.0.0.1:8000/api/scrapper/?url=https://es.gizmodo.com/

El resultado obtenido a esa consulta seria 

![scrapper-example.png](https://i.postimg.cc/kMkPcSgN/scrapper-example.png)


