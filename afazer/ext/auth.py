from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from afazer.ext.db import db
from afazer.models import Usuario


def verify_login(user):
    """Valida o usuario e senha para efetuar o login"""
    login = user.get('username')
    senha = user.get('password')
    if not login or not senha:
        return False
    existing_user = Usuario.query.filter_by(login=login).first()
    if not existing_user:
        return False
    if not (existing_user.tipo_usuario == 'admin'):
        return False
    if check_password_hash(existing_user.senha, senha):
        return True
    return False


def create_user(username, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if Usuario.query.filter_by(username=username).first():
        raise RuntimeError(f'{username} ja esta cadastrado')
    user = Usuario(login=username, senha=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
