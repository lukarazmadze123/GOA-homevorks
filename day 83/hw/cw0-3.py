# მაგალითი 1: 1-დან 5-ის ჩათვლით რიცხვების დაბეჭდვა
for i in range(1, 6):
    print(i)

# მაგალითი 2: სიაში არსებული ელემენტების დაბეჭდვა
fruits = ["ვაშლი", "მსხალი", "ბანანი"]
for fruit in fruits:
    print(fruit)

# მაგალითი 3: სტრიქონის თითოეული ასოს დაბეჭდვა
word = "Python"
for letter in word:
    print(letter)

# მაგალითი 4: რიცხვების ჯამი (1-დან 5-მდე)
sum = 0
for i in range(1, 6):
    sum += i
print("ჯამი:", sum)

# მაგალითი 5: მხოლოდ ლუწი რიცხვების დაბეჭდვა
for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# მაგალითი 1: 1-დან 5-ის ჩათვლით რიცხვების დაბეჭდვა
i = 1
while i <= 5:
    print(i)
    i += 1

# მაგალითი 2: მომხმარებლისგან სწორი პაროლის მოთხოვნა
password = ""
while password != "1234":
    password = input("შეიყვანეთ პაროლი: ")

# მაგალითი 3: რიცხვების ჯამი სანამ 100-ს არ გადააჭარბებს
i = 1
sum = 0
while sum <= 100:
    sum += i
    i += 1
print("ჯამი გახდა:", sum)

# მაგალითი 4: უკუღმა დათვლა 5-დან 1-მდე
i = 5
while i > 0:
    print(i)
    i -= 1

# მაგალითი 5: უსასრულო ციკლი შეწყვეტით
while True:
    num = int(input("შეიყვანე 0-ს გასაჩერებლად: "))
    if num == 0:
        break


