from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import urllib
import json

from pyyelp.pyyelp import Yelp


class FoodTruckTemplateView(TemplateView):
    template_name = 'food_trucks_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(FoodTruckTemplateView, self).dispatch(request, *args, **kwargs)

    @staticmethod
    def associate_yelp(input_data):
        output_data = input_data

        for truck in output_data:
            if 'applicant' in truck:
                term = truck['applicant']
            else:
                term = ''
            if 'location' in truck and 'latitude' in truck['location'] and 'longitude' in truck['location']:
                location = {
                    'lat': truck['location']['latitude'],
                    'lon': truck['location']['longitude'],
                }
            else:
                location = {}
            if term and location and 'lat' in location and 'lon' in location:
                try:
                    yelp = Yelp()
                    yelp_response = yelp.search(term=term, location='San Francisco', latitude=location['lat'], longitude=location['lon'], search_limit=1)
                    truck['yelp'] = yelp_response
                except:
                    pass
            else:
                try:
                    yelp = Yelp()
                    yelp_response = yelp.search(term=term, location='San Francisco', search_limit=1)
                    truck['yelp'] = yelp_response
                except:
                    pass

        return output_data

    def get_context_data(self, **kwargs):
        response_data = urllib.urlopen('https://data.sfgov.org/resource/rqzj-sfat.json?$$app_token=2j4ggSjUP1A7WCkhKSnPrPML6&status=APPROVED&$limit=20')
        json_data = json.loads(response_data.read())
        context = super(FoodTruckTemplateView, self).get_context_data(**kwargs)
        context['food_truck_data'] = self.associate_yelp(json_data)
        return context


class FoodTruckByCityListView(TemplateView):
    template_name = 'food_trucks_list.html'

    def dispatch(self, request, *args, **kwargs):
        print(kwargs['city'])
        return super(FoodTruckByCityListView, self).dispatch(request, *args, **kwargs)