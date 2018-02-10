# import all necessary modules
from flask import Flask
from recipes import *


# file to load recipes from
file = 'recipes.json'


""" 
set up Flask in debugging mode
nothing fancy needed here
"""
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'salaisuus'


"""
API endpoints for diffirent resources and states
"""
# list all recipes
@app.route('/recipes')
def list_recipes():
    return toJSON(recipes)

# show recipes from search results
# eg. http://hostname/search/chicken
@app.route('/search/<keyword>')
def search_recipes(keyword):
    results = searchRecipes(keyword)
    if len(results) > 0:
    	return toJSON(results)
    else:
    	return "No results"


# fire up the API
if __name__ == '__main__':
    loadRecipes(file) # load the recipes first
    app.run() # run the flask app
