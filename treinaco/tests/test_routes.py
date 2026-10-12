"""Testes simples. Executar: python -m unittest discover -s tests"""
import unittest

from app import app
from data import listar_treinos


class TestSite(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_inicio(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"BLUE REP", response.data)

    def test_treinos(self):
        for treino in listar_treinos():
            response = self.client.get(f'/treino/{treino["id"]}')
            self.assertEqual(response.status_code, 200)
            for exercicio in treino["exercicios"]:
                self.assertIn(exercicio["nome"].encode(), response.data)

    def test_exercicios_estrutura(self):
        for treino in listar_treinos():
            self.assertTrue(treino["exercicios"])
            for ex in treino["exercicios"]:
                self.assertGreater(ex["series"], 0)
                self.assertGreater(ex["descanso"], 0)
                self.assertTrue(ex["dicas"])

    def test_404(self):
        self.assertEqual(self.client.get("/treino/inexistente").status_code, 404)

    def test_assets(self):
        self.assertEqual(self.client.get("/assets/styles/main.css").status_code, 200)


if __name__ == "__main__":
    unittest.main()
