
import nbformat
import sys
from io import StringIO
from IPython import get_ipython

# Função para executar o notebook e obter a função soma
def get_function_from_notebook(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
        for cell in nb.cells:
            if cell.cell_type == "code":
                exec(cell.source, globals())

get_function_from_notebook("exercicios/data-types.ipynb")


def test_exercicio1():
    assert nome == "Python"

def test_resultado_soma():
    assert resultado_soma == 30

def test_tipo_valor():
    assert tipo_valor == type(123.45)

def test_x_maior_que_y():
    assert x_maior_que_y == True

def test_resultado_subtracao():
    assert resultado_subtacao == 5

def test_resultado_divisao():
    assert resultado_divisao == 1.5

def test_resultado_divisao_inteira():
    assert resultado_divisao_inteira == 1

def test_resultado_exponenciacao():
    assert resultado_exponenciacao == 576650390625

def test_fahrenheit():
    assert fahrenheit == 75.2

def test_media():
    assert media == 7.6

def test_nome_completo():
    assert nome_completo == 'João Silva'

def test_materia():
    assert materia == 'Computacional Thinking'

def test_texto_maiusculo():
    assert texto_maiusculo == 'OLÁ, MUNDO!'


def test_texto_substituido():
    assert texto_substituido == 'OLÁ, UNIVERSO!'

def test_dolar():
    assert dolar == 164.96749521988525

def test_esta_equilibrado():
    assert texto_maiusculo == 'OLÁ, MUNDO!'

def test_texto_maiusculo():
    assert texto_maiusculo == 'OLÁ, MUNDO!'

def test_mobile():
    assert mobile(12,3,3, 6) == True
    assert mobile(13,3,3, 6) == False

