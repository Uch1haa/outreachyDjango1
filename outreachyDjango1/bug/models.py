from django.db import models


# Create your models here.
class Bug(models.Model):
    BUG_TYPES = (
        ('error', 'Error'),
        ('new_feature', 'New Feature'),
    )

    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )

    description = models.TextField()
    bug_type = models.CharField(max_length=20, choices=BUG_TYPES)
    report_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
