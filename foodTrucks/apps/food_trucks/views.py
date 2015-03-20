from django.shortcuts import render
from django.views.generic import TemplateView


class FoodTruckTemplateView(TemplateView):
    template_name = 'food_trucks_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(FoodTruckTemplateView, self).dispatch(request, *args, **kwargs)