from django import forms

class PatientForm(forms.Form):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    EmailId = forms.CharField()
    MobileNo = forms.IntegerField()
    PatientId = forms.IntegerField()
