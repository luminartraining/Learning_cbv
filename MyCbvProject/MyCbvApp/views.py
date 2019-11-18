from django import http
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

from MyCbvApp import models, forms, serializer


class StudentList(generic.TemplateView):
    template_name = 'index.html'
    model_name = models.Student
    form_class = forms.StudentForm

    def get_queryset(self):
        return self.model_name.objects.all()

    def get(self, request, *args, **kwargs):
        context ={}
        context['student'] = self.get_queryset()
        context['form'] =self.form_class

        return  render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save()
        else:
            return JsonResponse({'errors': form.errors.as_json()})

        ser = serializer.StudentSerializer(data)
        return JsonResponse({"message": "save", 'data': ser.data})


class StudentDelete(generic.TemplateView):
    model_name = models.Student

    def get_queryset(self):
        return self.model_name.objects.filter(id=self.kwargs.get('pk'))

    def post(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return JsonResponse({"message": "deleted", 'status': 200})