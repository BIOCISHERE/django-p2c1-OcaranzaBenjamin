from django.test import TestCase


class ZonasViewsTest(TestCase):
    def test_listado_de_zonas_muestra_limites_y_estados(self):
        response = self.client.get('/zonas/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bodega Norte')
        self.assertContains(response, 'Oficina Central')
        self.assertContains(response, 'Planta Sur')
        self.assertContains(response, '500 kWh')
        self.assertContains(response, 'ALERTA')

    def test_detalle_de_zona_muestra_dispositivos_y_estado(self):
        response = self.client.get('/zonas/2/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Oficina Central')
        self.assertContains(response, 'ALERTA')
        self.assertContains(response, 'Consumo total')
        self.assertContains(response, 'Aire Acondicionado Oficina')
        self.assertContains(response, 'Volver al listado')
        self.assertContains(response, 'href="/zonas/"')

    def test_catalogo_muestra_todos_los_dispositivos(self):
        response = self.client.get('/dispositivos/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aire Acondicionado A1')
        self.assertContains(response, 'Aire Acondicionado Oficina')
        self.assertContains(response, 'Servidor de Produccion')
        self.assertContains(response, 'Catálogo de dispositivos')
