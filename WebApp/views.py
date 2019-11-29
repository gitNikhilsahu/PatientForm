from django.shortcuts import render
from django.http import HttpResponseRedirect

from WebApp import forms

def PatientView(request):
    if request.method == 'POST':
        form = forms.PatientForm(request.POST)
        if form.is_valid():
            print("Validations are Success Folks...!!")
            print(form.cleaned_data['FirstName'])
            print(form.cleaned_data['LastName'])
            print(form.cleaned_data['EmailId'])
            print(form.cleaned_data['MobileNo'])
            print(form.cleaned_data['PatientId'])

            return HttpResponseRedirect('/Thanks')
    else:
        form = forms.PatientForm()
    return render(request, 'WebApp/Patient.html', {'form': form})

def ThankView(request):
    return render(request, 'WebApp/Thanks.html')