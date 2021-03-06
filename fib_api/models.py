from __future__ import unicode_literals

from django.db import models


class FibonacciResults(models.Model):

    number = models.IntegerField()
    result = models.CharField(max_length=4000)

    class Meta:
        db_table = 'fibonacci_results'

    def __unicode__(self):
        return self.number
