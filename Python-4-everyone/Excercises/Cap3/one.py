"""
Calculate the pay of a employee, based on the Rate of dolars given in a hour
And the total worked hours. After 40 hours the rate is 1.5 higher.
Handle errors, with try-except
"""


class Employee:
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    def calculate_pay(self):
        payment = 0
        if self.hours >= 40:
            extra_hours = self.hours - 40
            payment += 40 * self.rate
            payment += extra_hours * (self.rate * 1.5)
        elif self.hours < 40:
            payment += self.hours * self.rate
        else:
            print("Invalid hours!")

        return payment


Peter = Employee(15, 44)
print(f"Peter salary is {Peter.calculate_pay()}")

try:
    You = Employee(float(input("Your rate > ")),
                   float(input("Your total hours > ")))
    print(f"Your salary is {You.calculate_pay()} $ ")
except ValueError:
    print("Your rate and hours should be numbers")
