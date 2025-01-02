from pessoa import Pessoa


class Elfo(Pessoa):
    def __init__(self, nome, sobrenome, idade, endereco, especialidade, departamento):
        super.__init__(self, nome, sobrenome, idade, endereco)

        self.especialidade = especialidade
        self.departamento = departamento