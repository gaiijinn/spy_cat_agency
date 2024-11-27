from django.db import models
from cats.models import Cat

# Create your models here.


class Target(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')


class Mission(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.PROTECT, related_name="missions")
    target = models.ForeignKey(Target, on_delete=models.PROTECT, related_name="targets")

    def __str__(self):
        return f"Mission {self.pk} for {self.cat.name}"
