#Por a classe ser publica n seria nescessario fazer os get e set, mas como temos validação é nescessario os setters
#Deixei esses raise value error assim por que é para debugg no codigo o usuario vai digitar s(sim) ou n(não)

from pessoa import Pessoa
from presente import Presente

class Elfo(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str, especialidade: str, departamento: str):#para esses especialidade e departamento podemos fazer multipla escolha

        super().__init__(nome, sobrenome, idade, endereco)

        self.especialidade = especialidade
        self.departamento = departamento

    @property
    def especialidade(self):
        return self._especialidade
    
    @especialidade.setter
    def especialidade(self, valor: str):
        if isinstance(valor, str):
            self.especialidade = valor
        else:
            raise ValueError("A especialidade deve ser uma string.")

    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, valor: str):
        if isinstance(valor, str):
            self.departamento = valor
        else:
            raise ValueError("O departamento deve ser uma string.")
        
    def presente_feito(self, presente):
        if isinstance(presente, Presente):
            presente.presente_produzido = True
            print(f"O presente '{presente.nome_presente}' foi produzido pelo elfo {self._nome}.")
        else:
            raise ValueError("O argumento deve ser uma instância da classe Presente.")
