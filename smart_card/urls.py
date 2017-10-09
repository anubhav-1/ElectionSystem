from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register$', views.register, name= 'register'),
    url(r'^get_districts/$', views.get_districts, name = 'get_districts'),
    url(r'^get_tehsils/$', views.get_tehsils, name = 'get_tehsils'),
    url(r'^get_gram_panchayats/$', views.get_gram_panchayats, name = 'get_gram_panchayats'),
    url(r'^details$', views.details, name= 'details'),
    url(r'^do_register/$', views.do_register, name='do_register'),
    url(r'^view_details/$',views.view_details, name='view_details')
]
