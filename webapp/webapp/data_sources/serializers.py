from rest_framework import serializers

from .import models


class CompanyOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyOfficer
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'
    
    def create(self, validated_data):
        return models.Company.objects.create(**validated_data)


class CompanyTickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ["symbol"]
