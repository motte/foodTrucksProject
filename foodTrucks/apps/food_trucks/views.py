from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class FoodTruckTemplateView(TemplateView):
    template_name = 'food_trucks_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(FoodTruckTemplateView, self).dispatch(request, *args, **kwargs)


class FoodTruckByCityListView(TemplateView):
    template_name = 'food_trucks_list.html'

    def dispatch(self, request, *args, **kwargs):
        print(kwargs['city'])
        return super(FoodTruckByCityListView, self).dispatch(request, *args, **kwargs)