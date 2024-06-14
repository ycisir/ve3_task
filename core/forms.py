from django import forms
# from .models import UploadedCSV

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField()
