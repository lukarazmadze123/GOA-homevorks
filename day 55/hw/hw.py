# ოჯახის წევრების ინფორმაცია
member1 = ("სოლომონი", 40, "მამა")
member2 = ("ნატალია", 38, "დედა")
member3 = ("ანა", 15, "შვილი")
member4 = ("ლუკა", 12, "შვილი")

# ტუპლების სია
family = [member1, member2, member3, member4]

print(family)

"-----------------------------------------------------"

# ტუპლის შექმნა
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# პირველი სამი და დანარჩენი
first, second, third, *rest = my_tuple

print("პირველი:", first)
print("მეორე:", second)
print("მესამე:", third)
print("დანარჩენი:", rest)

"-----------------------------------------------------"

# ქათმის სახელების dictionary
chickens = {
    "chicken_1": "ბეთი",
    "chicken_2": "ლედი",
    "chicken_3": ("ლაქა", "პასტი", "სანი"),  # ტუპლი
    "chicken_4": "კიკო"
}

print(chickens)

"-----------------------------------------------------"

# tuple-ზე წვდომა
chicken_tuple = chickens["chicken_3"]

# პირველი ელემენტი
first_element = chicken_tuple[0]
print("პირველი ელემენტი:", first_element)

"----------------------------------------------------------"

# დანარჩენი ელემენტები
_, *rest = chicken_tuple

print("დანარჩენი:", rest)
