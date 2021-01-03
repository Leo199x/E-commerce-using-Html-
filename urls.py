from django.urls import path
from . 	import views

urlpatterns = [
    path('', views.home),
    path('Language/',views.Language),
    path('Snippet/',views.Snippet),
]