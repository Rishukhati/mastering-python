#Q3
arr = [3,1,2,3,1,4]
remove = set(arr)

sort= sorted(remove)
print(sort)
#Q4
word=  "Rishabh"
count= {}

for char in word:
    if char in count:
        count[char] +=1
    else:
        count[char] = 1
print(count)
#Q5
arr2=  [4, 3, 2, 7, 3, 1]
seen = set()
for num in arr2 :
    if num in seen :
        print(num)
        break
    seen.add(num)
#Q6
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Q7
arr3 = [10, 5, 8, 20, 15]
result = sorted(arr3)
print(result[-1])