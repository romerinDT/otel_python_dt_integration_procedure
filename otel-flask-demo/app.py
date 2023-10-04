from flask import Flask, request, jsonify

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

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
    app.run(debug=True, host='0.0.0.0', port=8080)
