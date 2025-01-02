from pessoa import Pessoa


class Crianca(Pessoa):
    def __init__(self, nome, sobrenome, idade, endereco, chamine, status_presentes, lista_ranking):
        super.__init__(self, nome, sobrenome, idade, endereco)

        self.chamine = chamine
        self.status_presentes = status_presentes
        self.lista_ranking = lista_ranking