from django.db import models


class Greeting(models.Model):
    message = models.CharField(max_length=255, default='Hello, CI/CD!')

    def __str__(self) -> str:
        return self.message
