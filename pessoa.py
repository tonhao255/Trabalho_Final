class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__endereco = endereco

    @property
    def nomeDef(self):
        return self.__nome

    @nomeDef.setter
    def nomeDef(self, valor: str):
        self.__nome = valor

    @property
    def sobrenomeDef(self):
        return self.__sobrenome

    @sobrenomeDef.setter
    def sobrenomeDef(self, valor: str):
        self.__sobrenome = valor

    @property
    def idadeDef(self):
        return self.__idade

    @idadeDef.setter
    def idadeDef(self, valor):
        self.__idade = valor

    @property
    def enderecoDef(self):
        return self.__endereco

    @enderecoDef.setter
    def enderecoDef(self, valor: str):
        self.__endereco = valor
