from django.db import models
from django.db.models import Model

class Thing(Model):
    def __init__(self, name, description, quantity):
        self.name = name  # Attribute for first name
        self.description = description  # Attribute for last name
        self.quantity = quantity




