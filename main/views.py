from django.shortcuts import render, redirect
from django.views import generic

from .forms import ContactForm
from .models import *


class Index(generic.TemplateView):
    template_name = 'index.html'
    model = Info.objects.all()[0]
    context_object_name = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.objects.all()[0]
        context['skills'] = Skills.objects.all()[:5]
        context['portfolio'] = Portfolio.objects.all()[:6]
        context['contact'] = ContactForm()
        context['happies'] = HappyClients.objects.all()
        context['contactinfo'] = ContactInfo.objects.all()[0]
        context['works'] = WorkExp.objects.all()[:3]
        context['education'] = Education.objects.all()[:3]
        context['services'] = Services.objects.all()[:3]
        return context


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')

