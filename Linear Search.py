numbers = [10,25,55,45,98]
traget=10

found=False

for index in range(len(numbers)):
    if numbers[index]==traget:
        print("Number found at index:",index)
        found=True
        break

if not found:
    print("Number not found")