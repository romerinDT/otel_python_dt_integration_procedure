FROM python:3.6

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN opentelemetry-bootstrap --action=install

COPY . .

ENV OTEL_EXPORTER_OTLP_ENDPOINT=https://gnj89010.dev.dynatracelabs.com
ENV OTEL_EXPORTER_OTLP_HEADERS=Authorization=Api-Token%20dt0c01.CNHH7KNU6LFALM6XC6X7Z32K.CTK4TZHQEF7WAMC53CRGDNNWDO4VB6LXHSFD6TYZUYJARLCYAQNMCVTTGPIXLTQL
ENV OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
ENV OTEL_SERVICE_NAME="demopyotel"

CMD ["opentelemetry-instrument", "python", "app.py"]
