
# 5. მგელი და ბატკნის გამოცდა (if-else ვერსია)
def wolf_riddle(word):
    if word.lower() == "ბატკანი":
        return "გადარჩი!"
    else:
        return "მგელმა შეგჭამა!"

# გამოყენება:
word = input("შეიყვანე სიტყვა: ")
print(wolf_riddle(word))
