import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.executor import sqlExecutor
class servico:
    def __init__(self, servico_info:dict):
        self.servico= servico_info['servico']
        self.valor= float(servico_info['valor'])
        self.sqlExecutor = sqlExecutor()

    def add_servico(self):
        sql = f"""
        INSERT INTO servicos (`servico`, `valor`)
        VALUES(
            '{self.servico}',
            {self.valor}
        )"""
        self.sqlExecutor.executor(sql)

    def delete_servico(self):
        sql = f"""
        DELETE FROM 
            servicos 
        WHERE
            servico= '{self.servico}',
            valor = {self.valor}"""
        self.sqlExecutor.executor(sql)

if __name__ == '__main__': 
    json = {
        "servico" : "selagem",
        "valor": 40.5
    }
    s = servico(json)

    s.add_servico()