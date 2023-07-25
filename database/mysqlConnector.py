import mysql.connector
from loguru import logger
from time import sleep

class MysqlConn:
    _instance = None

    def __init__(self):
        if MysqlConn._instance is not None:
            raise Exception("This class is a singleton! call getInstance")
        else:
            MysqlConn._instance = self

    @staticmethod
    def getInstance():
        if MysqlConn._instance is None:
            MysqlConn()

        return MysqlConn._instance

    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                port=25060,
                user="root",
                password="dsin_password",
                database="export")

            return connection
        except mysql.connector.Error as err:
            logger.error('ERRO: ')
            logger.error(err)
