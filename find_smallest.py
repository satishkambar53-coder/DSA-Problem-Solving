numbers=[13,12,8,96,82]

smallest=numbers[0]

for number in numbers:
    if smallest>number:
        smallest = number

print("Smallest number:",smallest)
