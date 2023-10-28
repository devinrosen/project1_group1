import logging

from rest_framework import serializers

from .import models

logging.basicConfig()
log = logging.getLogger(__name__)


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'

    def validate_holdings(self, value):
        if not value:
            raise serializers.ValidationError("This field may not be blank.")
        if not isinstance(value, dict):
            raise serializers.ValidationError("This field must be a json dictionary {'symbol':'percent'}.")

        sum = 0
        for k, v in value.items():
            sum += v
        
        if sum != 1:
            raise serializers.ValidationError("The sum of percents must equal 1")
        log.info(f"value {value}")
        return value
