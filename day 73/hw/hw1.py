def turtle_race(speed1, speed2):
    if speed1 > speed2:
        return "პირველი კუ უფრო სწრაფია!"
    else:
        if speed2 > speed1:
            return "მეორე კუ უფრო სწრაფია!"
        else:
            return "ორივე კუ თანაბრად სწრაფია!"

# გამოყენება:
speed1 = int(input("შეიყვანე პირველი კუს სიჩქარე: "))
speed2 = int(input("შეიყვანე მეორე კუს სიჩქარე: "))
print(turtle_race(speed1, speed2))