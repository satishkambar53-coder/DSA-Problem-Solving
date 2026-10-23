 
numbers = [10, 25, 40, 30, 40, 15]

largest = float("-inf")
second_largest = float("-inf")

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number < largest and number > second_largest:
        second_largest = number

if second_largest == float("-inf"):
    print("No second-largest distinct number")
else:
    print("Second largest number:", second_largest)
