# Counter class:

class MyCounter:

    # Setting max of counter on initialisation
    def __init__(self, start=0, maximum=100):
        self.count = start
        self.max = maximum

    # Greater than, Less than, Equals
    def __gt__(self, other):
        return self.count > other.count

    def __lt__(self, other):
        return self.count < other.count

    def __eq__(self, other):
        return other.count == self.count

    # Method counting with step 1
    def iterate(self):
        if self.count < self.max:
            self.count += 1

    # Showing current counter value
    def show(self):
        if self.count >= self.max:
            print(f"Counter reached Maximum of {self.max}")
        return self.count

    # Comparing method
    def compare(self, other):
        if self.__gt__(other):
            s = str(f"{self.count} > {other.show()}")
        elif self.__lt__(other):
            s = str(f"{self.count} < {other.show()}")
        else:
            s = str(f"{self.count} = {other.show()}")
        return s


mycounter = MyCounter(1)
mycounter2 = MyCounter(2, 20)
for _ in range(10):
    mycounter.iterate()
    mycounter2.iterate()
print(f"mycounter = {mycounter.show()}")
print(f"mycounter2 = {mycounter2.show()}")
print(mycounter.compare(mycounter2))
