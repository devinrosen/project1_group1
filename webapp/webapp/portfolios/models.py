import uuid
from django.db import models


class Portfolio(models.Model):
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    holdings = models.JSONField()
