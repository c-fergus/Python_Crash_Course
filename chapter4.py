# CHAPTER 4 - WORKING WITH LISTS

# 4-1. Pizzas (pg 56)
pizzas = ['mozzarella', 'pepperoni', 'hawaiian']
for pizza in pizzas:
	print(f"I like {pizza} pizza!")
print("Pizza is my favourite food!")

# 4-2. Animals (pg 56)
animals = ['dog', 'cat', 'bird', 'bunny', 'hamster']
for animal in animals:
	print(f"A {animal} would make a great pet.")
print("They are all small!")

# 4-3. Counting to Twenty (pg 60)
for value in range(1, 21):
	print(value)

# 4-4. One Million (pg 60)
numbers = list(range(1,1_000_001))
print(numbers)

# 4-5. Summing a Million (pg 60)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6. Odd Numbers (pg 60)
for number in range(1,21,2):
	print(number) 

# 4-7. Threes (pg 60)
threes = list(range(3,31,3))
for three in threes:
	print(three)

# 4-8. Cubes (pg 60)
cubes = []
for value in range(1,11):
	cubes.append(value**3)
print(cubes)

# 4-9. Cube Comprehension (pg 60)
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
	print(cube)

# 4-10. Slices (pg 65)
print(f"The first three items in this list are:{animals[0:3]}")

print(f"The middle three items in this list are: {animals[1:4]}")

print(f"The last three items in this list are: {animals[-3:]}")

# 4-11. My Pizzas, Your Pizzas (pg 65)
friends_pizzas = pizzas[:]

pizzas.append('sausage')
friends_pizzas.append('mushroom')

print(f"My favourite pizzas are {pizzas}!")
print(f"My friends favourite pizzas are {friends_pizzas}!")

# 4-12. More Loops (pg 65)
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friends_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']

for my_food in my_foods:
	print(my_food)

for friends_food in friends_foods:
	print(friends_food)

# 4-13. Buffet (pg 68)
buffet_foods = ('burger', 'fries', 'wings', 'chicken', 'beans')

for buffet_food in buffet_foods:
	print(buffet_food)

# buffet_foods.append('nachos') # intentional error

buffet_foods = ('burger', 'fries', 'hot dog', 'chicken', 'macaroni')
for buffet_food in buffet_foods:
	print(buffet_food)

                 