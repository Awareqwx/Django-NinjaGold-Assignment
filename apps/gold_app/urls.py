from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.index),
    url(r"^process_money/(?P<name>\w+)/(?P<goldmin>[0-9\-]+)/(?P<goldmax>\d+)", views.process),
    url(r"^reset/$", views.reset)
]	