#Deixei esses raise value error assim por que é para debugg no codigo o usuario vai digitar s(sim) ou n(não)

from pessoa import Pessoa

class Crianca(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade, endereco: str, 
                 chamine: bool, status_presentes: bool, lista_ranking: int):
        
        super().__init__(nome, sobrenome, idade, endereco)

        self._chamine = chamine
        self._status_presentes = status_presentes
        self._lista_ranking = lista_ranking

    @property
    def get_chamine(self):
        return self._chamine

    @get_chamine.setter
    def set_chamine(self, valor: bool):
        self._chamine = valor

    @property
    def get_status_presentes(self):
        return self._status_presentes

    @get_status_presentes.setter
    def set_status_presentes(self, valor: bool):
        self._status_presentes = valor

    @property
    def get_lista_ranking(self):
        return self._lista_ranking

    @get_lista_ranking.setter
    def set_lista_ranking(self, valor: int):
        self._lista_ranking = valor
        
    def __str__(self):
        return f'Criança: {self.get_nome} {self.get_sobrenome}\nIdade: {self.get_idade}\nEndereço: {self.get_endereco}\nChamine: {self.get_chamine}\nPresentes: {self.get_status_presentes}\nLista Ranking: {self.get_lista_ranking}'
    
    def row(self):
        return [self.get_nome,self.get_sobrenome,self.get_idade,self.get_endereco,self.get_chamine,self.get_status_presentes,self.get_lista_ranking]
        
    # CTRL + K + C: Comentar
    # CTRL + K + U: Descomentar

    # def mais_boazinha(self):
    #     #Num sei como fazer se vamos colocar um atributo pra isso, ou se vai involver a lista rank


    # def mais_malcriada(self):
    #     #The same thing
