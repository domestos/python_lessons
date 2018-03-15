cities = ['New York', 'Ukrainia', 'Toronto']

print(cities)
print(len(cities))
print(cities[0]  + " <-|| print first element")
print(cities[-1] + " <-|| print last element")

#add element
cities.append("Lviv")
cities.insert(2,"Kiev")

#delete element
del cities[3]

cities.remove("New York")
deleted_city = cities.pop()


print(cities)
print("deleted_city is "+ deleted_city)


#sort List
cities.sort()
cities.reverse()

print(cities)
