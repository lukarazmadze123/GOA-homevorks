def bunny_hunter(lst, bunny_name):
    if bunny_name in lst: 
        return f"{bunny_name} ბევრი ვსვათ და ბევრი ვჭამოთ თუ დრო დაგვრჩა ვიმუშაოთ🍔🍕🍟🌭"
    else:
        return f"{bunny_name} ვინაა ბიჯო ჩჩმორიი დაახვიეეე👋👋"


bunny_list = ["გელა", "თინა", "ზაირა", "ნუკტი"]
print(bunny_hunter(bunny_list, 'გელა'))  
print(bunny_hunter(bunny_list, 'ინგა'))
print(bunny_hunter(bunny_list, 'ნატუკა'))
print(bunny_hunter(bunny_list, 'ჩჩმორიიი'))
