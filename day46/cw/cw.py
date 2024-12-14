import random

# 1) ცხოველების სია და რენდომის დამატება
def random_animals():
    animals = ["ლომი", "სპილო", "ვეფხვი", "ზებრა", "გველი", "კენგურუ"]
    new_animals = random.choices(animals, k=3)  # ვამატებთ 3 რენდომ ცხოველს
    print("ახალი ცხოველები:", new_animals)

# 2) საყვარელი ფილმების სია და 4 რენდომ ფილმის დამატება
def favorite_movies():
    movies = ["Inception", "Interstellar", "The Matrix", "Fight Club", "The Godfather", "Titanic"]
    random_movies = random.choices(movies, k=4)  # ვამატებთ 4 რენდომ ფილმს
    print("4 რენდომ ფილმი:", random_movies)

# 3) სახელი რანდომულ სტრინგში (For Loop გამოყენებით)
def random_name():
    name = "გიორგი"  # თქვენი სახელი
    random_string = ""
    for _ in range(5):  # ვამატებთ 5 რენდომ სიმბოლოს "<3"
        random_string += random.choice(name) + "<3"
    print("რენდომული სტრინგი:", random_string)

# 4) ხილის სია და საყვარელი ხილის დაბეჭდვა
def favorite_fruit():
    fruits = ["ვაშლი", "ბანანი", "ფორთოხალი", "მანგო"]
    favorite = random.choice(fruits)  # ვირჩევთ რენდომ ხილს
    print("თქვენი საყვარელი ხილია:", favorite)

# 5) მომხმარებლის მიერ შეყვანილი ცხოველების სია და რანდომის ბეჭდვა
def user_favorite_animals():
    animals = []
    for i in range(4):  # მომხმარებელს ვეკითხებით 4 ცხოველს
        animal = input(f"შეიყვანეთ თქვენი საყვარელი ცხოველი {i+1}: ")
        animals.append(animal)
    random_animal = random.choice(animals)  # რანდომად ვირჩევთ ერთ ცხოველს
    print("რენდომულად არჩეული ცხოველი:", random_animal)

# მთავარი ფუნქცია, რომელიც ყველა ფუნქციას გამოიძახებს
def main():
    print("\n1) ცხოველების სია და რენდომის დამატება")
    random_animals()

    print("\n2) საყვარელი ფილმების სია და 4 რენდომ ფილმის დამატება")
    favorite_movies()

    print("\n3) სახელი რანდომულ სტრინგში (For Loop გამოყენებით)")
    random_name()

    print("\n4) ხილის სია და საყვარელი ხილის დაბეჭდვა")
    favorite_fruit()

    print("\n5) მომხმარებლის მიერ შეყვანილი ცხოველების სია და რანდომის ბეჭდვა")
    user_favorite_animals()

# პროგრამის გაშვება
if __name__ == "__main__":
    main()