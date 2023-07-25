from mysqlConnector import MysqlConn
from loguru import logger

class createTables:
    def __init__(self):
        self.myMysql = MysqlConn.getInstance()

    def create_tables(self):
        self.conn = self.myMysql.get_connection()

        self.create_table_clientes()
        self.create_table_funcionarios()
        self.create_table_servicos()
        self.create_table_agendamentos()

        self.conn.close()
    def create_table_clientes(self):
        table_name = 'clientes'
        sql_props= f"""
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(30) NOT NULL,
            sobrenome VARCHAR(30) NOT NULL,
            ddd INT(2) NOT NULL,
            telefone VARCHAR (9) NOT NULL
            """
        self.creator(table_name, sql_props)

    def create_table_funcionarios(self):
        table_name = 'funcionarios'
        sql_props= f"""
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(30) NOT NULL,
            sobrenome VARCHAR(30) NOT NULL,
            ddd INT(2) NOT NULL,
            telefone VARCHAR (9) NOT NULL,
            endereco VARCHAR (70) NOT NULL,
            cargo ENUM("gerente", "cabelereira") NOT NULL
        """
        self.creator(table_name, sql_props)


    def create_table_servicos(self):
        table_name = 'servicos'
        sql_props= f"""
            id INT AUTO_INCREMENT PRIMARY KEY,
            servico VARCHAR(40) NOT NULL,
            valor DOUBLE NOT NULL
        """
        self.creator(table_name, sql_props)

    def create_table_agendamentos(self):
        table_name = 'agendamentos'
        sql_props= f"""
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_cliente INT NOT NULL,
            id_funcionario INT NOT NULL,
            cod_servico INT,
            data DATE,
            horario TIME,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id),
            FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id),
            FOREIGN KEY (cod_servico) REFERENCES servicos(id)
        """
        self.creator(table_name, sql_props)

    def creator(self, table_name:str, table_props:str):
        cursor = self.conn.cursor()
        if not self.verify_table_exists(table_name):

            sql= f"""CREATE TABLE {table_name}({table_props})"""
            logger.debug(sql)
            cursor.execute(sql)

            return logger.info(f"Tabela {table_name} criada com sucesso")
        return logger.info(f"Tabela {table_name} já existe")

    def verify_table_exists(self, table_name: str) -> bool:
        cursor = self.conn.cursor()

        sql = f"SHOW TABLES LIKE '{table_name}'"
        cursor.execute(sql)

        return cursor.fetchone()

if __name__ == '__main__': 
    createTables = createTables()
    createTables.create_tables()