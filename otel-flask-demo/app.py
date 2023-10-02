from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from opentelemetry import trace, metrics
from random import randint

# Configuraciones OpenTelemetry
tracer = trace.get_tracer("gestor-de-datos.tracer")
meter = metrics.get_meter("gestor-de-datos.meter")
roll_counter = meter.create_counter(
    "data.requests",
    description="The number of get and post requests",
)

app = Flask(__name__)

# Datos en memoria
DATA = []

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Gestor de Datos API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/data', methods=['GET'])
def get_data():
    with tracer.start_as_current_span("get_data") as span:
        span.set_attribute("data.length", len(DATA))
        roll_counter.add(1, {"method": "GET"})
        return jsonify(DATA)

@app.route('/data', methods=['POST'])
def add_data():
    with tracer.start_as_current_span("add_data") as span:
        item = request.json
        DATA.append(item)
        roll_counter.add(1, {"method": "POST"})
        return jsonify({"message": "Data added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
