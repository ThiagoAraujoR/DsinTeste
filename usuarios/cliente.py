from usuarios.usuario import usuario_info

class cliente(usuario_info):

    def add_cliente(self):
        sql = f""" insert into clientes ( `nome`, `sobrenome`, `ddd`, `telefone`) values(
            '{self.nome}',
            '{self.sobrenome}',
            {self.ddd},
            '{self.telefone}'
        )"""

        self.sqlExecutor.executor(sql)

if __name__ == '__main__': 
    json =  {
      "nome": "thiago",
      "sobrenome": "araujo",
      "ddd": 61,
      "telefone": "993199244",
    }

    c = cliente(json)
    c.add_cliente()