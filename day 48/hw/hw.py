import random
import string

# 1. ფუნქცია, რომელიც სიის ელემენტებს დაამატებს შემთხვევითი რიცხვები 1-დან 50-მდე.
def add_random_numbers_to_list(lst, count):
    for _ in range(count):
        lst.append(random.randint(1, 50))
    return lst

# 2. ფუნქცია, რომელიც სიის ელემენტებიდან შემთხვევით აირჩევს ერთ ცხოველს.
def pick_favorite_animal(animals):
    if not animals:
        print("ცხოველების სია ცარიელია.")
        return
    favorite = random.choice(animals)
    print(f"თქვენი საყვარელი ცხოველი არის: {favorite}")

# 3. ფუნქცია, რომელიც სტრინგში დაამატებს შემთხვევით სიმბოლოებს.
def add_random_symbols(string_input):
    symbols = random.choices(['#', '*', '%'], k=random.randint(1, 10))
    return string_input + ''.join(symbols)

# 4. ფუნქცია, რომელიც სიის ყველა ელემენტს გადაატრიალებს.
def reverse_list_elements(lst):
    reversed_elements = [str(item)[::-1] for item in lst]
    print(f"გადატრიალებული ელემენტები: {reversed_elements}")
    return reversed_elements

# 5. ფუნქცია, რომელიც მომხმარებელს სთხოვს 3 საყვარელი სპორტის შეყვანას.
def pick_random_sport():
    sports = []
    print("მიუთითეთ თქვენი 3 საყვარელი სპორტი:")
    for i in range(3):
        sport = input(f"სპორტი {i + 1}: ")
       
