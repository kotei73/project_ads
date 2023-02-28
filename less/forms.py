from django import forms

class UserForm(forms.Form):
    choose = ((1, 'yes'), (2, 'no'))
    name = forms.CharField(required=True, label='Имя', initial='ФИО')
    age = forms.IntegerField()

