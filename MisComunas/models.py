import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_habitantes = models.IntegerField(default=0)
    vulnerabilidad = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
    )
    fecha_fundacion = models.DateField(default=datetime.date(2000, 1, 1))

    def __str__(self):
        return self.nombre
