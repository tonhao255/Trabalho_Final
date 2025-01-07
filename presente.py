class Presente():
    def __init__(self, nome, tamanho, presente_produzido, presente_entregue):
        self.nome = nome
        self.tamanho = tamanho
        self.presente_produzido = presente_produzido
        self.presente_entregue = presente_entregue

    @property
    def nome(self):
        return self.nome
    
    @Property
    def tamanho(self):
        return self.tamanho

    @property
    def presente_produzido(self):
        return self.presente_produzido

    @property
    def presente_entregue(self):
        return self.presente_entregue

