import math

from flask import Flask, jsonify, Blueprint

view_modular_bp = Blueprint('view_modular', __name__)


@view_modular_bp.route("/modular/<x>")
def calcular_modular(x):
    valor_de_x = 0
    if x.startswith('m'):
        x = x.replace('m', '')
        valor_de_x = int(x) * -1
    else:
        valor_de_x = int(x)

    if math.pow(valor_de_x, 3) >= 0:
        return jsonify(valor_de_x)
    else:
        return jsonify(valor_de_x * -1)
