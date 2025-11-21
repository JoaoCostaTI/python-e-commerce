from produto import Produto

class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
    
    def __repr__(self):
        return f"Produto: {self.nome} - Preço: R${self.preco:.2f} - Peso: {self.tamanho} MB"
    
    def calcular_frete(self):
        return 0

    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, value):
        if value <= 0:
            raise ValueError('Tamanho não pode ser menor que 0')
        self._tamanho = value

