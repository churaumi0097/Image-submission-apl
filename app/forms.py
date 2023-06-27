from django import forms
from .models import Item
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DateInput(forms.DateInput):
    input_type = "date"

class CreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {
            "time" : DateInput(),
        }

