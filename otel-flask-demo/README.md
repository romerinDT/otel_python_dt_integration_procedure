# Construcción de la Aplicación

## Construye la imagen Docker:
   - Navega al directorio donde se encuentran los archivos de la aplicación
   - Construir imagen: `docker build -t demopython:latest .`

## Sube la imagen a un registro
   - Login al repositorio de docker hub: `docker login`
   - Subir imagen al docker hub: `docker push demopython:latest`
