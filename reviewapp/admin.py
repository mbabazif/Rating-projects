from django.contrib import admin

from .models import tags,Location,Project,Profile,Image

admin.site.register(tags)
admin.site.register(Location)
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Image)


# Register your models here.
