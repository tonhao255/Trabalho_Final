from pessoa import Pessoa


class Elfo(Pessoa):
    def __init__(self, nome, sobrenome, idade, endereco, especialidade, departamento):
        super.__init__(self, nome, sobrenome, idade, endereco)

        self.especialidade = especialidade
        self.departamento = departamento


    @property
    def especialidade(self):
        return self._especialidade

    @property
    def departamento(self):
        return self._departamento