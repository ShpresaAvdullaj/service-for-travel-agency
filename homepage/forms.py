from django import forms
from administrator.models import FilterDate


class FilterDateForm(forms.ModelForm):
    class Meta:
        model = FilterDate
        fields = "__all__"
        