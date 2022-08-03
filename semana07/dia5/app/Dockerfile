#imagen original
FROM python:3.9.6-alpine

#directorio de trabajo
WORKDIR /usr/src/app

#actualizamos la version de pip
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copiamos todos los archivos de mi carpeta actual a mi imagen
COPY . .


#desplegamos el servidor de django
CMD python manage.py runserver 0.0.0.0:8000

#exponemos el puerto 8000
EXPOSE 8000

