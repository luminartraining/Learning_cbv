from django import http
from django import forms
from django.shortcuts import render

# Create your views here.
from django.views import generic

from MyCbvApp import models


class StudentForm(forms.ModelForm):

    class Meta:
        model = models.Student
        fields='__all__'




