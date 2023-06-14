from rest_framework import serializers

from skills.models import SkillModel, ReviewModel, DayModel

class SkillModel_serializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = '__all__'

class ReviewModel_serializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'


class DayModel_serializer(serializers.ModelSerializer):
    class Meta:
        model = DayModel
        fields = '__all__'
