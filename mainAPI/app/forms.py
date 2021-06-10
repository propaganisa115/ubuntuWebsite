from django.forms import ModelForm, Form
from django.forms import DateField, CharField, ChoiceField, TextInput
from django.forms import ModelForm
from django import forms
from .models import Sekolah


class SekolahSearch(ModelForm):
    sekolah_domain = CharField(required=False)
    class Meta:
        model = Sekolah
        fields = ('sekolah_domain',)

