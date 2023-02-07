from django import forms


def Minchar(name):
    if len(name)<4:
        raise forms.ValidationError('name should be minimum four char')

def Maxchar(name):
    if len(name)>20:
        raise forms.ValidationError('name should be maximum 20  char')
