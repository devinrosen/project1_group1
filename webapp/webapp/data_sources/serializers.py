from rest_framework import serializers

from .import models


class CompanyOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyOfficer
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    companyOfficers = CompanyOfficerSerializer(many=True)

    class Meta:
        model = models.Company
        fields = '__all__'
    
    def create(self, validated_data):
        company_officers = validated_data.pop('companyOfficers')
        company = models.Company.objects.create(**validated_data)
        for company_officer in company_officers:
            models.CompanyOfficer.objects.create(
                company=company,
                **company_officer,
            )
        return company


class CompanyTickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ["symbol"]
