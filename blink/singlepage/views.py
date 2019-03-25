from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import strategy,philosophy,services
# Create your views here.

class strategy_view(TemplateView):
    template_name = "strategy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object']=get_object_or_404(strategy,pk=1)
        return context

class philosophy_view(TemplateView):
    template_name = "philosophy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object']=get_object_or_404(philosophy,pk=1)
        return context


class services_view(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj=get_object_or_404(services,pk=1)
        context['object']=obj
        all_services=obj.services.split("%*")
        context['the_services']=all_services
        services_no = len(all_services)+1
        numbers = []
        for x in range (1,services_no):
            numbers.append(str(x))

        zipped_list=zip(all_services,numbers)
        context["zip"] = zipped_list

        return context

class contact_view(TemplateView):
    template_name = "contact.html"