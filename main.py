# Apollos Eastman
# Oct 30 2024
# Removing list items
import random
print()

# Part 1: Favorites
favorites = ['Jack Black','Florida','Paris','Chicken Wings','Cheez-its','Nachos']
print(favorites)

# Pop method
favorites.pop()
print(favorites)
favorites.pop(3)
print(favorites)

# Remove method
favorites.remove('Paris')
print(favorites)

# Keyword Del
del favorites[0]
print(f'{favorites}\n')

# Part 2: Guest List
invites = ['Jack Black', 'Markiplier', 'Albert Einstein', 'Saul Goodman', 'Pat Fusty']

print (f'Dear {invites[0]}, please come to my dinner party.')
print (f'Dear {invites[1]}, please come to my dinner party.')
print (f'Dear {invites[2]}, please come to my dinner party.')
print (f'Dear {invites[3]}, please come to my dinner party.')
print (f'Dear {invites[4]}, please come to my dinner party.\n')

cant_come = 'Markiplier'
print (f'Unfortunetely, {cant_come} can\'t come.\n')

invites.remove(cant_come)

print (f'Dear {invites[0]}, please come to my dinner party.')
print (f'Dear {invites[1]}, please come to my dinner party.')
print (f'Dear {invites[2]}, please come to my dinner party.')
print (f'Dear {invites[3]}, please come to my dinner party.\n')

# Shrinking guest list

print('Unfortunately there will only be room fot two people at my dinner party.\n')

guest_pop = random.randint(0, 3)
print(f'Sorry {invites[guest_pop]}, there isnt enough room at the party for you.\n')
invites.pop(guest_pop)

guest_pop = random.randint(0, 2)
print(f'Sorry {invites[guest_pop]}, there isnt enough room at the party for you.\n')
invites.pop(guest_pop)

print(f'Dont worry {invites[0]}, you will still be invited.')
print(f'Dont worry {invites[1]}, you will still be invited.')

del invites[0]
del invites[0]
print(invites)
