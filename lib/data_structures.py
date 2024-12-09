spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
     return [food["name"] for food in spicy_foods]
 

def get_spiciest_foods(spicy_foods):
     return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    # Optionally return None if no match is found
     return None


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    # Print each spiciest food using the desired format
    for food in spiciest_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    # Calculate the total heat level
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    # Calculate the average and return it as an integer
    average_heat_level = total_heat_level // len(spicy_foods)
    return average_heat_level


def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
    # Return the updated list
     return spicy_foods
