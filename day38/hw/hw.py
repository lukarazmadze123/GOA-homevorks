def calculate_sum(num1, num2):
    return num1 + num2

"------------------------------------------------------------"


result = calculate_sum(5, 3)
print("ჯამი არის:", result) 


"------------------------------------------------------------"


def is_even(number):
    return number % 2 == 0


"--------------------------------------------------------------"

print(is_even(4))
print(is_even(7))


"---------------------------------------------------------------"


def greet_user(name):
    print(f"გამარჯობა, {name}!")

"-----------------------------------------------------------------"

def calculate_user_inputs():
    num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
    print("ორივე რიცხვის ჯამი არის:", calculate_sum(num1, num2))

"-------------------------------------------------------------------"

