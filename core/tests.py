from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Todo


class TodoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', password='test')
        self.user.save()

    def test_system(self):
        # Logging
        login = self.client.login(username='test', password='test')
        self.assertEquals(login, True)
        response = self.client.get(reverse('new_to_do'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'test')

        # Todo Test
        self.client.post('/todo/new/', {'title': "test_title", 'text': "test_text"})
        self.assertIsInstance(Todo.objects.last(), Todo)

        # Checking inserted tasks
        self.assertEqual(Todo.objects.last().title, 'test_title')
        self.assertEqual(Todo.objects.last().text, 'test_text')