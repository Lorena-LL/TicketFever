from django.urls import path


from . import views


urlpatterns = [
	path('', views.index, name = 'home'),
	path('search/item', views.display_item, name = 'displayItem'),
	path('search', views.search, name = 'search')



]