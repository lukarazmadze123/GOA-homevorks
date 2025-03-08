
# 4. ძაღლისა და ბომბის რობოტის გამოცანა (if-else ვერსია)
def dog_riddle(numbers):
    new_numbers = []
    for num in numbers:
        if True:  # ეს if ფაქტობრივად აქ არაა საჭირო, მაგრამ შენიშვნისთვის დავტოვე
            new_numbers.append(num + 10)
    return new_numbers

# გამოყენება:
numbers = list(map(int, input("შეიყვანე 3 რიცხვი დაშორებით: ").split()))
print("შედეგები:", dog_riddle(numbers))