class Animal:
    def _init_(self, habitat,no_of_legs,species):
        self.habitat= habitat
        self.no_of_legs= no_of_legs
        self.species= species
    
    def behaviour(self, answer):
        if answer == 'yes':
            print('animal is aggressive')
        elif answer == 'sometimes':
            print('sometimes friendly, other times aggressive')
        else:
            print('friendly')

DOG=Animal('apartment', 4,'canine')
behaviour('sometimes')

class insect(Animal):
    pass
Ant=insect('anthill', 6, 'fireant'  )
Ant.behaviour(no)