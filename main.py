from produto import Produto
from produto_digital import ProdutoDigital
from produto_fisico import ProdutoFisico
from banco import BancoDeDados

loja = BancoDeDados('loja.db')
loja.criar_tabela()

print("\n--- Teste de Segurança: Tentando criar Produto Abstrato ---")
try:
    # Isso deve ser PROIBIDO pelo Python agora
    p_invalido = Produto("Teste", 10) 
    print("ERRO: O sistema permitiu criar um Produto genérico!")
except TypeError:
    print("SUCESSO: O sistema bloqueou a criação de um Produto genérico.")

produtos_digitais = [
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

produtos_digitais.sort(reverse= True)
produtos_fisicos.sort(reverse=True)

todos_produtos = [produtos_fisicos, produtos_digitais]

"""
for i in todos_produtos:
    for p in i:
        loja.adicionar_produto(p)
        frete = p.calcular_frete()
        print(f"Nome: {p.nome} - Preco R${p.preco:.2f} - Frete: R${frete:.2f}")
"""

loja.listar_produtos()