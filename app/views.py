import json
from app import app
from flask import make_response, jsonify


@app.route('/api/v1')
def index():
  return make_response(jsonify({
    'message': 'Rota funcionando'
  }), 200)