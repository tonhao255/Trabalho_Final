from pessoa import Pessoa


class Claus(Pessoa):
    def __init__(self, nome, sobrenome, idade, endereco, licensa_treno):
        super.__init__(self, nome, sobrenome, idade, endereco)

        self.__licensa_treno = licensa_treno

    
    @property
    def get_licensa_treno(self):
        return self.__licensa_treno

    @get_licensa_treno.setter
    def get_licensa_treno(self, nova_licensa):
        if not isinstance(nova_licensa, str):
            raise ValueError("A licença de treino deve ser uma string.")
        self.__licensa_treno = nova_licensa
