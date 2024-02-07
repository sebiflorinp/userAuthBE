from django.db import models
from authentication.models import User


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.id} {self.userId} {self.name}"

