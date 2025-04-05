def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "ნულზე გაყოფა არ შეიძლება"
    elif operation == '//':
        if b != 0:
            return a // b
        else:
            return "ნულზე გაყოფა არ შეიძლება"
    else:
        return "უცნობი ოპერაცია"

def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

def greet(name):
    return f"გამარჯობა, {name}!"

def repeat_string(string, times):
    return string * times

def jean_claude_pushups(days):
    pushups_per_day = 10
    return days * pushups_per_day
