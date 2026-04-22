import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pucprojeto import Operacoes

def test_inicializacao():
    op = Operacoes()
    assert op is not None

def test_lista_eh_dict():
    op = Operacoes()
    assert isinstance(op.lista, dict)

def test_legenda_valida():
    op = Operacoes()
    assert op.legenda[1] == 'estudante(s)'
    assert op.legenda[2] == 'professor(a/es)'

def test_chaves_lista():
    op = Operacoes()
    # Garante que existem as 5 categorias
    assert set(op.lista.keys()) == {1, 2, 3, 4, 5}

def test_processo_insercao():
    op = Operacoes()
    # Testa a inserção de um estudante
    op.incluir(1, 'Alice', 1231234)
    assert 'Alice' in op.lista[1]

    # Testa a inserção de um professor
    op.incluir(2, 'Pedro Silva', 123)
    assert 'Pedro Silva' in op.lista[2]