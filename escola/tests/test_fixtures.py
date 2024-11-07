from django.test import TestCase
from escola.models import Estudante, Curso


class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        """"Teste que verifica o carregamento da fixtures"""
        estudante = Estudante.objects.get(cpf='78120275977')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, "41 97097-5738")
        self.assertEqual(curso.codigo, "CPOO1")
