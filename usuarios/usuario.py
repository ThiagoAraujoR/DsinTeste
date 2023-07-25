import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.executor import sqlExecutor

class usuario_info:
    def __init__(self, user_info:dict) -> None:
        self.nome = str(user_info['nome'])
        self.sobrenome = str(user_info['sobrenome'])
        self.ddd = user_info['ddd']
        self.telefone = str(user_info['telefone'])
        self.user_info = user_info

        self.sqlExecutor = sqlExecutor()