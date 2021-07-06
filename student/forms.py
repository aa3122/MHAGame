from django import forms
from game.models import Game, Session
from django.contrib.auth.models import User

class SessionCreateForm(forms.ModelForm):
    game_tag = forms.CharField(max_length=30, required=True)
    class Meta:
        model = Session
        fields = ('game_tag',)

