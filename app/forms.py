from flask_wtf import FlaskForm
from wtforms import DateTimeField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from database.getDbInfo import getDbInfo
from loguru import logger
class agendamentoForm(FlaskForm):
    DbInfo = getDbInfo()
    nome_funcionario= SelectField("nome_funcionario", choices=DbInfo.get_all_users_info("funcionarios", "nome, nome"))
    nome_cliente= SelectField("nome_cliente", choices=DbInfo.get_all_users_info("clientes", "nome, nome"))
    servico= SelectField("servico", choices=DbInfo.get_all_users_info("servicos", "servico, servico"))
    horario= DateTimeField("data_horario", validators=[DataRequired()])
    novo_horario= DateTimeField("novo_data_horario")
    submit = SubmitField("Agendar")

class clienteForm(FlaskForm):
    nome_cliente= StringField("nome_cliente")
    sobrenome_cliente= StringField("sobrenome_cliente")
    ddd = StringField("ddd")
    numero = StringField("numero")
    submit = SubmitField("Adicionar")


class funcionarioForm(FlaskForm):
    DbInfo = getDbInfo()

    nome_funcionario= StringField("nome_funcionario")
    sobrenome_funcionario= StringField("sobrenome_funcionario")
    ddd = StringField("ddd")
    numero = StringField("numero")
    endereco = StringField("endereco")
    cargo = SelectField("servico", choices=['cabelereira', 'gerente'])

    submit = SubmitField("Adicionar")

class servicoForm(FlaskForm):
    DbInfo = getDbInfo()

    nome_servico= StringField("nome_servico")
    valor= StringField("valor")

    submit = SubmitField("Adicionar")