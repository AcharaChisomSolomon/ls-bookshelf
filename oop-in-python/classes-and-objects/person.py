class Person:
    def __init__(self, first_name, last_name):
        try:
            self.first_name = first_name
            self.last_name = last_name
        except Exception as e:
            print(e)

    def raise_error(self):
        raise ValueError("ValueError: Name must be alphabetic.")
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        if name.isalpha():
            self._first_name = name
        else:
            self.raise_error()

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        if name.isalpha():
            self._last_name = name
        else:
            self.raise_error()

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}".title()
    
    @name.setter
    def name(self, names):
        try:
            self.first_name = names[0]
            self.last_name = names[1]
        except Exception as e:
            print(e)
            


# actor = Person('Mark', 'Sinclair')
# print(actor.name)              # Mark Sinclair
# actor.name = ('Vin', 'Diesel')
# print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.


# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.


friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.