from django.db import models

class CountryData(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    class Meta:
        verbose_name_plural = '각 나라별 인구 데이라'

    def __str__(self):
        return f'{self.country}--{self.population}'
