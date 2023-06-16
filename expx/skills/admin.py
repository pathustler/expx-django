from django.contrib import admin
from .models import DayModel, SkillModel, ReviewModel
# Register your models here.

admin.site.register(DayModel)
admin.site.register(SkillModel)
admin.site.register(ReviewModel)