from django.db import models


class CowInput(models.Model):
    cow_input = models.TextField()

    def __str__(self):
        return self.cow_input
