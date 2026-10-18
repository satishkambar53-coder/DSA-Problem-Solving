"""number=[10, 20,30,40,50]
print(number[0])
for n in number:
    print(n)"""

#Find the largest number
numbers=[12,52,82,97,45]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Number:",largest)