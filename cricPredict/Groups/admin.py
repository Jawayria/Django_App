from django.contrib import admin
from .models import Group
from .models import UserGroup

admin.site.register(Group)
admin.site.register(UserGroup)
