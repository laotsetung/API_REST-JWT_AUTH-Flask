from flask import Flask
from blueprints.auth.auth_bp import auth_routes
from blueprints.home.home_bp import home_routes
#Classe com configurações do projeto
from classes.configSC import configSC

app = Flask(__name__)
app.config['SECRECT_KEY'] = configSC.secret

#BluePrints do projeto
app.register_blueprint(auth_routes)
app.register_blueprint(home_routes)

if __name__ == '__main__':
    app.run(debug=True)