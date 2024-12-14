import random

# 1. ფუნქცია ცხოველების სიით და რენდომ ცხოველების დამატება
def random_animals():
    animals = ["Dog", "Cat", "Elephant", "Tiger", "Lion", "Giraffe", "Zebra", "Bear"]
    random_list = random.choices(animals, k=5)  # 5 რენდომ ცხოველი
    print("Random animals:", random_list)

# 2. ფუნქცია ფილმების სიით და რენდომ ფილმების დამატება
def random_movies():
    movies = ["Inception", "The Matrix", "Interstellar", "Titanic", "Avatar", "The Godfather"]
    random_list = random.choices(movies, k=4)  # 4 რენდომ ფილმი
    print("Random movies:", random_list)

# 3. თქვენი სახელი რენდომად დამატებული სტრინგში
def random_name_string(name):
    result = ""
    for _ in range(len(name)):
        result += random.choice(name)
    print("Randomized name:", result)

# 4. ხილის სია და საყვარელი ხილის ამორჩევა
def favorite_fruit():
    fruits = ["Apple", "Banana", "Cherry", "Orange"]
    favorite = random.choice(fruits)
    print("Your favorite fruit is:", favorite)

# 5. მომხმარებლის საყვარელი ცხოველების მიღება და რენდომ ამორჩევა
def user_favorite_animals():
    user_animals = []
    for i in range(4):
        animal = input(f"Enter your favorite animal #{i + 1}: ")
        user_animals.append(animal)
    random_animal = random.choice(user_animals)
    print("Random favorite animal:", random_animal)

# ამ ფუნქციების გამოყენება
random_animals()
random_movies()
random_name_string("YourName")
favorite_fruit()
user_favorite_animals()
