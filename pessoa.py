class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, valor: str):
        self._sobrenome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor: str):
        self._endereco = valor
