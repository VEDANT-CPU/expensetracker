from django.contrib import admin

# Register your models here.

from .models import transaction

admin.site.register(transaction)