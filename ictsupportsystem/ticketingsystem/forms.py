from django import forms

class PriorityForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    priority = forms.ChoiceField(choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])

class StatusForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    status = forms.ChoiceField( choices=[
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('escalated', 'Escalated'),
    ])

#modify this 
class AgentForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    agents = forms.ChoiceField( choices=[
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('escalated', 'Escalated'),
    ])