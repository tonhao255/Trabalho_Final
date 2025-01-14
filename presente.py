#Deixei esses raise value error assim por que é para debugg no codigo o usuario vai digitar s(sim) ou n(não)
#Por a classe ser publica n seria nescessario fazer os get e set, mas como temos validação é nescessario os setters

class Presente:
    def __init__(self, nome_presente: str, tamanho_presente: int, 
                 presente_produzido: bool = False, presente_entregue: bool = False):
        self.nome_presente = nome_presente
        self.tamanho_presente = tamanho_presente
        self.presente_produzido = presente_produzido
        self.presente_entregue = presente_entregue


    @property
    def nome_presente(self):
        return self._nome_presente

    @nome_presente.setter
    def nome_presente(self, valor: str):
        if isinstance(valor, str):
            self._nome_presente = valor
        else:
            raise ValueError("O nome do presente deve ser uma string.")

    @property
    def tamanho_presente(self):
        return self._tamanho_presente

    @tamanho_presente.setter
    def tamanho_presente(self, valor: int):
        if isinstance(valor, int) and valor > 0:
            self._tamanho_presente = valor
        else:
            raise ValueError("O tamanho do presente deve ser um número inteiro positivo.")

    @property
    def presente_produzido(self):
        return self._presente_produzido

    @presente_produzido.setter
    def presente_produzido(self, valor: bool):
        if isinstance(valor, bool):
            self._presente_produzido = valor
        else:
            raise ValueError("O atributo 'presente_produzido' deve ser do tipo bool.")

    @property
    def presente_entregue(self):
        return self._presente_entregue

    @presente_entregue.setter
    def presente_entregue(self, valor: bool):
        if isinstance(valor, bool):
            self._presente_entregue = valor
        else:
            raise ValueError("O atributo 'presente_entregue' deve ser do tipo bool.")

    def exibir_informacoes(self):
        return (f"Presente: {self.nome_presente}, "
                f"Tamanho: {self.tamanho_presente}, "
                f"Produzido: {'Sim' if self.presente_produzido else 'Não'}, "
                f"Entregue: {'Sim' if self.presente_entregue else 'Não'}")

