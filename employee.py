"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee():
    def __init__(self, name, salary, monthHour, hours, wage, commission, cContract, cContractWage, bCommission):
        self.name = name
        self.salary = salary
        self.monthHour = monthHour
        self.hours = hours
        self.wage = wage
        self.commission = commission
        self.cContract = cContract
        self.cContractWage = cContractWage
        self.bCommission = bCommission

    def get_pay(self):
        if self.monthHour == "month" and self.commission == 0:
            return self.salary
        elif self.monthHour == "month" and self.commission == 1:
            return self.salary + (self.cContract * self.cContractWage)
        elif self.monthHour == "month" and self.commission == 2:
            return self.salary + self.bCommission
        elif self.monthHour == "hour" and self.commission == 0:
            return self.hours * self.wage
        elif self.monthHour == "hour" and self.commission == 1:
            return (self.hours * self.wage) + (self.cContract * self.cContractWage)
        elif self.monthHour == "hour" and self.commission == 2:
            return (self.hours * self.wage) + self.bCommission


    def __str__(self):
        if self.monthHour == "month" and self.commission == 0:
            string = f"{self.name} works on a monthly salary of {self.get_pay()}. Their total pay is {self.get_pay()}."
        elif self.monthHour == "month" and self.commission == 1:
            string = f"{self.name} works on monthly salary of {self.get_pay()} and recieves a commission for {self.cContract} contract(s) at {self.cContractWage}/contract. Their total pay is {self.get_pay()}."
        elif self.monthHour == "month" and self.commission == 2:
            string = f"{self.name} works on monthly salary of {self.get_pay()} and recieves a bonus commission of {self.bCommission}. Their total pay is {self.get_pay()}."
        elif self.monthHour == "hour" and self.commission == 0:
            string = f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour. Their total pay is {self.get_pay()}."
        elif self.monthHour == "hour" and self.commission == 1:
            string = f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour. and recieves a commission for {self.cContract} contract(s) at {self.cContractWage}/contract.Their total pay is {self.get_pay()}."
        elif self.monthHour == "hour" and self.commission == 2:
            string = f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and recieves a bonus commission of {self.bCommission}. Their total pay is {self.get_pay()}."
        return string




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, "month", 0, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, "hour", 100, 25, 0, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, "month", 0, 0, 1, 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, "hour", 150, 25, 1, 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, "month", 0, 0, 2, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, "hour", 120, 30, 2, 0, 0, 600)
