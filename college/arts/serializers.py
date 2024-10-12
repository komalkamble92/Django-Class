#  pip install djangorestframework

from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'date_of_birth']