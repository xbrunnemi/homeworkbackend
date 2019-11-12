from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Soldier(models.Model):
    CHOICES = (
        ('A', 'Air Force'),
        ('N', 'Navy'),
        ('G', 'Ground Force')
    )

    first_name = models.TextField()
    last_name = models.TextField()
    date_of_birth = models.DateField()
    arm_of_service = models.CharField(max_length=1, choices=CHOICES, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.first_name} {0.last_name} {0.date_of_birth} {0.arm_of_service} {0.country}'
        return template.format(self)
