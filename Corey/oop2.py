class Employee:



    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'



    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last =last
        self.email = first + '.' + last + '@company.com'

emp1 = Employee('Rajesh', 'khanna')
print(emp1.email)
emp1.fullname = 'Amol Srivastav'
print(emp1.email)
print(emp1.first)
