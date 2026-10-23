numbers=[5, 10, 15, 12, 20]

is_sorted=True

for i in range(len(numbers)-1):
    if numbers[i]>numbers[i+1]:
        is_sorted=False
        break

if is_sorted:
    print("List is sorted")
else:
    print("List is not sorted")