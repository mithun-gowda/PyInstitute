from django import forms

from .models import StaffDB
from django.contrib.auth.hashers import make_password

class StaffForm(forms.ModelForm):
    Re_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=StaffDB
        fields=['username','first_name','last_name','email','mobile','gender','password','Re_password']

    def clean(self):
        password=self.cleaned_data['password']
        repassword=self.cleaned_data['Re_password']
        if password != repassword:
           raise forms.ValidationError('Repassword should be same as Password')
        

    def save(self,commit=True):
        data=super().save(commit=False)
        print(data.password)
        data.password=make_password(data.password)
        print(data.password)
        if commit:
            data.save()
        return data