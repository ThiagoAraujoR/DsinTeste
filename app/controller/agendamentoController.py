from database.getDbInfo import getDbInfo
from servicos.agendamento import agendamento
from loguru import logger
from datetime import datetime, timedelta
class agendamentoController:

    def agendar(self, func_name:str, cliente_name:str, servico:str, date:str):
        agendador = agendamento()
        funcionario, cliente, data, horario = self.sanitize_data(func_name, cliente_name, str(date))

        if agendador.existe_procedimento_na_mesma_semana(
            semana_anterior=(date-timedelta(days=7)).date(),
            proxima_semana=(date+timedelta(days=7)).date(),
            nome_cliente=cliente_name):
            logger.critical(1)
            return "Não deseja marcar para o mesmo dia?"
        agendador.agendar_procedimento(funcionario, cliente, servico, data, horario)

    def sanitize_data(self, func_name:str, cliente_name:str, date:str):
        dict_func = {"nome":func_name, 'sobrenome':''}
        dict_cliente = {"nome":cliente_name,  'sobrenome':''}
        date = date.split(' ')
        data = date[0]
        horario = date[1]
        return dict_func, dict_cliente, data, horario
