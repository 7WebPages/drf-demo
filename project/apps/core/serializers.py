from rest_framework import serializers
from .models import University, Student


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
