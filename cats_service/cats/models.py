from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=256)
    breed = models.CharField(max_length=256)
    years_of_experience = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.name

