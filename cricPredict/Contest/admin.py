from django.contrib import admin
from .models import Match
from .models import UserMatch
from .models import League
from .models import GroupLeague
from .models import Score

admin.site.register(Match)
admin.site.register(UserMatch)
admin.site.register(League)
admin.site.register(GroupLeague)
admin.site.register(Score)
