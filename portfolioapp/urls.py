from django.urls import path

from . import views

app_name = 'portfolio_app'

urlpatterns = [
           path('', views.homepage, name='home'),
           path('about/', views.about, name='about'),
           path('resume/', views.resume, name='resume'),
           path('research/', views.research, name='research'),
           path('publications/', views.publication, name='publication'),
           path('presentation/', views.presentation, name='presentation'),
           path('resources/', views.resource, name='resources'),
           path('gallery/', views.gallery, name='gallery'),
]