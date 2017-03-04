car = {'make': 'bmw', 'model': '550i', 'year': 2016}
car_list = []
print(car)
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}
print(cars)
print(cars['bmw'])
print(len(car))
print(car.keys())
car_list = car.keys()
car_string = " ".join(car_list)
"""for i in car_string:
    print(i)"""

my_tuple = (2, 4, 10, 10, 10)
#print(my_tuple.count(10))
#print(my_tuple.index(10))

# list is mutable but tuple is immutable
list1 = [1, 2, 1, 2, 3, 2, 4, 5, 5, 6]
s = []
count = 0
for i in list1:
    if i not in s:
        s.append(i)
        count += 1
print(s)
print(count)










