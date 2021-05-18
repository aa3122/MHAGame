from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    cost = models.DecimalField(max_digits=10, decimal_places=0)
    access_scorefunction = models.DecimalField(db_column='access_ScoreFunction', max_digits=10, decimal_places=0)  # Field name made lowercase.
    initial_pop = models.IntegerField()
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'game'
    def __str__(self):
        return self.game_id