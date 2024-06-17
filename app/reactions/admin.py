from django.contrib import admin
from .models import Reaction


@admin.register(Reaction)
class ReactionModel(admin.ModelAdmin):
    pass
