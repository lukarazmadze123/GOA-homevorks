class AceVentura:
    def __init__(self):
        self.hit_count = 0
    
    def stone_throw(self):
        self.hit_count += 1
        if self.hit_count == 1:
            print("ვაიმე პირდაპირ ფეხში მომხვდა!")
        elif self.hit_count == 2:
            print("ვაიმე ორივე ფეხში მომხვდა!!~")

# გამოყენება
ace = AceVentura()
ace.stone_throw()  # პირველად სროლა
ace.stone_throw()  # მეორედ სროლა
ace.stone_throw()  # მესამედ სროლა, არაფერი არ ხდება
