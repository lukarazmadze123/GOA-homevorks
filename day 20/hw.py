numb = int(input("შემოიყვანე რიცხვი -> "))

if numb >100 :
    print("შენს მიერ შემოყვანილი რიცხვი არის დადებითი")


elif numb <101 :
    print("შენს მიერ შემოყვანილი რიცხვი არის უარხოფითი ")

else :
    print("შენი რიცხვი არის არასწორი")





number0 = int(input("შემოიტანე პირველი რიცხვი "))
number1 = int(input("შემოიყვანე მეორე რიცხვი "))

if number0 < number1 :
    print("მეორე მეტია პირველზე")

elif number0 > number1 :
    print("პირველი რიცხვი მეტია მეორეზე")


else :
    print("<>")



num = int(input("შემოიყვანე 1 -10 რიცხვი "))
if num == 6 :
    print("მოიგე 100,000 დოლარი")
elif num == 2 :
    print(10,000)

else :
    print("მოიგე 10 დოლარი")