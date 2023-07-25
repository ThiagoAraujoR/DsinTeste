from usuarios.usuario import usuario_info

class funcionario(usuario_info):
    def add_funcionario(self):
        sql = f"""
        INSERT INTO funcionarios (`nome`, `sobrenome`, `ddd`, `telefone`, `endereco`, `cargo`) 
        VALUES(
            '{self.nome}',
            '{self.sobrenome}',
            {self.ddd},
            '{self.telefone}',
            "{self.user_info['endereco']}",
            "{self.user_info['cargo']}"
        )"""
        self.sqlExecutor.executor(sql)

    def remove_funcionario(self):
        sql = f"""
        delete from  funcionarios 
        where
           nome= '{self.nome}' and
           sobrenome ='{self.sobrenome}';
        """
        self.sqlExecutor.executor(sql)

    def select_all_funcionario(self):
        sql = """select nome, sobrenome from funcionarios"""
        return self.sqlExecutor.select_all(sql)


if __name__ == '__main__':
    json =  {
      "nome": "thiago",
      "sobrenome": "araujo",
      "ddd": 61,
      "telefone": "993199244",
      "endereco": 'lala',
      "cargo": 'cabelereira'
    }

    f = funcionario(json)

    f.add_funcionario()