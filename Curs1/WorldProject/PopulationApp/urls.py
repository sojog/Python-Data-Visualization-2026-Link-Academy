from django.urls import path
from .views import choose_countries_view
from .views import all_countries_view

urlpatterns = [

	path("all", all_countries_view),
	path("choose", choose_countries_view),
]
