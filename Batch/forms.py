from django import forms

from .models import Trainer,Subject,BatchDB

class SubjectForm(forms.ModelForm):
     class Meta:
        model=Subject
        fields='__all__'


class TrainerForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields='__all__'
        widgets={'Date_of_join':forms.DateInput(attrs={'type':'date'})}


class BatchForm(forms.ModelForm):
    class Meta:
        model=BatchDB
        fields='__all__'
        widgets={'Time':forms.TimeInput(attrs={'type':'time'})}