from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.food_trucks.views import FoodTruckTemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodTrucks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', FoodTruckTemplateView.as_view(), name='food_trucks'),

    url(r'^admin/', include(admin.site.urls)),
)
