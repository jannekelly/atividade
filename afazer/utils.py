from models import Pessoas, Atividades, Usuarios

# USUARIOS = {
#     'gabriel': '1',
#     'amanda': '2'
# }
# @auth.verify_password
# def verificacao(login, senha):
#     print('validando usuario')
#     print(USUARIOS.get(login) == senha)
#     if not (login, senha):
#         return False
#     return USUARIOS.get(login) == senha



def inserir_pessoas():
    pessoa = Pessoas(nome='Amanda', idade=20)
    print(pessoa)
    pessoa.save()

def consultar_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Biel').first()
    print(pessoa.idade)
def alterar_pessoa():
    pessoa= Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.idade = 22
    pessoa.save()

def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.delete()


def inserir_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha, tipo_usuatio = '')
    usuario.save()

def consultar_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def deletar_usuarios():
    usuarios = Usuarios.query.all()
    for i in usuarios:
        i.delete()

def teste():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    print(pessoa)
    atividade = Atividades(nome='teste', pessoa=pessoa, status='fazendo')
    atividade.save()


def geteste():
    atividade = Atividades.query.all()
    print(atividade)


if __name__ == '__main__':

    # teste()
    # geteste()
    #deletar_usuarios()
    # inserir_usuarios('gabriel', '123')
    # inserir_usuarios('amanda', '432')
    # consultar_todos_usuarios()
    inserir_pessoas()
    #alterar_pessoa()
    #excluir_pessoa()
    #consultar_pessoas()