score = 70

if score >= 80:
    print('You pass the course with flying colors!')

elif score > 65:
    print('You pass the course! Talk to your instructor.')

else:
    print('You do not pass the course!')

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

for i in range(3):  # range() function can be used with the for loop to execute multiple times
    print(i)

teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
    for name in team:
        print(name, team)

i = 1
while i < 6:
    print(i)
    i += 1

nums = [3, 4, 16]

print('This is an example of for loops')

for num in nums:
    print(num ** 2)

# while loop
i = 3

print('This is an example of while loops')

while i < 258:
    print(i)
    i = i ** 2

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for name in names:  # The pass keyword is mostly used as a placeholder in a loop. Nothing gets executed.
    if 'j' in name.lower():
        pass
    else:
        print(name)

for name in names:
    if 'h' in name.lower():
        break
    else:
        print(name)

for name in names:
    if 'm' in name.lower():
        continue
    else:
        print(name)

nums = [5, 2, 3, 10]

try:
    avg = sum(nums) / len(nums)
    print('The average of the list is: ', avg)

except:
    print('Cannot compute average - make sure you enter a list of integers!')

finally:
    print('Feel free to rerun the code with another list of integers!')
