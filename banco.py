import sqlite3

from produto_digital import ProdutoDigital
from produto_fisico import ProdutoFisico

class BancoDeDados:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.conexao = None
    def conectar(self):
        self.conexao = sqlite3.connect(self.nome_banco)
    
    def desconectar(self):
        self.conexao.close()
    
    def criar_tabela(self):
        self.conectar()
        cursor = self.conexao.cursor()
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL, 
            preco REAL NOT NULL, 
            tipo TEXT NOT NULL,
            peso REAL,
            tamanho REAL
        )
        ''')
        self.conexao.commit()
        self.desconectar()

    def adicionar_produto(self, produto):
        self.conectar()
        cursor = self.conexao.cursor()

        tipo = ""
        peso = None
        tamanho = None

        if isinstance(produto, ProdutoFisico):
            tipo = "Fisico"
            peso = produto.peso
        elif isinstance(produto, ProdutoDigital):
            tipo = 'Digital'
            tamanho = produto.tamanho
        
        cursor.execute("""
        INSERT INTO produtos (nome, preco, tipo, peso, tamanho )
        VALUES (?,?,?,?,?)
        """, (produto.nome, produto.preco, tipo, peso, tamanho))
        self.conexao.commit()
        self.desconectar()
        print(f'Produto {produto.nome} salvo no banco com sucesso. ')

    def listar_produtos(self):
        self.conectar()
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        for p in produtos:
            print(f'ID: {p[0]}\nNome: {p[1]}\nPreço: R${p[2]}\nTipo: {p[3]}\nPeso: {p[4]}\nTamanho: {p[5]}')


            