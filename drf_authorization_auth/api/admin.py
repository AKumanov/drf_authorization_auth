from django.contrib import admin

# Register your models here.

from drf_authorization_auth.api.models import Profile

admin.site.register(Profile)
