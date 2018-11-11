from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, HttpResponse, render
from django.urls import reverse
from django.views import generic


from .models import Recipe, Ingredient




# def index(request):
# 	latest_recipe_list = Recipe.objects.all()
# 	context = {'latest_recipe_list': latest_recipe_list}
# 	return render(request, 'recipe_planner/index.html', context)

# 	# There’s also a get_list_or_404() function, which works just as
# 	# get_object_or_404() – except using filter() instead of get().
# 	# It raises Http404 if the list is empty.

class IndexView(generic.ListView):
	template_name = 'recipe_planner/index.html'
	context_object_name = 'latest_recipe_list'

	def get_queryset(self):
		return Recipe.objects.order_by('-pk')


# def detail(request, recipe_id):
# 	recipe = get_object_or_404(Recipe, pk=recipe_id)
# 	return render(request, 'recipe_planner/detail.html', {'recipe': recipe})


class DetailView(generic.DetailView):
	model = Recipe
	template_name = 'recipe_planner/detail.html'


# def ingredient_detail(request, ingredient_id):
# 	ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
# 	context = {
# 		'ingredient': ingredient
# 	}
# 	return render(request, 'recipe_planner/ingredient_detail.html', context)

class IngredientDetailView(generic.DetailView):
	model = Ingredient
	template_name = 'recipe_planner/ingredient_detail.html'

def ingredient_list(request):
	all_ingredients_list = Ingredient.objects.all()
	context = {'all_ingredients_list': all_ingredients_list}

	results = request.POST.getlist('ingredient')

	if results and request.method == 'POST':
		context.update({'results': results})

	return render(request, 'recipe_planner/ingredient_list.html', context)


def search_ingredient(request):
    query = request.POST.get('search_ingredient', None)
    context = {}

    if query and request.method == 'POST':
        results = Ingredient.objects.filter(name=query)
        context.update({'results': results})

    return render(request, 'recipe_planner/search_ingredient.html', context)