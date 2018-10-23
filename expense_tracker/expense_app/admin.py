from django.contrib import admin

from .models import User
from .models import Withdaraw
from .models import Deposit

admin.site.register(User)
admin.site.register(Withdaraw)
admin.site.register(Deposit)