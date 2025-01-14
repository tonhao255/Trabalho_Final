from pessoa import Pessoa

class Crianca(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str, 
                 chamine: bool, status_presentes: bool, lista_ranking: int):
        
        super().__init__(nome, sobrenome, idade, endereco)

        self._chamine = chamine
        self._status_presentes = status_presentes
        self._lista_ranking = lista_ranking

    @property
    def chamine(self):
        return self._chamine

    @chamine.setter
    def chamine(self, valor: bool):
        if isinstance(valor, bool):
            self._chamine = valor
        else:
            raise ValueError("O atributo 'chamine' deve ser do tipo bool.")

    @property
    def status_presentes(self):
        return self._status_presentes

    @status_presentes.setter
    def status_presentes(self, valor: bool):
        if isinstance(valor, bool):
            self._status_presentes = valor
        else:
            raise ValueError("O atributo 'status_presentes' deve ser do tipo bool.")

    @property
    def lista_ranking(self):
        return self._lista_ranking

    @lista_ranking.setter
    def lista_ranking(self, valor: int):
        if isinstance(valor, int):
            self._lista_ranking = valor
        else:
            raise ValueError("O atributo 'lista_ranking' deve ser um número inteiro)
        
    # CTRL + K + C: Comentar
    # CTRL + K + U: Descomentar

    # def mais_boazinha(self):
    #     #Num sei como fazer se vamos colocar um atributo pra isso, ou se vai involver a lista rank


    # def mais_malcriada(self):
    #     #The same thing
