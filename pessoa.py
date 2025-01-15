class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__endereco = endereco

    @property
    def get_nome(self):
        return self.__nome

    @get_nome.setter
    def set_nome(self, valor: str):
        self.__nome = valor

    @property
    def get_sobrenome(self):
        return self.__sobrenome

    @get_sobrenome.setter
    def set_sobrenome(self, valor: str):
        self.__sobrenome = valor

    @property
    def get_idade(self):
        return self.__idade

    @get_idade.setter
    def set_idade(self, valor):
        self.__idade = valor

    @property
    def get_endereco(self):
        return self.__endereco

    @get_endereco.setter
    def set_endereco(self, valor: str):
        self.__endereco = valor
