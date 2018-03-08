from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^logout$',views.logout),
    url(r'^add$', views.add),
    url(r'^create$',views.create),
    url(r'^event/(?P<id>\d+)/$',views.event),
    url(r'^delete/(?P<id>\d+)/',views.delete),
    url(r'^remove/(?P<id>\d+)/$',views.remove),
    url(r'^adder/(?P<id>\d+)/$',views.adder),
]
