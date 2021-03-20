class Myclass:
    def __init__(self, name):
        self.name = name
        self.upper_name = name.upper()

    def print_name(self):
        print("Hi my name is ", self.name)

    def print_upper_name(self):
        print("Hi my name is ", self.upper_name)


class MySubClass(Myclass):

    def print_default_name(self):
        print(self.default_name)


myperson = MySubClass("manuelito")

print(dir(myperson))

print(myperson.print_name())
print(myperson.print_upper_name())
print(myperson.print_default_name())
