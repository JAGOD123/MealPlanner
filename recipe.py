import json as json
import os


def easy_new_Recipe():
    name = input("Name of Recipe")
    ingredients = [input("ingredients:").split("/")]
    method = input("method")
    link = input("link")
    new_Recipe("id, name, ingredients, method, link=None")


def new_Recipe(name, ingredients, method, link=None):
    '''
    Need to check if the file already exists, use name remove white space
    '''
    recipe_Dict = {
        "id":set_Recipe_ID(),
        "name":name,
        "ingredients":ingredients,
        "method":method,
        "link":link
        }

    filename = "Meals/{} - {}.json".format(str(recipe_Dict["id"]), recipe_Dict["name"])

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(recipe_Dict, indent=4))

def set_Recipe_ID():
    # go through folder, get largest num add one
    id = 1
    for file in os.listdir("Meals/"):
        if file.startswith(str(id)):
            id += 1
        else:
            return id


def ingredients_reader(txt):
    return [tuple(item.split(",")) for item in txt.split("/")]



def read_Recipe(id):
    for file in os.listdir("Meals/"):
        if file.startswith(str(id)):
            filepath = "Meals/"+file
    
    with open(filepath, 'r') as openfile:
        json_Obj = json.load(openfile)
        
    print(json_Obj)
