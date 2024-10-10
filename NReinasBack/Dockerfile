#Especifica la imagen base a utilizar
FROM python:3.9 

# Establece el directorio de trabajo
WORKDIR /code

# Copia los archivos de requisitos 
COPY ./requirements.txt /code/requirements.txt

# Instala las dependencias
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia  el código de la aplicación
COPY . /code/aplication

# Comando para iniciar la aplicación
CMD ["fastapi", "run", "aplication/app/api/app.py", "--port", "8000"]