from django import forms

class PriorityForm(forms.Form):
    selectedPriority = forms.CharField(widget=forms.MultipleHiddenInput)
    priority = forms.ChoiceField(choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])

class StatusForm(forms.Form):
    selectedStatus = forms.CharField(widget=forms.MultipleHiddenInput)
    status = forms.ChoiceField( choices=[
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('escalated', 'Escalated'),
    ])