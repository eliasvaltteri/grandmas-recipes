# imports
from flask import jsonify
import json


# define a class for a recipe
class Recipe(object):

	# constructor for a recipe model
	def __init__(self, name, ingredients, instructions):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions

	# return a dictionary so we can jsonify it later
	def serialize(self):
		return {
		'name': self.name,
		'ingredients': self.ingredients,
		'instructions': self.instructions
		}


# declare a global variable for the recipes
recipes = []


# initialize function load recipes from a json file
def loadRecipes(file):

	# try to load from file
	try:
		with open(file) as recipes_file:	
			json_recipes = json.load(recipes_file)

			# create a new instance of a recipe object
			# and give the constructor corresponding arguments
			for i in json_recipes:
				new_recipe = Recipe(i["name"], i["ingredients"], i["instructions"])
				recipes.append(new_recipe)

	# catch error in case file can't be read
	except ValueError:
		print('Decoding JSON failed')


# function to search for recipes
def searchRecipes(keyword):

	# init array for results
	results = []

	# loop through loaded recipes and
	# check for matches in ingredients
	for recipe in recipes:
		for ingredient in recipe:
			if keyword.lower() in ingredient.lower():
				results.append(recipe)
				return results

# simple function to produce json from a dictionary
def toJSON(dict):
	return jsonify([i.serialize() for i in dict])