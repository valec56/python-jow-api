from src import Jow

# Perform a search for recipes containing the word "poulet"
recipes = Jow.search("poulet", 5)

# Loop through each recipe in the results and print its attributes
for recipe in recipes:
    print(f"ID: {recipe.id}")
    print(f"Name: {recipe.name}")
    print(f"URL: {recipe.url}")
    print(f"Description: {recipe.description}")
    print(f"Preparation time: {recipe.preparation_time}")
    print(f"Cooking time: {recipe.cookingTime}")
    print(f"Preparation extra time per cover: {recipe.preparation_extra_time_per_cover}")
    print(f"Covers count: {recipe.covers_count}")
    print("Ingredients:")
    for ingredient in recipe.ingredients:
        print(f"\t{ingredient.name}: {ingredient.quantity} {ingredient.unit}")
        if ingredient.is_optional:
            print("\t(optional)")
    print()
