FROM python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN opentelemetry-bootstrap --action=requirements
RUN opentelemetry-bootstrap --action=install

COPY . .

ARG DT_URL
ARG DT_TOKEN

ENV OTEL_SERVICE_NAME="demopyotel"
ENV OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=${DT_URL}/api/v2/otlp/v1/traces
ENV OTEL_EXPORTER_OTLP_HEADERS=Authorization=Api-Token%20${DT_TOKEN}
ENV OTEL_METRICS_EXPORTER=none
ENV OTEL_LOG_LEVEL=DEBUG

CMD ["opentelemetry-instrument", "python", "app.py"]
#CMD ["opentelemetry-instrument", "--traces_exporter", "console","--metrics_exporter", "console", "python", "app.py"]
