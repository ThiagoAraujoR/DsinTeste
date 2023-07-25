
from database.mysqlConnector import MysqlConn
from loguru import logger

class sqlExecutor:
    def executor(self, sql:str):
        try:
            conn, cursor = self.get_sql_instance()
            cursor.execute(sql)
            conn.commit()

            cursor.close()
            conn.close()
            logger.debug(f"Query: {sql} foi executada com sucesso")
        except Exception as e:
            logger.error('ERRO: ')
            logger.error(e)

    def select_first(self, sql:str):
        try:
            conn, cursor = self.get_sql_instance()
            cursor.execute(sql)
            first = cursor.fetchone()
            conn.close()
            cursor.close()
            return first
        except Exception as e:
            logger.error('ERRO: ')
            logger.error(e)

    def select_all(self, sql:str):
        try:
            conn, cursor = self.get_sql_instance()
            cursor.execute(sql)
            all_sql_info = cursor.fetchall()
            conn.close()
            cursor.close()
            return all_sql_info
        except Exception as e:
            logger.error('ERRO: ')
            logger.error(e)

    def get_sql_instance(self):
        myMysql = MysqlConn.getInstance()
        conn = myMysql.get_connection()
        cursor = conn.cursor()

        return conn, cursor