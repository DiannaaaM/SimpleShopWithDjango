from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts
from catalog.views import index

app_name = CatalogConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('', contacts, name='contacts'),
    path('', index, name='index'),
]