from flask import Blueprint

from .views import login, listar_atividades, visualizar_menu_gestor, gerenciar_atividades, visualizar_menu_usuario, sair


bp = Blueprint("webui", __name__, template_folder="templates")

login.methods = ['GET', 'POST']
bp.add_url_rule("/", view_func=login, endpoint="login")
bp.add_url_rule(
    "/gestor", view_func=visualizar_menu_gestor, endpoint="gestorview"
)
bp.add_url_rule(
    "/gestor/atividades", view_func=listar_atividades, endpoint="atividadeview"
)
bp.add_url_rule(
    "/gestor/gerenciar_atividades", view_func=gerenciar_atividades, endpoint="gerenciaratividadesview"
)


bp.add_url_rule(
    "/usuario/", view_func=visualizar_menu_usuario, endpoint="menu_usuarioview"
)
bp.add_url_rule(
    "/usuario/sair/", view_func=sair, endpoint="sair"
)

# api.add_resource(Index, '/')
# api.add_resource(Pessoa, '/pessoa/<string:nome>/')
# api.add_resource(ListaPessoas, '/pessoa/')
# api.add_resource(ListaAtividades, '/atividades/')
# api.add_resource(Atividade, '/atividade/<int:id>/')


def iniciar_app(app):
    app.register_blueprint(bp)
