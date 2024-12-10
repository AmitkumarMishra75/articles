from django.contrib import admin
from .models import Articles

# Register your models here.
@admin.register(Articles)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','heading','content']