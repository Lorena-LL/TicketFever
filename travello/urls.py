from django.urls import path


from . import views


urlpatterns = [
	path('', views.index, name = 'home'),
	path('search/item', views.displayItem, name = 'displayItem'),
	path('search', views.search, name = 'search')



]