example_file = open("example.txt", "r")
file_contents= example_file.read()
example_file.close()
print(file_contents)

ingredient_costs = {
    "flour": 2.5,  # per kg
    "sugar": 1.5,  # per kg
    "butter": 3.0,  # per kg
    "water": 0.01,  # per liter
    "salt": 1,  # per kg
    "yeast": 0.05,  # per oz
    "eggs": 0.2,  # per egg
    "milk": 0.8,  # per liter
    "chocolate_chips": 4.0,  # per kg
    "vanilla_extract": 20,  # per liter
    "baking_powder": 0.02,  # per gram
    "baking_soda": 0.015,  # per gram
    "cinnamon": 0.03,  # per gram
    "raisins": 5.0  # per kg
}
import json

ingredients_cost_file = open("ingredient_costs.json","w")
ingredients_cost_file.write(json.dumps(ingredient_costs))
ingredients_cost_file.close()

##convert json to a csv
## loop over the ingredient cost
    ##make ingredient amount become a string

data_csv = open("data.csv", "a")
for ingredient_name, amount in ingredient_costs.items():
    ingrediant_string = "\n" + ingredient_name + "," + str(amount) 
    data_csv.write(ingrediant_string)

data_csv.close()