import logging

from rest_framework import serializers

from .import models
from .utils import validate_symbol

logging.basicConfig()
log = logging.getLogger(__name__)


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'

    def validate_holdings(self, value):
        # value is required
        if not value:
            raise serializers.ValidationError("This field may not be blank.")

        #value must be a dict
        if not isinstance(value, dict):
            raise serializers.ValidationError("This field must be a json dictionary {'symbol':'weight'}.")

        sum = 0
        for k, v in value.items():
            sum += v
            try:
                validate_symbol(k)
            except Exception:
                raise serializers.ValidationError(f"Unable to validate symbol {k}.")
        
        # sum of weights must equal 1
        if sum != 1:
            raise serializers.ValidationError("The sum of weights must equal 1")

        return value
