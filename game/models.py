from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    access_scorefunction = models.DecimalField(db_column='access_ScoreFunction', max_digits=10, decimal_places=0)  # Field name made lowercase.
    initial_pop = models.IntegerField()
    email = models.CharField(max_length=254)
    initial_budget = models.DecimalField(max_digits=10, decimal_places=0)
    preventative_total = models.DecimalField(max_digits=10, decimal_places=0)
    acute_total = models.DecimalField(max_digits=10, decimal_places=0)
    ambulatory_total = models.DecimalField(max_digits=10, decimal_places=0)
    longterm_total = models.DecimalField(max_digits=10, decimal_places=0)
    pharmacy_total = models.DecimalField(max_digits=10, decimal_places=0)
    tax_total = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'game'


    def __str__(self):
        return self.game_id