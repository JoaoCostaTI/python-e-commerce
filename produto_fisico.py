from produto import Produto

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    def __repr__(self):
        return f"Produto: {self.nome} - Preço: R${self.preco:.2f} - Peso: {self.peso}KG"
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, value):
        if value <= 0:
            raise ValueError('Peso não pode ser negativo nem 0')
        self._peso = value
    