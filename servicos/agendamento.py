import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.executor import sqlExecutor
from database.getDbInfo import getDbInfo
from loguru import logger
from datetime import datetime

class agendamento:
    def __init__(self) -> None:
        self.sqlExecutor = sqlExecutor()

    def agendar_procedimento(self, funcionaria_info:dict, cliente_info:dict, servico_name:str, data:str, horario:str):
        DbInfo = getDbInfo()

        funcionaria =DbInfo.get_user_info('funcionarios', funcionaria_info)
        cliente = DbInfo.get_user_info('clientes', cliente_info)
        servico = DbInfo.get_servico_info(servico_name)

        sql = f"""
        INSERT INTO agendamentos (`id_cliente`, `id_funcionario`, `cod_servico`, `data`, `horario`)
        VALUES(
            '{cliente[0]}',
            '{funcionaria[0]}',
            {servico[0]},
            '{data}',
            '{horario}'
        )"""
        self.sqlExecutor.executor(sql)

    def reagendar_procedimento(self, funcionaria_info:dict, data:str, horario:str, nova_data:str, novo_horario:str):
        DbInfo = getDbInfo()
        data_hoje = datetime.today().date()

        data_agendada = datetime.strptime(data, '%Y-%m-%d')
        data_proc = datetime.date(data_agendada)

        diferenca_data = data_proc - data_hoje

        if diferenca_data.days < 2:
            return "mudança só pode ser realizado por telefone : 61 90000-0000"

        funcionaria =DbInfo.get_user_info('funcionarios', funcionaria_info)

        sql = f"""
        update agendamentos set `data` = '{nova_data}', `horario` = '{novo_horario}'
        where
            `id_funcionario` ='{funcionaria[0]}' and
            `data` = '{data}' and
            `horario` = '{horario}'
        """
        self.sqlExecutor.executor(sql)

    def cancelar_procedimento(self, funcionaria_info:dict,  data:str, horario:str):
        DbInfo = getDbInfo()
        data_hoje = datetime.today().date()

        data_agendada = datetime.strptime(data, '%Y-%m-%d')
        data_proc = datetime.date(data_agendada)

        diferenca_data = data_proc - data_hoje

        if diferenca_data.days < 2:
            return "Cancelamento só pode ser realizado por telefone : 61 90000-0000"

        funcionaria =DbInfo.get_user_info('funcionarios', funcionaria_info)

        sql = f"""
        delete from agendamentos 
        where
            `id_funcionario` ='{funcionaria[0]}' and
            `data` = '{data}' and
            `horario` = '{horario}'
            """
        self.sqlExecutor.executor(sql)

    def verificar_agendamento(self, data:str='', horario:str=''):
        dados_formatados =[]
        DbInfo = getDbInfo()

        sql ='''select id_cliente, id_funcionario, cod_servico, data, horario from agendamentos'''
        if data:
            sql += f' where data= "{data}"'
        if  data and horario:
            sql += f' and horario= "{horario}"'
        if not data and horario:
            sql += f' where horario= "{horario}"'


        data = self.sqlExecutor.select_all(sql)
        for row in data:
            row =list(row)
            info_dict = {}

            cliente = DbInfo.get_info_by_id('clientes', row[0])
            info_dict['cliente'] = cliente[1]

            funcionaria =DbInfo.get_info_by_id('funcionarios', row[1])
            info_dict['funcionario'] = funcionaria[1]

            servico = DbInfo.get_info_by_id('servicos', row[2])
            info_dict['servico'] = servico[1]

            info_dict['data'] = row[-2]
            info_dict['horario'] = str(row[-1])

            dados_formatados.append(info_dict)
        return {'data':dados_formatados}

    def existe_procedimento_na_mesma_semana(self, semana_anterior:str, proxima_semana:str, nome_cliente:str):
        DbInfo = getDbInfo()

        cliente = DbInfo.get_user_info('clientes', {'nome':nome_cliente, 'sobrenome':''})

        sql =f'''select * from agendamentos
        where data between "{semana_anterior}" and "{proxima_semana}" and id_cliente ={cliente[0]}'''
        data = self.sqlExecutor.select_all(sql)
        if data:
            return True
        return False

if __name__ == '__main__': 
    funcionario = {
        'nome':'thiago',
        'sobrenome':'araujo'
    }
    cliente = {
        'nome':'thiago',
        'sobrenome':'araujo'
    }
    servico = 'selagem'
    a = agendamento()
    a.agendar_procedimento(funcionario,cliente, servico, '2023-07-23', '19:00:00')
