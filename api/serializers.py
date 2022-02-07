from rest_framework import serializers
from timetable_app.models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        # name = serializers.ReadOnlyField()

        model = Course
        fields = ['id', 'code', 'name', 'capacity']


class CourseCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        # name = serializers.ReadOnlyField()

        model = Course
        fields = ['id']
        read_only_fields = ['code', 'name', 'capacity']
