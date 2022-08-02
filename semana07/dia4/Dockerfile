#esta es mi primera imagen con docker

#imagen base
FROM ubuntu

#ejecutar comandos en mi contenedor ubuntu
RUN apt-get update
RUN apt-get install python3 python3-dev -y
RUN mkdir /app

#defino mi directorio de trabajo
WORKDIR /app

#copio los archivos de mi local a mi contenedor
ADD index.html .

#ejecuta un comando de python3
CMD python3 -m http.server 5000

#expone el puerto 5000
EXPOSE 5000