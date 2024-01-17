from django import forms
from my_app. models import About

class AboutForm(forms.ModelForm):
  mobile_number = forms.CharField(label='Password', widget=forms.PasswordInput)
  class Meta:
    model = About
    fields = '__all__'
    # fields = ['ids','first_name','last_name','roll_number','mobile_number','image']

