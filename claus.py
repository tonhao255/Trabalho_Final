from presente import Presente
from pessoa import Pessoa

class Claus(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str, licensa_treno: int):
        super().__init__(nome, sobrenome, idade, endereco)

        self._licensa_treno = licensa_treno

    @property
    def get_licensa_treno(self):
        return self._licensa_treno

    @get_licensa_treno.setter
    def set_licensa_treno(self, valor: int):
        self._licensa_treno = valor
        
    def __str__(self):
        return f'Papai Noel: {self.get_nome} {self.get_sobrenome}\nIdade: {self.get_idade}\nEndereço: {self.get_endereco}\nLicensa: {self.get_licensa_treno}'
    
    def row(self):
        return [self.get_nome,self.get_sobrenome,self.get_idade,self.get_endereco,self.get_licensa_treno]
