from django.db import models

class Burger(models.Model):
    TYPE_CHOICES = [
        ('Street', 'Street Burger'),
        ('Cheese', 'Cheese Burger'),
        ('Veggie', 'Veggie Burger'),
        ('BBQ', 'BBQ Burger'),
        ('Mushroom', 'Mushroom Burger'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="burgers/")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
