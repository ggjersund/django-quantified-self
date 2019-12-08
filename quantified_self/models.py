from django.db import models
from quantified_self.mixins import DatapointMixin, RatingMixin, IntervalMixin, IntCountMixin


class IntervalEvent(DatapointMixin, IntervalMixin, RatingMixin):
    """
    Interval data entry, preferably also provide a label
    """
    title = models.CharField(max_length=50)

    def __str__(self):
        return '%s (%s)' % (self.title, self.pk)

    class Meta:
        ordering = ["-start"]
        verbose_name = "interval event"
        verbose_name_plural = "interval events"


class IntCountEvent(DatapointMixin, IntCountMixin, RatingMixin):
    """
    Count data entry, preferably also provide a label
    """
    title = models.CharField(max_length=50)

    def __str__(self):
        return '%s (%s)' % (self.title, self.pk)

    class Meta:
        ordering = ["-datetime"]
        verbose_name = "integer count event"
        verbose_name_plural = "integer count events"
