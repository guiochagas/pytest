from carrinho import Produto, CarrinhoDeCompras
import pytest

@pytest.fixture
def carrinho_cheio():
    carrinho = CarrinhoDeCompras()

    produto1 = Produto(nome="Notebook", preco=3000)
    produto2 = Produto(nome="Teclado", preco=500)

    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)

    return carrinho

def test_calcular_total_sem_desconto(carrinho_cheio):
    total_carrinho = carrinho_cheio.calcular_total()
    assert total_carrinho == 3500

def test_calcular_total_com_desconto(carrinho_cheio):    
    total_carrinho = carrinho_cheio.calcular_total(desconto_percentual=20)
    assert total_carrinho == 2800

def test_desconto_fora_intervalo(carrinho_cheio):
    with pytest.raises(ValueError):
        carrinho_cheio.calcular_total(desconto_percentual=120)
    
    with pytest.raises(ValueError):
        carrinho_cheio.calcular_total(desconto_percentual=-20)
    
