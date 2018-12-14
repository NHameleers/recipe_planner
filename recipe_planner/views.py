from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, HttpResponse, render
from django.urls import reverse
from django.views import generic

from django.conf import settings
from django.core.mail import send_mail



from collections import Counter


from .models import Recipe, Ingredient



def IndexView(request):

	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1


	template_name = 'recipe_planner/index.html'
	context = {'latest_recipe_list': Recipe.objects.order_by('last_in_menu'),
				'num_visits': num_visits}

	# control flow for adding ingredients of selected recipes to list
	recipes_to_add = request.POST.getlist('recipes_to_add')
	ingredients_to_add = Ingredient.objects.filter(recipe__name__in=recipes_to_add)
	shopping_list = Counter(ingredients_to_add)
	context.update({'ingredients_to_add': ingredients_to_add,
		'shopping_list': shopping_list.items()})

	# for the session shopping_list: work with the names, not the objects
	shopping_list_names_counter = Counter([ingredient.name for ingredient in ingredients_to_add])
	current_shopping_list_counter = Counter(request.session.get('shopping_list', {}))
	request.session['shopping_list'] = current_shopping_list_counter + shopping_list_names_counter





	return render(request, template_name, context)






class DetailView(generic.DetailView):
	model = Recipe
	template_name = 'recipe_planner/detail.html'







class IngredientDetailView(generic.DetailView):
	model = Ingredient
	template_name = 'recipe_planner/ingredient_detail.html'






def ingredient_list(request):
	# list of all recipes to use for multiselect
	all_ingredients_list = Ingredient.objects.all()
	


	# control flow for searching recipes with selected ingredients
	ingredient_names = request.POST.getlist('ingredients')

	recipes = Recipe.objects.filter(ingredients__name__in=ingredient_names).distinct().order_by('last_in_menu')

	context = {'all_ingredients_list': all_ingredients_list,
	'recipes': recipes}


	# control flow for adding ingredients of selected recipes to list
	recipes_to_add = request.POST.getlist('recipes_to_add')
	ingredients_to_add = Ingredient.objects.filter(recipe__name__in=recipes_to_add)
	shopping_list = Counter(ingredients_to_add)
	context.update({'ingredients_to_add': ingredients_to_add,
		'shopping_list': shopping_list.items()})

	# for the session shopping_list: work with the names, not the objects
	shopping_list_names = Counter([ingredient.name for ingredient in ingredients_to_add])
	request.session['shopping_list'] = Counter(request.session.get('shopping_list', {})) + shopping_list_names



	return render(request, 'recipe_planner/ingredient_list.html', context)



def shopping_list(request):
	shopping_list = request.session.get('shopping_list', {})

	context = {'shopping_list': sorted(shopping_list.items())}


	# get most recent values of ingredients
	for ingredient in shopping_list.keys():
		new_amount = shopping_list[ingredient]
		shopping_list[ingredient] = int(new_amount)

	# control flow for sending shopping list to email
	email_address = request.POST.get('email_address')

	email_message = ''' Shopping list:\n'''

	for ingredient, amount in shopping_list.items():
		email_message += '{}x  {}\n'.format(amount, ingredient)

	# for ingr, amount in shopping_list.items():
	# 	recipes_with_ingredient = [r.name for r in Ingredient.objects.get(name=ingr).recipe_set.all() if r.name in recipes_to_add]
	# 	email_message += '{}x  {} ({})\n'.format(amount, ingr, ','.join(recipes_with_ingredient))
	# email_message += '\nSelected recipes:\n'
	# for rec in recipes_to_add:
	# 	email_message += '{}\n'.format(rec.title())

	context.update({'email_message': email_message})
	
	send_mail(
	    'Shopping list',
	    email_message,
	    settings.EMAIL_HOST_USER,
	    [email_address],
	    fail_silently=False,
	)

	return render(request, 'recipe_planner/shopping_list.html', context)




	# # control flow for sending shopping list to email
	# email_address = request.POST.get('email_address')

	# email_message = ''' Shopping list:\n'''
	# for ingr, amount in shopping_list.items():
	# 	recipes_with_ingredient = [r.name for r in Ingredient.objects.get(name=ingr).recipe_set.all() if r.name in recipes_to_add]
	# 	email_message += '{}x  {} ({})\n'.format(amount, ingr, ','.join(recipes_with_ingredient))
	# email_message += '\nSelected recipes:\n'
	# for rec in recipes_to_add:
	# 	email_message += '{}\n'.format(rec.title())

	# context.update({'email_message': email_message})

	# send_mail(
	#     'Shopping list',
	#     email_message,
	#     settings.EMAIL_HOST_USER,
	#     [email_address],
	#     fail_silently=False,
	# )