from django.contrib import admin
from . models import Clients, Work, Services, Profile, Social
# Register your models here.

admin.site.register(Clients)
admin.site.register(Work)
admin.site.register(Services)
admin.site.register(Profile)
admin.site.register(Social)

