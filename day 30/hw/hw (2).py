num = int(input("Please enter an number: "))
        
if num == 0:
    print("It's zero.")
elif num % 2 == 0:
    print("It's even.")
else:
    print("It's odd.")

#----------------------------------------------------------------

def classify_numbers():
    numbers = []
    results = []
    
    # Ask the user for 10 numbers
    for i in range(10):
        while True:
            try:
                num = int(input(f"Please enter number {i + 1}: "))
                numbers.append(num)
                break  # Break the loop if input is valid
            except ValueError:
                print("That's not a valid integer. Please try again.")

    # Classify each number
    for num in numbers:
        if num == 0:
            results.append(0)
        elif num % 2 == 0:
            results.append("even")
        else:
            results.append("odd")

    # Print the results
    print("The classification of the numbers is:", results)

classify_numbers()

#----------------------------------------------------------------
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = (input("add item in a list : "))
list.append(a)
print(list)

#----------------------------------------------------------------

def create_and_modify_list():
    # Generate a list of 10 random integers between -50 and 50
    numbers = [1,4,2,7,8,4,100,12,45,363463]
    
    print("Original list:", numbers)
    
    # Find the lowest number in the list
    lowest_number = min(numbers)
    
    # Create a new list starting with the lowest number + 100, followed by the original numbers
    modified_list = [lowest_number + 100] + numbers
    
    # Sort the modified list in ascending order
    modified_list.sort()
    
    # Print the final sorted list
    print("Modified list:", modified_list)

create_and_modify_list()

#---------------------------------------------------------------------------

list = ["ბანანი","ვაშლი","მაიმუნი","შაურმა"]
a = int(input("how many items do you want to add? : "))
for i in range(a):
    b = input("add : ")
    list.append(b)
print(list)

#----------------------------------------------------------------------------
list = ["harry potter","fall","gods","titanic","xd"]

a = str(input("chosse 'add' , 'insert' or 'delete' something : "))

if a is "add":
    d = int(input("chosse your text : "))
    list.append(d)

if a is "insert":
    e = int(input("on wich index? : "))
    h = int(input("chosse your text : "))
    list.insert[e](h)

if a is "delete":
    f = int(input("on wich index? : "))
    list.delete(e)