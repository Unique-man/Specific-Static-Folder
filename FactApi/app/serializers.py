from rest_framework import serializers
from app.models import Fact

class FactMS(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = '__all__'
