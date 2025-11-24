import pytest

@pytest.fixture
def lista_simples():
    return [1, 2, 3, 4, 5]

def soma_dobro(lista_simples):
    numeros_dobrados = [x * 2 for x in lista_simples]
    total = sum(numeros_dobrados)
    return numeros_dobrados, total

def test_soma_dobro(lista_simples):
    numeros, total = soma_dobro(lista_simples)

    print("Números dobrados:", numeros)
    print("Total:", total)

    assert numeros == [2, 4, 6, 8, 10]

    assert total == 30