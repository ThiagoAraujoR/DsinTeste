import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.executor import sqlExecutor
from loguru import logger

class getDbInfo:
    sqlExecutor= sqlExecutor()
    def get_user_info(self, user_type:str, info:dict) -> tuple:
        sql = f"""
        select * from  {user_type}
        where
            nome= '{info["nome"]}'
        """
        if info['sobrenome']:
            sql =  f'''and sobrenome ='{info["sobrenome"]}';'''
        user_info = self.sqlExecutor.select_first(sql)
        return user_info

    def get_all_users_info(self, user_type:str, info_type:str="*") -> list:
        sql = f"""select {info_type} from  {user_type}"""

        user_info = self.sqlExecutor.select_all(sql)
        return user_info

    def get_info_by_id(self, user_type:str, id:int) -> tuple:
        sql = f"""
        select * from  {user_type}
        where
            id={id};
        """
        user_info = self.sqlExecutor.select_first(sql)
        return user_info

    def get_servico_info(self, nome_servico:str) -> tuple:
        sql = f"""
            select * from servicos
            where
                servico = '{nome_servico}'
            """
        servico_info = self.sqlExecutor.select_first(sql)
        return servico_info

    def get_all_servicos_info(self, table:str, info_type:str="*") -> list:
        sql = f"""
            select {info_type} from  {table}
            """
        servico_info = self.sqlExecutor.select_all(sql)
        return servico_info
