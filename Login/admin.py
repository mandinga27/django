from django.contrib import admin
from .models import UserProfile, UserLanguage, Language

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserLanguage)
admin.site.register(Language)