import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def generate_uuid():
    return uuid.uuid4

class DatapointMixin(models.Model):
    """
    Each data entry should inherit this abstract class
    """
    uuid = models.UUIDField(unique=True, default=generate_uuid())
    label = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        abstract = True


class RatingMixin(models.Model):
    """
    Add rating functionality to any data entry
    """
    score = models.SmallIntegerField(validators=[
        MinValueValidator(0, "Value has to be greater or equal to zero."),
        MaxValueValidator(10, "Value has to be less or equal to 10.")
    ], null=True, blank=True)

    class Meta:
        abstract = True


class IntervalMixin(models.Model):
    """
    Used for interval data entries, e.g. events with durations
    """
    start = models.DateTimeField()
    stop = models.DateTimeField()

    class Meta:
        abstract = True


class IntCountMixin(models.Model):
    """
    Used to keep track of Integer counts, e.g. beverages
    consumed or available items of a given sort.
    """
    datetime = models.DateTimeField()
    value = models.IntegerField()

    class Meta:
        abstract = True
