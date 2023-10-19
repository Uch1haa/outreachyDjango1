from django import forms
from .models import Bug  # Import your Bug model


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['description', 'bug_type', 'report_date', 'status']
