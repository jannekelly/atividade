from afazer.ext import admin
from afazer.ext import db
from afazer.ext import auth
from afazer.ext import aparencia
from flask import Flask
from afazer.blueprints import webui
from flask_login import LoginManager
from afazer.models import Usuario

app = Flask(__name__)
app.config['TITLE'] = "Afazer"
db.iniciar_app(app)
aparencia.iniciar_app(app)
admin.iniciar_app(app)
auth.init_app(app)
webui.iniciar_app(app)

login_manager = LoginManager()
login_manager.login_view = 'webui.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return Usuario.query.get(int(user_id))



# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return Usuarios.query.filter_by(login=login, senha=senha).first()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
#ssl_context='adhoc',