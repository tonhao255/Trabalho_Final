#Deixei esses raise value error assim por que é para debugg no codigo o usuario vai digitar s(sim) ou n(não)

from presente import Presente
from pessoa import Pessoa

class Claus(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str, licensa_treno: int):
        super().__init__(nome, sobrenome, idade, endereco)

        self.licensa_treno = licensa_treno

    @property
    def licensa_treno(self):
        return self._licensa_treno

    @licensa_treno.setter
    def licensa_treno(self, valor: int):
        if isinstance(valor, int) and valor > 0:
            self._licensa_treno = valor
        else:
            raise ValueError("A licença do trenó deve ser um número inteiro positivo.")

    def presente_entregado(self, presente):

        if isinstance(presente, Presente):
            presente.presente_entregue = True
            print(f"O presente '{presente.nome_presente}' foi entregue pelo Claus.")
        else:
            raise ValueError("O argumento deve ser uma instância da classe Presente.")
