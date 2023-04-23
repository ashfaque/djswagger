from .models import *
from django.contrib import admin

# Register your models here.


@admin.register(SwaggerTest)
class SwaggerTest(admin.ModelAdmin):
    list_display = [field.name for field in SwaggerTest._meta.fields]
    search_fields = ('__all__',)
