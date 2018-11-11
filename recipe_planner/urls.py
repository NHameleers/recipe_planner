from django.urls import path

from . import views

app_name = 'recipe_planner'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>', views.IngredientDetailView.as_view(), name='ingredient_detail'),
	path('ingredient_list/', views.ingredient_list, name='ingredient_list'),
	path('search_ingredient/', views.search_ingredient, name='search_ingredient'),
]