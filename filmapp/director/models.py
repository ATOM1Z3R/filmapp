from django.db import models
import datetime

class Director(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    birth_date = models.DateField(blank=False)
    death_date = models.DateField(blank=True, default=None, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    @property
    def age(self):
        if self.death_date != None:
            return self.death_date.year - self.birth_date.year
        return datetime.date.today().year - self.birth_date.year