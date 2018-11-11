from django.db import models




class Ingredient(models.Model):
	'An ingredient!'

	# def __init__(self, recipe_id, name):
	# 	self.recipe_id
	# 	self.name = name

	name = models.CharField(max_length=255)
	# ah_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)




class Recipe(models.Model):
	'A recipe!'

	# def __init__(self, recipe_id, name, description):
	# 	self.recipe_id
	# 	self.name = name
	# 	self.description

	name = models.CharField(max_length=255)
	ingredients = models.ManyToManyField(Ingredient)
	last_in_menu = models.DateField('Last time this recipe was on menu', blank=True)
	# description = models.CharField(max_length=3000)


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


