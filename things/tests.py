from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Model

class ThingsTest(TestCase):
    def setUp(self):
        self.user=Model.objects.create_user(
           '@TV',
            name='TV',
            description='screeen',
            quantity=5
        )

