from django.urls import path
from .api import SekolahCreateApi, SekolahApi, SekolahUpdateApi, SekolahDeleteApi, SekolahAuthApi


urlpatterns = [
	#path('create', SekolahCreateApi.as_view()),
	#path('', SekolahApi.as_view()),
	#path('<int:pk>', SekolahUpdateApi.as_view()),
	path('auth', SekolahAuthApi.as_view()),
	#path('delete/<int:pk>', SekolahDeleteApi.as_view()),
]