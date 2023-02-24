import json as json
import os



def new_Recipe(id, name, ingredients, method, link):
    #name = input("Name of Recipe")
    #ingredients = [input("ingredients:").split("/")]
    #method = input("method")
    #link = input("link")

    #recipe_Dict = {"name":name,"ingredients":ingredients,"method":method,"link":link}
    recipe_Dict = {
        "id":1,
        "name":"Easy risotto with bacon & peas", 
        "ingredients":[
            ("Onion",1,"each"),
            ("Olive Oil",2,"tbsp"),
            ("Bacon",6,"each"),
            ("Risotto Rice",300,"g"),
            ("Vegetable Stock",1000,"ml"),
            ("Frozen Peas", 100,"g")],
        "method": "STEP 1\nFinely chop 1 onion. Heat 2 tbsp olive oil and a knob of butter in a pan, add the onions and fry until lightly browned (about 7 minutes).\n\nSTEP 2\nAdd 6 chopped rashers streaky bacon and fry for a further 5 minutes, until it starts to crisp.\n\nSTEP 3\nAdd 300g risotto rice and 1l hot vegetable stock, and bring to the boil. Stir well, then reduce the heat and cook, covered, for 15-20 minutes until the rice is almost tender.\n\nSTEP 4\nStir in 100g frozen peas, add a little salt and pepper and cook for a further 3 minutes, until the peas are cooked.\n\nSTEP 5\nServe sprinkled with freshly grated parmesan and freshly ground black pepper.",
        "link":"https://www.bbcgoodfood.com/recipes/easy-risotto-bacon-peas#commentsFeed"       
        } 
    filename = "Meals/{} - {}.json".format(str(recipe_Dict["id"]), recipe_Dict["name"])

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(recipe_Dict, indent=4))

def read_Recipe(id):
    for file in os.listdir("Meals/"):
        if file.startswith(str(id)):
            filepath = "Meals/"+file
    
    with open(filepath, 'r') as openfile:
        json_Obj = json.load(openfile)
        
    print(json_Obj)
