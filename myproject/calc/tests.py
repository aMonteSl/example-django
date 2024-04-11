from django.test import TestCase, Client

# Create your tests here.


class CalcTest(TestCase):

    def test_suma(self):
        """Si la suma funciona"""
        client = Client()
        response = self.client.get('/calc/suma/3/4')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('7', content)

    def test_resta(self):
        """Si la resta funciona"""
        client = Client()
        response = self.client.get('/calc/resta/3/4')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('-1', content)

    def test_only_integers(self):
        """Si solo se aceptan enteros"""
        client = Client()
        response = self.client.get('/calc/suma/3.14/4')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/calc/suma/3/4.14')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/calc/suma/3.14/4.14')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/calc/suma/3/cuatro')
        self.assertEqual(response.status_code, 404)
