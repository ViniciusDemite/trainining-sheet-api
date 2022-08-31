from app import app, env
from flask import make_response, jsonify


@app.route(f'{env["BASE_URL"]}')
def index():
  return make_response(jsonify({
    'message': 'Rota funcionando'
  }), 200)