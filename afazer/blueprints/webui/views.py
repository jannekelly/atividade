from flask import request, render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash
from afazer.models import Pessoa, Atividade, Usuario
from flask_login import login_user, login_required, logout_user, current_user


def login():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form.get('senha')
        remember = True if request.form.get('remember') else False
        usuario = Usuario.query.filter_by(login=email).first()
        if usuario is not None and check_password_hash(usuario.senha, senha):
            login_user(usuario, remember=remember)
            if current_user.tipo_usuario=="gestor":
                return redirect(url_for('webui.gestorview'))
            return redirect(url_for('webui.menu_usuarioview'))
        flash("Email ou senha incorretos, tente novemente.")
        return render_template('loginUser.html')

    return render_template('loginUser.html')


@login_required
def sair():
    logout_user()
    return redirect(url_for('webui.login'))


@login_required
def visualizar_menu_gestor():
    if request.method=='POST':
        pass
    atividades = Atividade.query.all()
    print(atividades)
    return render_template('atividades.html', atividades=atividades)


@login_required
def editar_atividade(id):
    if current_user.tipo_usuario =="gestor":
        return render_template('editar_atividade.html',id=id)

    atividades = Atividade.query.filter_by(pessoa_id=current_user.pessoa_id)

    return render_template('menu_usuario.html', atividades=atividades,id=id)
@login_required
def excluir_atividade(id):
    atividade=Atividade.query.filter_by(id=id).first()
    atividade.delete()
    return redirect(url_for('webui.gestorview'))
@login_required
def criar_atividade():
    if request.method=='POST':
        nome = request.form['nome']
        responsavel = request.form.get('responsavel')
        pessoa=Pessoa.query.filter_by(nome=responsavel).first()
        atividade=Atividade(nome=nome,pessoa=pessoa,status="Por Fazer")
        atividade.save()
        return redirect(url_for('webui.gestorview'))
    pessoas=Usuario.query.filter_by(tipo_usuario="usuario").all()
    return render_template('criar_atividade.html',pessoas=pessoas)
def buscar_atividade():
    pass

@login_required
def gerenciar_atividades():
    return render_template('gerenciar_atividades.html')


@login_required
def visualizar_menu_usuario():

    atividades = Atividade.query.filter_by(pessoa_id=current_user.pessoa_id)
    #print(type(current_user.pessoa_id))
    id = request.args.get('id')
    #status=request.form.get('status',type=str)
    print("teste aqui",id)
    if request.method=="POST":
        #status = request.form.get('status',type=str)
        print("POST")
        id=request.form.get('id',type=int)
        status = request.form.get('status', type=str)
        print(id,status)
        atividade = Atividade.query.filter_by(id=id).first()
        atividade.status=status
       # print(atividade.status)
        atividade.save()
        return render_template('atividades.html', atividades=atividades)
    elif request.method=="GET":
        print("geet")
        id=request.args.get('id')
        print(id)
        pass
    print("methods fail")
    return render_template('atividades.html', atividades=atividades)


def post():
    dados = request.json
    try:
        pessoa = Pessoa.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividade(nome=dados['nome'], pessoa=pessoa)
        nomePessoa = atividade.pessoa.nome
        atividade.save()
        response = {
            'pessoa': nomePessoa,
            'nome': atividade.nome,
            'id': atividade.id
        }

    except AttributeError:
        response = {
            'status': 'error',
            'mensagem': 'Pessoa nao encontrada'
        }

    return response


# class Atividade():
    # def put(self, id):
    #     dados = request.json
    #     if not("Pendente" == dados['status'] or "Finalizado"):
    #         response = {
    #             'status': 'error',
    #             'mensagem': 'Dado recebido nao correponde ao esperado'
    #         }
    #         return response
    #
    #     atividade = Atividades.query.filter_by(id=id).first()
    #     atividade.status = dados['status']
    #     atividade.save()
    #     response = {
    #         'status': atividade.status
    #     }
    #     return response

    # def delete(self, id):
        # atividade = Atividades.query.filter_by(id=id).first()
        # #mensagem = 'Atividade {} excluida com sucesso'.format(atividade.nome)
        # mensagem = 'Atividade {} excluida com sucesso'
        # atividade.delete()
        # return {'status': 'sucesso', 'mensagem': mensagem}

