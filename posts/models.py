from django.db import models

class ConversionRequest(models.Model):
    url = models.URLField()
    email = models.EmailField()
    # Добавьте дополнительные поля по необходимости
    