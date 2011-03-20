#-*- coding: utf-8 -*-

from django import forms
from agenda.models import ItemAgenda

class FormItemAgenda(forms.ModelForm):
    data = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%y', '%d/%m/%Y']
    )
    class Meta:
        model = ItemAgenda
        fields = ('titulo', 'hora', 'descricao')
