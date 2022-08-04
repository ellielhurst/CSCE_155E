from random import randint
import names

TAKEN_HOUSE_NUMBERS = []

class house:
    # house() -> will init 
    def __init__(self): 
        self.house_number = self.generate_number()
        self.roof_color_options = ['blue', 'yellow', 'green']
        self.roof_color = self.roof_color_options[randint(0,2)]
        self.occupants = [names.get_first_name()]

    def change_roof_color(self, color):
        if color not in self.roof_color_options:
            print(f"not valid color. pick between {self.roof_color_options}")
        else:
            self.roof_color = color
    
    def generate_number(self):
        number = randint(100, 109) # set random house number
        while number in TAKEN_HOUSE_NUMBERS: # while current number is in TAKEN list
            number = randint(100, 109) # generate new number
        TAKEN_HOUSE_NUMBERS.append(number) # "registering" number to TAKEN list
        return number
        
    def __str__(self):
        return f'{self.occupants} are at house {self.house_number} with the {self.roof_color} roof.\n' #print to output 


class cul_de_sac:                               #class for cul_de_sac
    def __init__(self):                     #constructer def
        self.list_of_houses = [] 
        self.num_houses = randint(2, 5) # returns a random number between 2 and 5
        for i in range(self.num_houses):     #looping through range of the random number of houses being generated
            self.list_of_houses.append(house())     #
        self.zipcode = randint(60000, 69999)

    def get_list(self):
        return self.list_of_houses

    def move_number(self, start_h, end_h):
        house_start = None
        house_end = None
        for house in self.list_of_houses:
            if start_h == house.house_number:
                house_start = house
            if end_h == house.house_number:
                house_end = house

        if house_start is not None and house_end is not None:
            house_end.occupants.extend(house_start.occupants)
            house_start.occupants.clear()         

    def __str__(self):
        string = str(self.zipcode) + '\n'
        for i in range(self.num_houses):
            string += (f'{self.list_of_houses[i]}')
        return string


def main():
    test = cul_de_sac()
    print(test)
    while True:
        house_start, house_end = [int(i) for i in input("Select house num to move (ex 100 109): ").split()]
        test.move_number(house_start, house_end)
        print(test)


main()


