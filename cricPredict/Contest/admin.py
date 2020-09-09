from django.contrib import admin
from .models import Match
from .models import League
from .models import Prediction

admin.site.register(Match)
admin.site.register(Prediction)
admin.site.register(League)
