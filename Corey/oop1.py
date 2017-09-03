class Employee:

    no_of_emp = 0
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.no_of_emp += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        return int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod  # acting as alternate constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


print(Employee.no_of_emp)

emp1 = Employee('Amol', 'Srivastav', 130000)
emp2 = Employee('Test', 'User', 50000)

emp_str1 = 'john-doe-10000'

emp3 = Employee.from_string(emp_str1)

print(emp1.__dict__)

print(emp3.first)
print(Employee.no_of_emp)
print(emp1.apply_raise())

print(emp1.fullname())

print(Employee.fullname(emp1))


import datetime

my_date = datetime.date(2016, 7, 10)
print(emp1.is_workday(my_date))


class Developer(Employee):


    def __init__(self, first, last, pay, prg_lang):

        super().__init__(first, last, pay)
        self.prg_lang = prg_lang



dev1 = Developer('Amol', 'Srivastav', 130000, 'python')
dev2 = Developer('Test', 'User', 50000, 'java')


print(dev2.fullname())

class Manager(Employee):


    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


mgr1 = Manager('Sue', 'Son', 90000, [dev2])


print(mgr1.email)

mgr1.print_emp()
mgr1.add_emp(dev1)

mgr1.print_emp()






