from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.trace import get_tracer_provider, set_tracer_provider

set_tracer_provider(TracerProvider())
get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)

instrumentor = FlaskInstrumentor()

app = Flask(__name__)

instrumentor.instrument_app(app)

# Datos en memoria
DATA = []

# Swagger UI Configuration
SWAGGER_URL = '/api-docs'
API_URL = '/swagger.json'  # Nota el cambio aquí: añadimos un slash al principio

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
    return jsonify(DATA)

@app.route('/data', methods=['POST'])
def add_data():
    item = request.json
    DATA.append(item)
    return jsonify({"message": "Data added successfully!"}), 201

@app.route('/swagger.json')  # Ruta para servir el archivo swagger.json
def swagger_json():
    with open('swagger.json', 'r') as f:
        json_content = f.read()
    return json_content, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, use_reloader=False)
