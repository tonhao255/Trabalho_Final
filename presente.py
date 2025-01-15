class Presente:
    def __init__(self, nome_presente: str, tamanho_presente: int, 
                 presente_produzido: bool = False, presente_entregue: bool = False):
        self._nome_presente = nome_presente
        self._tamanho_presente = tamanho_presente
        self._presente_produzido = presente_produzido
        self._presente_entregue = presente_entregue


    @property
    def get_nome_presente(self):
        return self._nome_presente

    @get_nome_presente.setter
    def set_nome_presente(self, valor: str):
        self._nome_presente = valor

    @property
    def get_tamanho_presente(self):
        return self._tamanho_presente

    @get_tamanho_presente.setter
    def set_tamanho_presente(self, valor: int):
        self._tamanho_presente = valor

    @property
    def get_presente_produzido(self):
        return self._presente_produzido

    @get_presente_produzido.setter
    def set_presente_produzido(self, valor: bool):
        self._presente_produzido = valor

    @property
    def get_presente_entregue(self):
        return self._presente_entregue

    @get_presente_entregue.setter
    def set_presente_entregue(self, valor: bool):
        self._presente_entregue = valor
        
    def __str__(self):
        return f"Nome do presente: {self.get_nome_presente}\nTamanho do presente: {self.get_tamanho_presente}\nPresente produzido: {self.get_presente_produzido}\nPresente entregue: {self.get_presente_entregue}"
    
    def row(self):
        return [self.get_nome_presente,self.get_tamanho_presente,self.get_presente_produzido,self.get_presente_entregue]