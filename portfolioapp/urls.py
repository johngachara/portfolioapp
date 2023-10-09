from django.urls import path
from . import views
urlpatterns = [
path('',views.index, name = 'home'  ),
path('aboutpage',views.about,name = 'about'),
path('projectspage',views.projects,name = 'projects'),
path('contactspage',views.contact,name = 'contact')
]