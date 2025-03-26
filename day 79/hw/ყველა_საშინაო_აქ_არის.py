def traffic_light(color):
    colors = {
        "წითელი": "გაჩერდი!",
        "ყვითელი": "მოემზადე!",
        "მწვანე": "გაიარე!"
    }
    return colors.get(color, "შეცდომა: უცნობი ფერი!")


def grade(score):
    if 90 <= score <= 100:
        return "შესანიშნავი!"
    elif 75 <= score <= 89:
        return "კარგი!"
    elif 50 <= score <= 74:
        return "საშუალო!"
    elif 30 <= score <= 49:
        return "სუსტია!"
    elif 0 <= score <= 29:
        return "ჩავარდნა!"
    else:
        return "შეცდომა: არასწორი ქულა!"


def parking_fee(hours):
    if hours < 1:
        return "უფასო"
    elif 1 <= hours <= 3:
        return "5 ლარი"
    elif 4 <= hours <= 6:
        return "10 ლარი"
    else:
        return "20 ლარი"


def temperature_status(temp):
    if temp >= 30:
        return "ცხელა"
    elif 20 <= temp < 30:
        return "თბილა"
    elif 10 <= temp < 20:
        return "ცოტა ცივა"
    else:
        return "ძალიან ცივა"


def drink_advice(drink):
    drinks = {
        "ყავა": "გაიღვიძე და იმუშავე!",
        "კაკაო": "დაისვენე და მოდუნდი!",
        "წყალი": "დაიწყე ჯანმრთელი ცხოვრება!",
        "ლიმონათი": "გაგრილდი"
    }
    return drinks.get(drink, "შეარჩიე სხვა სასმელი!")


print(traffic_light("წითელი")) 
print(grade(85))  
print(parking_fee(5))
print(temperature_status(15))
print(drink_advice("კაკაო")) 
