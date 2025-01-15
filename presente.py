class Presente:
    def __init__(self, nome_presente: str, tamanho_presente: int, 
                 presente_produzido: bool = False, presente_entregue: bool = False):
        self.nome_presente = nome_presente
        self.tamanho_presente = tamanho_presente
        self.presente_produzido = presente_produzido
        self.presente_entregue = presente_entregue


    @property
    def get_nome_presente(self):
        return self._nome_presente

    @get_nome_presente.setter
    def set_nome_presente(self, valor: str):
        if isinstance(valor, str):
            self._nome_presente = valor
        else:
            raise ValueError("O nome do presente deve ser uma string.")

    @property
    def get_tamanho_presente(self):
        return self._tamanho_presente

    @get_tamanho_presente.setter
    def set_tamanho_presente(self, valor: int):
        if isinstance(valor, int) and valor > 0:
            self._tamanho_presente = valor
        else:
            raise ValueError("O tamanho do presente deve ser um número inteiro positivo.")

    @property
    def get_presente_produzido(self):
        return self._presente_produzido

    @get_presente_produzido.setter
    def set_presente_produzido(self, valor: bool):
        if isinstance(valor, bool):
            self._presente_produzido = valor
        else:
            raise ValueError("O atributo 'presente_produzido' deve ser do tipo bool.")

    @property
    def get_presente_entregue(self):
        return self._presente_entregue

    @get_presente_entregue.setter
    def set_presente_entregue(self, valor: bool):
        if isinstance(valor, bool):
            self._presente_entregue = valor
        else:
            raise ValueError("O atributo 'presente_entregue' deve ser do tipo bool.")
        
    def __str__(self):
        return f"Nome do presente: {self.get_nome_presente}\nTamanho do presente: {self.get_tamanho_presente}\nPresente produzido: {self.get_presente_produzido}\nPresente entregue: {self.get_presente_entregue}"
    
    def row(self):
        return [self.get_nome_presente,self.get_tamanho_presente,self.get_presente_produzido,self.get_presente_entregue]