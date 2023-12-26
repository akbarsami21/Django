from django import forms
from django.core import validators
class TeacherForm(forms.Form):
    name=forms.CharField(label="Enter First Name",label_suffix=" ")
    email=forms.EmailField(initial='mdsami6351@gmail.com',disabled=True)
    password  =forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)
    checkbox=forms.CharField(widget=forms.CheckboxInput)
    textarea=forms.ChoiceField(widget=forms.Textarea)
    # hiddenfiled=forms.CharField(widget=forms.HiddenInput)
    file=forms.CharField(widget=forms.FileInput)
    dob=forms.DateInput

    def clean(self):
        cleaned_data=super().clean()
        rightpassword=self.cleaned_data['password']
        wrongpassword=self.cleaned_data['repassword']

        if rightpassword != wrongpassword:
            raise forms.ValidationError('password does not match')

