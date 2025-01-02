from pessoa import Pessoa


class Claus(Pessoa):
    def __init__(self, nome, sobrenome, idade, endereco, licensa_treno):
        super.__init__(self, nome, sobrenome, idade, endereco)

        self.licensa_treno = licensa_treno