from pessoa import Pessoa


class Crianca(Pessoa):
    def __init__(self, nome, sobrenome, idade, endereco, chamine, status_presentes, lista_ranking):
        super.__init__(self, nome, sobrenome, idade, endereco)

        self._ chamine = chamine
        self._status_presentes = status_presentes
        self._lista_ranking = lista_ranking

    


    @property
    def chamine(self):
        return self._chamine

    
    @chamine.setter
    def chamine(self, chamnine):
        self._chamine = chamnine

    
    @property
    def status_presentes(self):
        return self._status_presentes

    @status_presentes.setter
    def status_presentes(self, status_presentes):
        self._status_presentes = status_presentes

    
    @property
    def lista_ranking(self):
        return self._lista_ranking

    @lista_ranking.setter
    def lista_ranking(self, lista_ranking):
        self._lista_ranking = lista_ranking
