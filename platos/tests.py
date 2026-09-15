from django.test import TestCase
from django.urls import reverse


class DetallePlatoTests(TestCase):
    def test_detalle_muestra_precio_con_propina_y_etiqueta_picante(self):
        response = self.client.get(reverse('platos:detalle', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Precio con propina (10%): $9790')
        self.assertContains(response, 'Contiene aji')

    def test_detalle_muestra_etiqueta_para_vegetariano(self):
        response = self.client.get(reverse('platos:detalle', args=[2]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Precio con propina (10%): $4950')
        self.assertContains(response, 'Apto para todos')

    def test_detalle_muestra_etiqueta_tradicional(self):
        response = self.client.get(reverse('platos:detalle', args=[3]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Precio con propina (10%): $14190')
        self.assertContains(response, 'Plato tradicional')
