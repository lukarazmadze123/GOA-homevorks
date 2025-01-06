ice_cream_set = {"chocolate", "vanilla", "strawberry", "mint", "cookie"}

check_flavor = print("შეიყვანეთ ნაყინის სახელი: ").lower()

if check_flavor in ice_cream_set:
    print("ყოჩაღ!!!!")
else:
    print("ეს სახელი ჩვენს სიის არ არის. სცადეთ სხვა.")
"-------------------------------------------------------------"

# ტუპლის შექმნა
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# პირველი ორი ელემენტის ცვლადებში შენახვა და დანარჩენების სხვა ცვლადში *-ის გამოყენებით შენახვა
first, second, *rest = my_tuple

# შედეგების დაბეჭდვა
print("პირველი:", first)
print("მეორე:", second)
print("დანარჩენი:", rest)
