from django import forms
from .models import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['leave_type', 'date', 'team_email', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


