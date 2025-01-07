class Pessoa():
    def __init__(self, nome, sobrenome, idade, endereco):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._endereco = endereco



    @property
    def nome(self):
        return self.nome

    @property
    def sobrenome(self):
        return self.sobrenome

    @property
    def idade(self):
        return self.__idade


    @property
    def endereco(self):