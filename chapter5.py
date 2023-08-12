# CHAPTER 5 - IF STATEMENTS

# 5-1. Conditional Tests (pg. 78)
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

flavour = 'mint'
print("Is flavour == 'mint'? I predict True.")
print(flavour == 'mint')
print("Is flavour == 'strawberry'? I predict False.")
print(car == 'strawberry')

sport = 'soccer'
print("Is sport == 'soccer'? I predict True.")
print(sport == 'soccer')
print("Is sport == 'rugby'? I predict False.")
print(sport == 'rugby')

drink = 'coke'
print("Is drink == 'coke'? I predict True.")
print(drink == 'coke')
print("Is drink == 'fanta'? I predict False.")
print(drink == 'fanta')

subject = 'history'
print("Is subject == 'history'? I predict True.")
print(subject == 'history')
print("Is subject == 'math'? I predict False.")
print(subject == 'math')

# 5-2. More Conditional Tests (pg. 78)
fruit = 'banana'
print("Is fruit == 'banana'? I predict True.")
print(fruit == 'banana')
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

name = 'Conor'
print("Is name == 'conor'? I predict False.")
print(name == 'conor')
print("Is name == 'conor'? I predict True.")
print(name.lower() == 'conor')

number = 42
print("Is number == 42? I predict True.")
print(number == 42)
print("Is number == 17? I predict False.")
print(number == 17)

print("Is number > 40? I predict True.")
print(number > 40)
print("Is number < 17? I predict False.")
print(number < 17)

print("Is number >= 42? I predict True.")
print(number >= 42)
print("Is number <= 20? I predict False.")
print(number <= 20)

print("Is number >= 42 and <100? I predict True.")
print((number >= 42) and (number < 100))
print("Is number <= 20 or < 40 I predict False.")
print((number <= 20) or (number < 40))

hats = ['baseball', 'beanie', 'cowboy']
print("Is 'cowboy' a type of hat? I predict True.")
print('cowboy' in hats)
print("Is 'socks' not a type of hat? I predict True.")
print('socks' not in hats)

# 5-3. Alien Colors (pg. 84)
alien_color = 'green'

if alien_color == 'green':
	print("You have just earned 5 points!")

if alien_color == 'blue':
	print("You have just earned 5 points!")

# 5-4. Alien Colors #2 (pg. 84)
if alien_color == 'green':
	print("You have just earned 5 points!")
if alien_color != 'green':
	print("You have just earned 10 points!")

if alien_color == 'green':
	print("You have just earned 5 points!")
else:
	print("You have just earned 10 points!") 

# 5-5. Alien Colors #3 (pg. 85)
if alien_color == 'green':
	print("You have just earned 5 points!")
elif alien_color == 'yellow':
	print("You have just earned 10 points!")
elif alien_color == 'red':
	print("You have just earned 15 points!")

# 5-6. Stages of Life (pg. 85)
age = 26

if age < 2:
	print("This person is a baby.")
elif (age >= 2) and (age < 4):
	print("This person is a toddler.")
elif (age >= 4) and (age < 13):
	print("This person is a kid.")
elif (age >= 13) and (age < 20):
	print("This person is a teenager.")	
elif (age >= 20) and (age < 65):
	print("This person is a adult.")	
else:
	print("This person is an elder.")

# 5-7. Favorite Fruit (pg. 85)
fruits = ['strawberry', 'banana', 'blueberry']

if 'strawberry' in fruits:
	print("You like strawberries!")
if 'apple' in fruits:
	print("You like apples!")
if 'banana' in fruits:
	print("You like bananas!")
if 'grape' in fruits:
	print("You like grapes!")
if 'blueberry' in fruits:
	print("You like blueberries!")

# 5-8. Hello Admin (pg. 89)
usernames = ['admin', 'conor', 'sally', 'sam', 'mark' ]

for username in usernames:
	if username == 'admin':
		print(f"Hello {username.title()}, would you like to see a status report?")
	else:
		print(f"Hello {username.title()}, thank you for logging in.")

# 5-9. No Users (pg. 89)
if usernames:
	for username in usernames:
		if username == 'admin':
			print(f"Hello {username.title()}, would you like to see a status report?")
		else:
			print(f"Hello {username.title()}, thank you for logging in.")
else:
	print("We need to find some users!")

# 5-10. Checking Usernames (pg. 89)
current_users = ['conor', 'orlaith', 'ronan', 'brona', 'anna']
new_users = ['anna', 'mark', 'sam', 'eoghan', 'conor']

for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"Sorry, the username {new_user.title()} is not available!")
	else:
		print(f"Hello {new_user.title()}, this username is available!")

# 5-11. Ordinal Numbers (pg. 89)
numbers = list(range(1, 10))

for number in numbers:
	print(number)

for number in numbers:
	if number in numbers == 1:
		print(f'{number}st')
	elif number in numbers == 2:
		print(f'{number}nd')
	elif number in numbers == 3:
		print(f'{number}rd')
	else:
		print(f'{number}th')