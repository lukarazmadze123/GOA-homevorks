# 1. დათვი და მელიას თავსატეხი (if-else ვერსია)
def bear_riddle(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return f"მაქსიმალური: {max_num}, მინიმალური: {min_num}"

# გამოყენება:
numbers = list(map(int, input("შეიყვანე 6 რიცხვი დაშორებით: ").split()))
print(bear_riddle(numbers))

