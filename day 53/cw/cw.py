# Creating a dictionary with favorite foods
favorite_foods = {
    "Fruits": ["Apple", "Banana", "Mango", "Strawberry"],
    "Vegetables": ["Carrot", "Broccoli", "Spinach"],
    "Snacks": ["Chips", "Popcorn", "Chocolate"],
    "Main Dishes": ["Pizza", "Sushi", "Pasta"],
    "Desserts": ["Ice Cream", "Cheesecake", "Brownie"]
}

# Printing the dictionary
for category, items in favorite_foods.items():
    print(f"My favorite {category.lower()} are: {', '.join(items)}.")
