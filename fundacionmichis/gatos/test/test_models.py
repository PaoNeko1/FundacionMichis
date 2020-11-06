from django.test import TestCase
from gatos.models import Gatitos, Padres



class GatitosTestCase(TestCase):

    def setUp(self):
        
        Gatitos.objects.create(id = "404", nombre = "Dixy", edad = 2)


    def test_gatitos(self):

        gatitos = Gatitos.objects.get(id = "404")
        self.assertEqual(gatitos.nombre , "Dixy")


class PadresTestCase(TestCase):

    def setUp(self):
        
        Padres.objects.create(rut = "187881439", nom = "marcopolo", fono = 12345678)


    def test_padres(self):

        padres = Padres.objects.get(rut = "187881439")
        self.assertEqual(padres.nom , "marcopolo")
#py manage.py test




