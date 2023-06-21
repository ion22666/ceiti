#-*- coding:utf-8 -*-
from . import models
from django import forms

class ApartamentForm(forms.ModelForm):

    class Meta:
        model = models.Apartament
        fields = "__all__"

class AgentForm(forms.ModelForm):

    class Meta:
        model = models.Agent
        fields = "__all__"