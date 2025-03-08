def calculate_mean(elements):
    if len(elements) == 5:
        mean = sum(elements) / 5
        return mean
    else:
        return "შეცდომა: სიის ელემენტების რაოდენობა არ არის 5."

elements = [3, 6, 9, 12, 15]
result = calculate_mean(elements)
print("არითმეტიკული საშუალო:", result)
