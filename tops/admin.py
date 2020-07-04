from django.contrib import admin

# Register your models here.
from .models import Score, Rank

admin.site.register(Score)
admin.site.register(Rank)
