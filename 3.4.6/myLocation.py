# Nadia Clarissa Hermawan / 6181901013

class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

loc1 = Location("Thomas", "Portugal")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
your_loc = Location("Nadia", "Indonesia")

loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
your_loc.myLocation()