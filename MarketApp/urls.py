from django.conf.urls import url

from MarketApp import views

urlpatterns=[
    url(r'^market/',views.market,name='market')
]