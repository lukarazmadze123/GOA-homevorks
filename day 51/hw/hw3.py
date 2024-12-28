family = {
    "Mother": "nini",
    "Father": "giga",
    "sister": "elene",
}

print(f"Our family consists of: {family}")


"------------------------------------------------------"

# Creating a dictionary about our favorite car
favorite_car = {
    "Brand": "Tesla",
    "Model": "Model S",
    "Year": 2023,
    "Color": "Midnight Silver",
    "Electric": True
}

print(f"My favorite car is a {favorite_car['Year']} {favorite_car['Brand']} {favorite_car['Model']} in {favorite_car['Color']} color.")

"------------------------------------------------------------------"

# Creating a dictionary about myself
about_me = {
    "Name": "razma",
    "Age": 11,
    "Hobby": "codding",
    "Favorite Food": "burger , mwvadi , xinkali",
}

# Generating a small introduction using f-strings
intro = f"Hello! My name is {about_me['Name']}. I am {about_me['Age']} years old and I love {about_me['Hobby']}. " \
        f"My favorite food is {about_me['Favorite Food']} and my dream is {about_me['Dream']}."

print(intro)
