from django.test import TestCase, Client
from .views import Counter

# Create your tests here.


class CounterTest(TestCase):

    def test_creation(self):
        """Si la creacion funciona"""
        counter = Counter()
        self.assertEqual(counter.count, 0)

    def test_increment(self):
        """Si el incremento funciona"""
        counter = Counter()
        number = counter.increment()
        self.assertEqual(counter.count, 1)
        number = counter.increment()
        self.assertEqual(counter.count, 2)
        number = counter.increment()
        self.assertEqual(number, 3)


class CmsTest(TestCase):

    def test_index(self):
        """Si la vista index funciona"""
        cliente = Client()
        response = cliente.get('/cms/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertInHTML('<h1>Django CMS</h1>', content)

    def test_not_found(self):
        """Si la vista get_content funciona"""
        cliente = Client()
        response = cliente.get('/cms/contenido_inexistente')
        self.assertEqual(response.status_code, 404)

    def test_actualizar_crear_contenido(self):
        """Si la vista actualizar_contenido funciona"""
        cliente = Client()
        response = cliente.post('/cms/contenido_prueba',
                                {'valor': 'contenido de prueba'})
        self.assertEqual(response.status_code, 200)
        response = cliente.get('/cms/contenido_prueba')
        self.assertEqual(response.status_code, 200)

    def test_found(self):
        """Si la vista get_content funciona"""
        cliente = Client()
        response = cliente.post('/cms/contenido_prueba',
                                {'valor': 'contenido de prueba'})
        response = cliente.get('/cms/contenido_prueba')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertInHTML('contenido de prueba', content)
