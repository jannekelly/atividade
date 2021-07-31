from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required
from werkzeug.security import generate_password_hash

from afazer.ext.db import db
from afazer.models import Pessoa, Usuario, Atividade

# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin()


class UserAdmin(sqla.ModelView):
    column_list = ['login', 'pessoa.nome', 'tipo_usuario']
    can_edit = True

    def on_model_change(self, form, model, is_created):
        model.senha = generate_password_hash(model.senha)


def iniciar_app(app):
    admin.name = "admin"
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.add_view(sqla.ModelView(Atividade, db))
    admin.add_view(sqla.ModelView(Pessoa, db))
    admin.add_view(UserAdmin(Usuario, db))
