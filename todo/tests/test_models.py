from utils.test_setup import TestSetup
from authentication.models import User
from todo.models import Todo


class TestModel(TestSetup):

    def test_should_create_todo(self):
        user = self.create_test_user()
        todo=Todo(owner=user, title="Buy milk",description="get it dome")
        todo.save()

        self.assertEqual(str(todo), "Buy milk")