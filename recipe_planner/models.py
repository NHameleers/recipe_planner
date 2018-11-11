from django.db import models


class Recipe(models.Model):
	'A recipe!'

	# def __init__(self, recipe_id, name, description):
	# 	self.recipe_id
	# 	self.name = name
	# 	self.description

	name = models.CharField(max_length=255)
	# description = models.CharField(max_length=3000)
	# last_in_menu = models.DateTimeField('Last time this recipe was on menu')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)



class Ingredient(models.Model):
	'An ingredient!'

	# def __init__(self, recipe_id, name):
	# 	self.recipe_id
	# 	self.name = name

	name = models.CharField(max_length=255)
	recipes = models.ManyToManyField(Recipe)
	# ah_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

# class Recipe_ingredient(models.Model):
# 	'An ingredient, its characteristics, and the recipe it belongs to'

# 	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
# 	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
# 	quantity = models.DecimalField(max_digits=7, decimal_places=2, default=0)

# 	def __str__(self):
# 		return f"{ingredient.name}: {quantity}"


