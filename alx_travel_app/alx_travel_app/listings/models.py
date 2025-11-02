from django.db import models

# Example model (can be expanded later)
class Listing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
