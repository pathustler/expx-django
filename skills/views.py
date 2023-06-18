from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from skills.models import SkillModel, ReviewModel, DayModel
from skills.serializers import SkillModel_serializer, ReviewModel_serializer, DayModel_serializer
# Create your views here.


class SkillModel_ViewSet(viewsets.ModelViewSet):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModel_serializer
    
class ReviewModel_ViewSet(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewModel_serializer
    
class DayModel_ViewSet(viewsets.ModelViewSet):
    queryset = DayModel.objects.all()
    serializer_class = DayModel_serializer
    