from flask import Flask
from routes.home import home_route
from routes.client import client_route
#inicializaçao
app= Flask(__name__)

#rotas
app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix='/clientes')

#execuçao
app.run(debug=True)



