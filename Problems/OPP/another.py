class Myclass:
    def __init__(self, name):
        self.name = name
        self.upper_name = name.upper()

    def print_name(self):
        print("Hi my name is ", self.name)

    def print_upper_name(self):
        print("Hi my name is ", self.upper_name)


class MySubClass(Myclass):

    @property
    def get_default_name(self):
        self.default_name = self.name + "default"
        return self.default_name

    @get_default_name.setter
    def print_default_name(self):
        print(self.default_name)


myperson = MySubClass("manuelito")

print(dir(myperson))

print(myperson.print_name())
print(myperson.print_upper_name())
print(myperson.print_default_name())
