from django.urls import re_path, include
from rest_framework import routers
from skills.views import SkillModel_ViewSet, ReviewModel_ViewSet, DayModel_ViewSet
router = routers.DefaultRouter()
router.register(r'skills', SkillModel_ViewSet)
router.register(r'reviews', ReviewModel_ViewSet)
router.register(r'days', DayModel_ViewSet)
urlpatterns = [
    re_path(r'^', include(router.urls))
]