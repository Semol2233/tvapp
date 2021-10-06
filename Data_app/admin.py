from django.contrib import admin
admin.site.site_header = "Nbox Tv App"
# Register your models here.
from django.contrib.auth.models import  Group
from .models import *

admin.site.unregister(Group)

admin.site.register(Add_Channel)
admin.site.register(Channel_catgory)
admin.site.register(Featrued_Channel)

















