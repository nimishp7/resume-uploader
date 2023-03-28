from django.contrib import admin
from app.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'dob', 'state', 'gender', 'location']