from mysqlConnector import MysqlConn
class startDatabase:
    
    def create_client_table():
        connection = MysqlConn.getInstance()

        connection