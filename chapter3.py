# CHAPTER 3 - INTRODUCING LISTS

# 3-1. Names (pg 36)
names = ['conor', 'ciaran', 'emily', 'jack', 'shannon']

print(names[0])
print(names[1])
print(names[2])
print(names[-2])
print(names[-1])

# 3-2. Greetings (pg 36)
print(f"{names[0].title()} should learn Python!")
print(f"{names[1].title()} should learn Python!")
print(f"{names[2].title()} should learn Python!")
print(f"{names[-2].title()} should learn Python!")
print(f"{names[-1].title()} should learn Python!")

# 3-3. Your Own List (pg 36)
cars = ['ford', 'toyota', 'mercedes', 'bmw', 'audi']

print(f"I drive a {cars[0].title()}.")
print(f"I drive a {cars[1].title()}.")
print(f"I drive a {cars[2].title()}.")
print(f"I drive a {cars[3].upper()}.")
print(f"I drive a {cars[4].title()}.")

# 3-4. Guest List (pg 42)
guests = ['robin williams', 'steve jobs', 'taylor swift']

print(f"Dear {guests[0].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[1].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[-1].title()}, please consider this a formal invite to my dinner party.")

# 3-5. Changing Guest List (pg 42)
print(f"{guests[1].title()} cannot attend the dinner party")

del guests[1]

guests.append('darth vader')

print(f"Dear {guests[0].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[1].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[-1].title()}, please consider this a formal invite to my dinner party.")

# 3-6. More Guests (pg 42)
print("Good news! I have sourced a bigger table so we will have more guests.")

guests.insert(0, 'julius caesar')
guests.insert(2, 'keanu reeves')
guests.append('george costanza')
print(guests)

print(f"Dear {guests[0].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[1].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[2].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[3].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[-2].title()}, please consider this a formal invite to my dinner party.")
print(f"Dear {guests[-1].title()}, please consider this a formal invite to my dinner party.")

# 3-7. Shrinking Guest List (pg 43)
print("Hi all, unfortunately the new table will not arrive in time. As such I can only invite two people.")

uninvited_guests = guests.pop()
print(f"Hi {uninvited_guests.title()}, unfortunately we have to uninvite you from the party.")
uninvited_guests = guests.pop()
print(f"Hi {uninvited_guests.title()}, unfortunately we have to uninvite you from the party.")
uninvited_guests = guests.pop()
print(f"Hi {uninvited_guests.title()}, unfortunately we have to uninvite you from the party.")
uninvited_guests = guests.pop()
print(f"Hi {uninvited_guests.title()}, unfortunately we have to uninvite you from the party.")

print(f"Dear {guests[0].title()}, I am just writing to confirm that you are still invited to the dinner party. Hope to see you soon.")
print(f"Dear {guests[1].title()}, I am just writing to confirm that you are still invited to the dinner party. Hope to see you soon.")

del guests[1]
del guests[0]
print(guests )

# 3-8. Seeing The World (pg 46)
locations = ['hawaii', 'tokyo', 'sydney', 'rome', 'dublin']

print(locations) 
print(sorted(locations))

print(locations)
print(sorted(locations, reverse=True))

print(locations)
locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

# 3-9. Dinner Guests
print(f"Hi, I am writing to confirm that I am inviting {len(guests)} to dinner.")

# 3-10. Every Function (pg 46)
sports = ['soccer', 'ice hockey', 'basketball', 'hurling', 'rugby']
print(sports)

print(sports[0].title())

message = f"I used to play {sports[1]}!"
print(message)

sports.append('baseball')
print(sports)

sports.insert(3, 'cricket')
print(sports)

del sports[5]
print(sports)

popped_sports = sports.pop()
print(popped_sports)

print(sorted(sports))
sports.sort()
print(sports)
sports.sort(reverse=True)
print(sports)
sports.reverse()
print(sports)
print(len(sports))

#3-11. Intentional Error (corrected) (pg 48)
print(sports[4])