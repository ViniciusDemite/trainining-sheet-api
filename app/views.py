import json
from app import app
from flask import make_response, jsonify
from dotenv import dotenv_values


env = dotenv_values('.env')

@app.route(f'{env["BASE_URL"]}')
def index():
  return make_response(jsonify({
    'message': 'Rota funcionando'
  }), 200)