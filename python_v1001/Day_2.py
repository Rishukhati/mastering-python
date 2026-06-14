# Q1. Given a list of numbers, return the sum of all even numbers.
# Input:  [1, 2, 3, 4, 5, 6]
# Output: 12

arr1 = [1,2,3,4,5,6]
total = 0
for num in arr1:
    if num % 2 == 0:
        total = total + num
print(total)

arr2 = [1, 2, 3, 4, 5]
result = []
for i in range(len(arr2) - 1, -1, -1):
    result.append(arr2[i])
print(result)
