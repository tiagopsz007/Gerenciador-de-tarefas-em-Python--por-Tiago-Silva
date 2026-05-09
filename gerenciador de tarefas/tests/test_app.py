import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from app import validar_prioridade


# -----------------------------
# TESTES DE LÓGICA (100% OK)
# -----------------------------

def test_prioridade_valida():
    assert validar_prioridade("Alta") == True
    assert validar_prioridade("Média") == True
    assert validar_prioridade("Baixa") == True


def test_prioridade_invalida():
    assert validar_prioridade("Ultra") == False
    assert validar_prioridade("") == False
    assert validar_prioridade("123") == False
