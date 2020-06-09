from django.db import models
from django.contrib.auth.models import User

class Assets(models.Model):
    name = models.CharField(max_length=100)
    worth = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_object = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}'s {self.name}"

class Liabilities(models.Model):
    name = models.CharField(max_length=100)
    worth = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_object = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}'s {self.name}"

class Expenses(models.Model):
    name = models.CharField(max_length=100)
    worth = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_object = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}'s {self.name}"

class SourceOfIncome(models.Model):
    name = models.CharField(max_length=100)
    worth = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_object = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}'s {self.name}"




