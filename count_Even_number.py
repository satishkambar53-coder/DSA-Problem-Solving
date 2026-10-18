numbers=[10,12,18,17,19,9]
count=0

for number in numbers:
    if number % 2==0:
        count+=1

print("Even number:",count)