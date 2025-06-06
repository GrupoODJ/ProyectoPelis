# -*- coding: utf-8 -*-
"""api.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LHBpCXKz-sVypNsGtjMpZp0guAr93_e_
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, fields
import joblib
import pandas as pd

# === Inicialización de Flask y CORS ===
app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='API de Predicción de Géneros',
          description='Predicción multilabel de géneros cinematográficos a partir de sinopsis')

# === Cargar el modelo serializado ===
modelo = joblib.load('modelo_m2_tfidf_rf.pkl')
clf = modelo['model']
vectorizer = modelo['vectorizer']
binarizer = modelo['binarizer']

# === Definir el namespace ===
ns = api.namespace('predict', description='Predicción de géneros de películas')

# === Modelo de entrada (ajustado al campo "plot") ===
input_model = api.model('InputModel', {
    'plot': fields.String(required=True, description='Sinopsis de la película')
})

# === Endpoint de predicción ===
@ns.route('/')
class Predict(Resource):
    @ns.expect(input_model)
    def post(self):
        try:
            # Extraer la sinopsis del request
            data = request.get_json()
            plot_text = data.get('plot', '')

            if not plot_text:
                return {'error': 'Debe incluir la clave "plot" con la sinopsis'}, 400

            # Vectorizar
            X_input = vectorizer.transform([plot_text])
            y_proba = clf.predict_proba(X_input)[0]

            # Formato de salida
            resultado = dict(zip(['p_' + g for g in binarizer.classes_], y_proba))
            return jsonify(resultado)

        except Exception as e:
            return {'error': str(e)}, 500

# === Ejecutar la API ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)