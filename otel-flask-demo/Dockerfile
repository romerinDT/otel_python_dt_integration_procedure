FROM python:3.6

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN opentelemetry-bootstrap --action=install

COPY . .

ENV OTEL_EXPORTER_OTLP_ENDPOINT="URL"
ENV OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token TOKEN"
ENV OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"
ENV OTEL_SERVICE_NAME="demopyotel"

CMD ["opentelemetry-instrument", "python", "app.py"]
