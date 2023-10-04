# Construcción de la Aplicación

## Construye la imagen Docker:
   - Navega al directorio donde se encuentran los archivos de la aplicación
   - Define la variable en entorno DT_URL con la url del tenant hasta el .com Ejemplo: `https://XXXXX.live.com`
      - linux: `export DT_URL=https://XXXXX.live.com`
      - windows: `set DT_URL=https://XXXXX.live.com`
   - Define la variable en entorno DT_TOKEN con el token generado en dynatrace
      - permisos:
         - Ingest logs
         - Ingest metrics
         - Ingest OpenTelemetry traces
      - ejemplo:
         - linux: `export DT_TOKEN=dt.XXXX.XXXX`
         - windows: `set DT_TOKEN=dt.XXXX.XXXX`
   - Construir imagen: `docker build --build-arg DT_URL=${DT_URL} --build-arg DT_TOKEN=${DT_TOKEN} -t demopython:latest .`

## Sube la imagen a un registro
   - Login al repositorio de docker hub: `docker login`
   - Subir imagen al docker hub: `docker push demopython:latest`
   - (Opcional) levantar en local: `docker run --name demopython -p 8080:8080 demopython:latest`
