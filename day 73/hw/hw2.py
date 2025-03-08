def beaver_riddle(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    # ახალი სია მაქსიმალურის გარეშე
    new_numbers = []
    for num in numbers:
        if num != max_num:
            new_numbers.append(num)
    return new_numbers


# გამოყენება:
numbers = list(map(int, input("შეიყვანე 5 რიცხვი დაშორებით: ").split()))
print("დანარჩენი რიცხვები:", beaver_riddle(numbers))