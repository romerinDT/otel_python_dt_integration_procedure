# Construcción de la Aplicación

## Construye la imagen Docker:
   - Navega al directorio donde se encuentran los archivos de la aplicación
   - Reemplaza el campo [URL] por la url del tenant hasta el .com Ejemplo: `https://XXXXX.live.com/`
   - Reemplaza el campo [TOKEN] por el token generado en dynatrace con lo siguientes permisos:
      - Ingest logs
      - Ingest metrics
      - Ingest OpenTelemetry traces
   - Construir imagen: `docker build -t demopython:latest .`

## Sube la imagen a un registro
   - Login al repositorio de docker hub: `docker login`
   - Subir imagen al docker hub: `docker push demopython:latest`
   - (Opcional) levantar en local: `docker run --name demopython -p 8080:8080 demopython:latest`
