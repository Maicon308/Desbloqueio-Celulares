from django.db import models

class Aparelho(models.Model):
    MARCAS = [
        ('SAMSUNG', 'Samsung'),
        ('MOTOROLA', 'Motorola'),
        ('XIAOMI', 'Xiaomi'),
        ('IPHONE', 'iPhone'),
        ('LG', 'LG'),
        ('MULTILASER','Multilaser'),
        ('ASUS','Asus'),
    ]

    marca = models.CharField(max_length=20, choices=MARCAS)
    modelo = models.CharField(max_length=100)
    preco_desbloqueio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.marca} {self.modelo}'
