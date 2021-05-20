from django import forms
from game.models import Game, Session


class SessionCreateForm(forms.ModelForm):
	class Meta:
		model = Session
		fields =('gameid', 'student', 'prev_expenses', 'acute_expenses', 'ambul_expenses', 'long_expenses', 'pharm_expenses', 'tax_total',)
		