family = {
    "Mother": {"First Name": "Maria", "Last Name": "Smith"},
    "Father": {"First Name": "John", "Last Name": "Smith"},
    "Sibling": {"First Name": "Sophia", "Last Name": "Smith"}
}

# Print family details
for role, details in family.items():
    print(f"{role}: {details['First Name']} {details['Last Name']}")

"---------------------------------------------------------------"

car = {
    "Model": "Tesla Model S",
    "Year": 2022
}

print(f"The car is a {car['Model']} made in {car['Year']}.")

"-----------------------------------------------------------"

# Creating 38 dictionaries to represent today's learned material
learned_material = []

for i in range(38):
    learned_material.append(
        {
            "Lesson": f"Topic {i + 1}",
            "Description": f"Details about lesson {i + 1}",
            "Duration (minutes)": 30
        }
    )

# Example output from the first and last entries
print(learned_material[0])  # First lesson
print(learned_material[-1])  # Last lesson

"----------------------------------------------------------"

programming = {
    "Languages": ["Python", "JavaScript", "C++", "Java"],
    "Concepts": ["Variables", "Loops", "Functions", "Classes"],
    "Favorite Frameworks": {"Frontend": "React", "Backend": "Django"},
    "Goals": "Build complex applications and master algorithms."
}

# Display details from the dictionary
print(f"Languages I love: {', '.join(programming['Languages'])}")
print(f"Key Concepts: {', '.join(programming['Concepts'])}")
print(f"My favorite frameworks are: {programming['Favorite Frameworks']['Frontend']} (Frontend) and {programming['Favorite Frameworks']['Backend']} (Backend).")
