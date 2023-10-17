from flask import Flask
from blueprints.auth.auth_bp import auth_routes
from blueprints.home.home_bp import home_routes
import os
from dotenv import load_dotenv, dotenv_values

app = Flask(__name__)
app.config['SECRECT_KEY'] = os.getenv("CHAVE")

#BluePrints do projeto
app.register_blueprint(auth_routes)
app.register_blueprint(home_routes)

if __name__ == '__main__':
    app.run(debug=True)