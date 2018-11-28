from django.contrib import admin

from . import models

admin.site.register(models.Ask)
admin.site.register(models.Answer)
admin.site.register(models.Game)
admin.site.register(models.Name)
admin.site.register(models.Results)