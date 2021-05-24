from django.contrib import admin
from .models import Game, Session

# Register your models here.
admin.site.register(Game)
admin.site.register(Session)

class YourAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):                
        if Session.student == 'user': kwargs['queryset'] = User.objects.filter(user=request.user)