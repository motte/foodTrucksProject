from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import urllib
import json


class FoodTruckTemplateView(TemplateView):
    template_name = 'food_trucks_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(FoodTruckTemplateView, self).dispatch(request, *args, **kwargs)

    @staticmethod
    def associate_yelp(input_data):
        output_data = input_data
        for truck in input_data:
            print truck
        return output_data

    def get_context_data(self, **kwargs):
        response_data = urllib.urlopen('https://data.sfgov.org/resource/rqzj-sfat.json')
        json_data = json.loads(response_data.read())
        context = super(FoodTruckTemplateView, self).get_context_data(**kwargs)
        context['food_truck_data'] = self.associate_yelp(json_data)
        return context


class FoodTruckByCityListView(TemplateView):
    template_name = 'food_trucks_list.html'

    def dispatch(self, request, *args, **kwargs):
        print(kwargs['city'])
        return super(FoodTruckByCityListView, self).dispatch(request, *args, **kwargs)