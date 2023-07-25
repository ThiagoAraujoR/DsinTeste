import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from loguru import logger
from flask import Flask, render_template, request, redirect, url_for
from servicos.agendamento import agendamento
from servicos.servico import servico
from forms import agendamentoForm, clienteForm, funcionarioForm, servicoForm
from controller.agendamentoController import agendamentoController
from database.getDbInfo import getDbInfo
from usuarios.cliente import cliente
from usuarios.funcionario import funcionario
app = Flask(__name__)
app.config.from_object('config')
app.debug= True

@app.route('/')
@app.route('/agenda')
@app.route('/agendamentos(/<message>)')
def agendamentos(message:str=''):
    agendador = agendamento()
    lista_agentamentos = agendador.verificar_agendamento()

    return render_template('agendamentos.html', content=lista_agentamentos, message = message)

@app.route('/agendar', methods=["GET", "POST"])
def marcar_agendamento():
    form = agendamentoForm()
    agendador = agendamentoController()
    if request.method != "POST":
        return render_template('marcar_agendamento.html', content='', form=form)

    if form.validate_on_submit():
        message = agendador.agendar(form.nome_funcionario.data, form.nome_cliente.data, form.servico.data, form.horario.data)
        return redirect(url_for('agendamentos',message = message))

    return redirect(url_for('agendamentos'))
@app.route('/delete_agendamento/<funcionario_name>/<data>/<horario>', methods=["GET", "POST"])
def desmarcar_agendamento(funcionario_name:str, data:str, horario:str):
    agendador = agendamento()

    message = agendador.cancelar_procedimento(
        funcionaria_info={
            "nome":funcionario_name,
            "sobrenome":''
            },
        data=data,
        horario=horario
    )
    return redirect(url_for('agendamentos', message=message))
@app.route('/reagendar/<funcionario_name>/<data>/<horario>', methods=["GET", "POST"])
def reagendar(funcionario_name:str, data:str, horario:str):
    form = agendamentoForm()

    if request.method != "POST":
        return render_template('reagendar.html', content='', form=form, dados ={
            'funcionario_name':funcionario_name,
            'data':data,
            'horario':horario
            })

    agendador = agendamento()

    message = agendador.reagendar_procedimento(
        funcionaria_info={
            "nome":funcionario_name,
            "sobrenome":''
            },
        data=data,
        horario=horario,
        nova_data= str(form.novo_horario.data).split(' ')[0],
        novo_horario= str(form.novo_horario.data).split(' ')[1]
    )
    return redirect(url_for('agendamentos', message=message))

@app.route('/funcionarios', methods=['GET'])
def funcionarios():
    DbInfo = getDbInfo()
    lista_funcionarios = DbInfo.get_all_users_info('funcionarios')

    return render_template('funcionarios.html', content=lista_funcionarios)

@app.route('/adicionar_funcionario', methods=['GET',"POST"])
def add_funcionarios():
    form = funcionarioForm()

    if request.method != "POST":
        return render_template('adicionar_funcionario.html', content='', form=form)

    if form.validate_on_submit():
        funcionarios_add = funcionario({
            'nome':form.nome_funcionario.data,
            'sobrenome': form.sobrenome_funcionario.data,
            'ddd': form.ddd.data,
            'telefone': form.numero.data,
            'endereco': form.endereco.data,
            'cargo': form.cargo.data,
        })
        funcionarios_add.add_funcionario()
        return redirect(url_for('funcionarios'))

@app.route('/clientes', methods=['GET'])
def clientes():
    DbInfo = getDbInfo()
    lista_clientes = DbInfo.get_all_users_info('clientes')

    return render_template('clientes.html', content=lista_clientes)

@app.route('/adicionar_cliente', methods=['GET',"POST"])
def add_clientes():
    form = clienteForm()

    if request.method != "POST":
        return render_template('adicionar_cliente.html', content='', form=form)
    if form.validate_on_submit():
        cliente_add = cliente({
            'nome':form.nome_cliente.data,
            'sobrenome': form.sobrenome_cliente.data,
            'ddd': form.ddd.data,
            'telefone': form.numero.data
        })

        cliente_add.add_cliente()
        return redirect(url_for('clientes'))

@app.route('/servico', methods=['GET'])
def servicos():
    DbInfo = getDbInfo()
    lista_servicos = DbInfo.get_all_servicos_info('servicos')

    return render_template('servicos.html', content=lista_servicos)

@app.route('/adicionar_servico', methods=['GET',"POST"])
def add_servicos():
    form = servicoForm()

    if request.method != "POST":
        return render_template('adicionar_servico.html', content='', form=form)

    if form.validate_on_submit():

        servico_add = servico({
            'servico':form.nome_servico.data,
            'valor': form.valor.data,
        })
        logger.debug(servico_add)
        servico_add.add_servico()
        return redirect(url_for('servicos'))

if __name__ == '__main__': 
    app.run()