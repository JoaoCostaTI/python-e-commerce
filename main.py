from produto import Produto
from produto_digital import ProdutoDigital
from produto_fisico import ProdutoFisico



produtos = [
    ProdutoDigital('Mario Kart', 299.99, 155),
    ProdutoDigital('Zelda: Breath of the Wild', 349.90, 120),
    ProdutoDigital('Hollow Knight', 49.99, 30),
    ProdutoDigital('Stardew Valley', 24.99, 15),
    ProdutoDigital('Metroid Dread', 299.99, 80)
]
produtos_fisicos = [
    ProdutoFisico('Skate', 150, 3),
    ProdutoFisico('Bicicleta', 899.90, 10),
    ProdutoFisico('Capacete', 120.00, 25),
    ProdutoFisico('Luva de Boxe', 89.90, 12),
    ProdutoFisico('Patins', 350.00, 8)
]

produtos.sort(reverse= True)
produtos_fisicos.sort(reverse=True)

print('Produtos Digitais')
for p in produtos:
    print(p)

print('Produtos Físicos')
for p in produtos_fisicos:
    print(p)

