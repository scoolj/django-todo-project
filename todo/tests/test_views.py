from urllib import response

from django.urls import reverse
from utils.test_setup import TestSetup
from authentication.models import User
from todo.models import Todo


class TestModel(TestSetup):

    def  test_Should_create_a_todo(self):
        user =self.create_test_user()
        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!'
        })
        todos = Todo.objects.all()
        self.assertEqual(todos.count(), 0)
        response = self.client.post(reverse('create-todo'), {
            'owner': user,
            'title': "Hello do this",
            "description": "Remember to do this"
        })

        print(response)

        updated_todos = Todo.objects.all()
        self.assertEqual(updated_todos.count(),1)
        self.assertEqual(response.status_code, 302)