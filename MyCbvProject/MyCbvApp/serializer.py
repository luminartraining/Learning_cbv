from django import http
from django import forms
from django.shortcuts import render

# Create your views here.
from django.views import generic

from MyCbvApp import models
from rest_framework import routers, serializers, viewsets

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields ='__all__'




