from flask import Flask

from views.views import view_modular_bp

app = Flask(__name__)
app.register_blueprint(view_modular_bp)


if __name__ == "__main__":
    app.run(debug=True)


