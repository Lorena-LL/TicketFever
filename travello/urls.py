from django.urls import path


from . import views


urlpatterns = [
	path('', views.index, name = 'home'),
	path('search/item', views.display_item, name = 'displayItem'),
	path('search', views.search, name = 'search'),
	path('reserve', views.check_resrevations, name = 'reserve'),
	path('user-reservations', views.user_reservations, name = 'user_reservations'),
	path('user-messages', views.user_messages, name = 'user_messages')

]