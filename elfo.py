#Por a classe ser publica n seria nescessario fazer os get e set, mas como temos validação é nescessario os setters
#Deixei esses raise value error assim por que é para debugg no codigo o usuario vai digitar s(sim) ou n(não)

from pessoa import Pessoa
from presente import Presente

class Elfo(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str, especialidade: str, departamento: str):#para esses especialidade e departamento podemos fazer multipla escolha

        super().__init__(nome, sobrenome, idade, endereco)

        self.__especialidade = especialidade
        self.__departamento = departamento

    @property
    def get_especialidade(self):
        return self.__especialidade
    
    @get_especialidade.setter
    def set_especialidade(self, valor: str):
        self.__especialidade = valor

    @property
    def get_departamento(self):
        return self.__departamento
    
    @get_departamento.setter
    def set_departamento(self, valor: str):
        self.__departamento = valor

    def __str__(self):
        return f'Elfo: {self.get_nome} {self.get_sobrenome}\nIdade: {self.get_idade}\nEndereço: {self.get_endereco}\nEspecialidade: {self.__especialidade}\nDepartamento: {self.__departamento}'
    
    def row(self):
        return [self.get_nome,self.get_sobrenome,self.get_idade,self.get_endereco,self.__especialidade,self.__departamento]
