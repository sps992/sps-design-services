from django.test import TestCase
from .models import Service

# Create your tests here.


class ServiceTest(TestCase):
    """
    Defining the tests that we will run
    against our Service models
    """

    def test_str(self):
        test_name = Service(name='Test Service')
        self. assertEqual(str(test_name), 'Test Service')
