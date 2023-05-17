from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView
from app.forms import *


class Context_Form_View(TemplateView):
    template_name='Context_Form_View.html'
    
    def get_context_data(self, **kwargs):
        ECO=super().get_context_data(**kwargs)
        ECO['SFO']=StudentForm()
        return ECO
    
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
        return HttpResponse("data sucessfully inserted:")



