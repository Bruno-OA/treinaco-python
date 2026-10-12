"""Cadastro central dos treinos. Importe um novo arquivo aqui para adicionar um treino."""
from .treino_a import TREINO_A
from .treino_b import TREINO_B
from .treino_c import TREINO_C

TREINOS = [TREINO_A, TREINO_B, TREINO_C]


def listar_treinos():
    return TREINOS


def buscar_treino(treino_id):
    return next((t for t in TREINOS if t["id"] == treino_id.lower()), None)
