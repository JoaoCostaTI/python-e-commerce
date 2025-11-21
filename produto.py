from functools import total_ordering

@total_ordering
class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto: {self.nome} - Preço: R${self.preco:.2f}\n"
    
    #Protegendo Preço
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, value):
        if value < 0:
            raise ValueError('Preço não pode ser negativo! ')
        self._preco = value


    def __eq__(self, value):
        if not isinstance(value, Produto):
            return NotImplemented
        return self.nome == value.nome and self.preco == value.preco

    def __lt__(self, value):
        if not isinstance(value, Produto):
            return NotImplemented
        return self.preco < value.preco
    

