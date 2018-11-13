from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, HttpResponse, render
from django.urls import reverse
from django.views import generic


from .models import Recipe, Ingredient



class IndexView(generic.ListView):
	template_name = 'recipe_planner/index.html'
	context_object_name = 'latest_recipe_list'

	def get_queryset(self):
		return Recipe.objects.order_by('last_in_menu')



class DetailView(generic.DetailView):
	model = Recipe
	template_name = 'recipe_planner/detail.html'



class IngredientDetailView(generic.DetailView):
	model = Ingredient
	template_name = 'recipe_planner/ingredient_detail.html'



def ingredient_list(request):
	all_ingredients_list = Ingredient.objects.all()
	
	# this works with the names instead of the ideas. Not the greatest solution,
	# as it could run into trouble when names get duplicates. I was able to pass
	# the id through from the template file (option --> value), but this is not
	# working anymore.
	ingredient_names = request.POST.getlist('ingredients')

	recipes = Recipe.objects.filter(ingredients__name__in=ingredient_names).distinct().order_by('last_in_menu')

	context = {'all_ingredients_list': all_ingredients_list,
	'recipes': recipes}

	return render(request, 'recipe_planner/ingredient_list.html', context)



