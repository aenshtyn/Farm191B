from django.contrib import admin
from .models import Cow, Calf, MorningMilk, AfternoonMilk, EveningMilk
# Register your models here.
admin.site.register(Cow)
admin.site.register(Calf)
admin.site.register(MorningMilk)
admin.site.register(AfternoonMilk)
admin.site.register(EveningMilk)
# admin.site.register()