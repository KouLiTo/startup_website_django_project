from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Feedback)
admin.site.register(models.Projects)
admin.site.register(models.Basic)
admin.site.register(models.Standard)
admin.site.register(models.Premium)
