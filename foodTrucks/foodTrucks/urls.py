from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.food_trucks.views import FoodTruckTemplateView, FoodTruckByCityListView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodTrucks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', FoodTruckTemplateView.as_view(), name='food_trucks'),
    url(r'^(?P<city>[\w{}.-]{2,40})/$', FoodTruckByCityListView.as_view(), name='food_trucks_city'),

    url(r'^admin/', include(admin.site.urls)),
)
