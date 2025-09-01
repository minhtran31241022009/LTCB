import random
nums = [random.randint(1,10) for i in range(5)]
print(f"#List: {nums}")
# 1. Write a Python program to sum all the items in a list
total = 0
for x in nums:
    total += x
print(f"1) Total: {total}")
# 2. Write a Python program to multiply all the items in a list.
result = 1
for x in nums:
    result *= x
print(f"2) Result: {result}")
# 3. Write a Python program to get the largest number from a list.
largest = nums[0]
for i in nums:
    if i > largest:
        largest = i
print(f"3)The largest number from list: {largest}")
# 4. Write a Python program to get the smallest number from a list.
smallest = nums[0]
for i in nums:
    if i < smallest:
        smallest = i
print(f"4)The smallest number from list: {smallest}")
# 5. Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
samlpe_str = ['abc', 'xyz', 'aba', '1221', 'aa']
print(f"5) Sample string: {samlpe_str}")
count = 0
for s in samlpe_str:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1
print(f"Result: {count}")
# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple
# from a given list of non-empty tuples.
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(f"6) Sample list: {sample_list}")
sorted_list = sorted(sample_list, key=lambda x: x[-1])
print(f"Sorted list: {sorted_list}")
# 7. Write a Python program to remove duplicates from a list.
print(f"7) List: {nums}")
no_duplicates = list(set(nums))
print(f"Removed duplicate numbers list: {no_duplicates}")
# 8. Write a Python program to check if a list is empty or not.
if not nums:
    print("8) Empty list")
else:
    print("8) NOT empty list")
# 9. Write a Python program to clone or copy a list.
cop_list1 = list(nums)
cop_list2 = list(cop_list1)
print(f"9) Original list: {nums}")
print(f"   Copy list_1: {cop_list1}")
print(f"   Copy list_2: {cop_list2}")
# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
words = ["apple", "hi", "banana", "cat", "elephant", "dog"]
n = 3
print(f"10) Sample list: {words}")
print(f"    Given that n = {n}")
result = []
for w in words:
    if len(w) > n:
        result.append(w)
print(f"List of words that are longer than {n}: {result}")
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
nums_1 = [random.randint(1,10) for i in range(5)]
print(f"11) List 1: {nums}")
print(f"    List 2: {nums_1}")
set1 = set(nums)
set2 = set(nums_1)
has_common = not set1.isdisjoint(set2)
print(f"Result: {has_common}")
#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
print(f"12) Sample list: {words}")
result = [words[i] for i in range(len(words)) if i not in (0, 4, 5)]
print(f"Result: {result}")
#13. Write a Python program to generate a 3*4*6 3D array whose each element is*.
print("13)")
array = [[['*' for k in range(6)] for j in range(4)] for i in range(3)]
for i in range(3):
    print("Stage", i+1)
    for j in range(4):
        print(array[i][j])
    print()
#14 Write a Python program to print the numbers of a specified list after removing even numbers from it.
print(f"14) List: {nums}")
result = []
for x in nums:
    if x % 2 != 0:
        result.append(x)
print(f"Result: {result}")
#15. Write a Python program to shuffle and print a specified list.
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(f"15) List: {colors}")
random.shuffle(colors)
print(f"Shuffled list: {colors}")
#16. Write a Python program to generate and print a list of the first and last
# 5 elements where the values are square numbers between 1 and 30 (both included).
squares = [x*x for x in range(1, 31) if x*x <= 30]
if len(squares) <= 5:
    result = squares   # nếu ít hơn hoặc bằng 5 phần tử thì in nguyên list
else:
    result = squares[:5] + squares[-5:]
print("16) Square numbers:", squares)
print("Result:", result)
#17. Write a Python program to check if each number is prime in a given list of numbers.
# Return True if all numbers are prime otherwise False.
print(f"17) List: {nums}")
is_all_prime = True
for n in nums:
    if n < 2:  # 0, 1 không phải số nguyên tố
        is_all_prime = False
        break
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_all_prime = False
            break
    if not is_all_prime:
        break
print(f"Result: {is_all_prime}")
#18. Write a Python program to generate all permutations of a list in Python.
import itertools
data = [1, 2, 3]
print(f"18) List: {data}")
perms = list(itertools.permutations(data))
print(f"Permutations: {perms}")
#19. Write a Python program to calculate the difference between the two lists.
print(f"19) List 1: {nums}")
print(f"    List 2: {nums_1}")
diff1 = list(set(nums) - set(nums_1))  # phần tử có trong list1 mà không có trong list2
diff2 = list(set(nums_1) - set(nums))  # phần tử có trong list2 mà không có trong list1
print("The difference between list1 - list2:", diff1)
print("The difference between list2 - list1:", diff2)
#20. Write a Python program to access the index of a list.
print(f"20) List: {colors}")
for index, value in enumerate(colors):
    print("Index:", index, "->", value)
#21. Write a Python program to convert a list of characters into a string.
chars = ['P', 'y', 't', 'h', 'o', 'n']
print(f"21) {chars}")
string = ''.join(chars)
print(f"Result: {string}")
#22. Write a Python program to find the index of an item in a specified list.
print(f"22) {nums}")
k = int(input("Enter the item: "))
indexes = []
for i in range(len(nums)):
    if nums[i] == k:
        indexes.append(i)
print(f"Index of {k}: {indexes}")
#23. Write a Python program to flatten a shallow list.
list1 = [[1, 2], [3, 4], [5, 6]]
print(f"23) {list1}")
flat = [item for sublist in list1 for item in sublist]
print(f"Flattened list: {flat}")
#24. Write a Python program to append a list to the second list.
list_1 = [1, 2, 3]
list_2 = ["a", "b"]
print(f"24) List 1: {list_1}")
print(f"    List 2: {list_2}")
list_2.extend(list_1)
print(f"Append list 1 to list 2: {list_2}")
#25. Write a Python program to select an item randomly from a list.
print(f"25) List: {colors}")
choice = random.choice(colors)
print(f"A random item from list: {choice}")
#26. Write a Python program to check whether two lists are circularly identical.
list_1_1 = [10, 20, 30, 10]
list_2_2 = [30, 10, 10, 20]
print(f"26) List 1: {list_1_1}")
print(f"    List 2: {list_2_2}")
is_circular = ' '.join(map(str, list_2_2)) in ' '.join(map(str, list_1_1 * 2))
print(f"Two lists are circularly identical? {is_circular}")
#27. Write a Python program to find the second smallest number in a list.
numbers = [random.randint(1,50) for i in range(5)]
print(f"#List: {numbers}")
unique_sorted = sorted(set(numbers))  # bỏ trùng rồi sắp xếp
second_smallest = unique_sorted[1]
print("27) Second smallest number:", second_smallest)
#28. Write a Python program to find the second largest number in a list.
unique_sorted = sorted(set(numbers), reverse=True)  # bỏ trùng, sắp xếp giảm dần
second_largest = unique_sorted[1]
print("28) Second largest number:", second_largest)
#29. Write a Python program to get unique values from a list.
unique_values = list(set(numbers))
print("29) Unique values from list:", unique_values)
#30. Write a Python program to get the frequency of elements in a list.
freq = {}
for i in numbers:
    freq[i] = freq.get(i, 0) + 1
print(f"30) Frequency of elements: {freq}")
#31. Write a Python program to count the number of elements in a list within a specified range.
low, high = 10, 25
count = 0
for x in numbers:
    if low <= x <= high:
        count += 1
print(f"31) The number of elements in range {low} to {high}: {count}")
#32. Write a Python program to check whether a list contains a sublist.
sub_numbers = [random.randint(1,50) for i in range(3)]
print(f"32) List 1: {numbers}")
print(f"    List 2: {sub_numbers}")
found = False
for i in range(len(numbers) - len(sub_numbers) + 1):
    if numbers[i:i+len(sub_numbers)] == sub_numbers:
        found = True
        break
print(f"list 1 contains a list 2? {found} ")
#33. Write a Python program to generate all sublists of a list.
lst = [1, 2, 3]
sublists = []
print(f"33) List: {lst}")
for i in range(len(lst) + 1):
    for j in range(i + 1, len(lst) + 1):
        sublists.append(lst[i:j])
sublists.insert(0, [])      #tính cả list rỗng
print(f"All sublists of a list: {sublists}")
#35. Write a Python program to create a list by concatenating a given list with arange from 1 to n.
lst_1 = ['p', 'q']
n = 5
result = []
print(f"35) List: {lst_1}")
for i in range(1, n+1):
    for item in lst_1:
        result.append(item + str(i))
print(result)
#36. Write a Python program to get a variable with an identification number or string.
x = "Hello"
y = 123
print(f"36) x: {x}, y: {y}")
print("ID of x:", id(x))
print("ID of y:", id(y))
#37. Write a Python program to find common items in two lists.
numbers_1 = [random.randint(1,20) for i in range(5)]
numbers_2 = [random.randint(1,20) for i in range(5)]
print(f"37) List 1: {numbers_1}")
print(f"    List 2: {numbers_2}")
common = list(set(numbers_1) & set(numbers_2))
print("Common items:", common)
#38. Write a Python program to change the position of every n-th value to the(n+1)th in a list.
lst_2 = [0, 1, 2, 3, 4, 5]
print(f"#List: {lst_2}")
for i in range(0, len(lst_2)-1, 2):
    lst_2[i], lst_2[i+1] = lst_2[i+1], lst_2[i]
print(f"38) Result: {lst_2}")
#39. Write a Python program to convert a list of multiple integers into a single integer.
result = int("".join(map(str, lst_2)))
print(f"39) Convert list of multiple integers into a single integer: {result}")
#40. Write a Python program to split a list based on the first character of a word.
words_1 = ["apple", "banana", "cherry", "avocado", "blueberry", "apricot"]
print(f"40) List: {words_1}")
result = {}
for word in words_1:
    key = word[0]   # ký tự đầu tiên
    if key not in result:
        result[key] = []
    result[key].append(word)
print(result)
#41. Write a Python program to create multiple lists.
lists = [[] for i in range(3)]
print(f"41) Multiple lists: {lists}")
#42. Write a Python program to find missing and additional values in two lists.
list_a = ['a', 'b', 'c', 'd', 'e', 'f']
list_b = ['d', 'e', 'f', 'g', 'h']
print(f"42) List a: {list_a}")
print(f"    List b: {list_b}")
missing = list(set(list_a) - set(list_b))   # có trong lista mà không có trong listb
additional = list(set(list_b) - set(list_a)) # có trong listb mà không có trong lista
print("Missing values in second list:", missing)
print("Additional values in second list:", additional)
#43. Write a Python program to split a list into different variables.
my_list = [10, 20, 30]
print(f"43) {my_list}")
a, b, c = my_list
print(a)
print(b)
print(c)
#44. Write a Python program to generate groups of five consecutive numbers in alist.
my_list_1 = list(range(1, 21))
print(f"44) {my_list_1}")
result = [my_list_1[i:i+5] for i in range(0, len(my_list_1), 5)]
print(result)
#45. Write a Python program to convert a pair of values into a sorted unique array.
pair = [random.randint(1,20) for i in range(2)]
print(f"45) {pair}")
result = sorted(set(pair))
print(f"Sorted: {result}")
#46. Write a Python program to select the odd items from a list.
odd_values = [x for x in my_list_1 if x % 2 != 0]
print(f"46) {my_list_1}")
print("Odd values:", odd_values)
#47. Write a Python program to insert an element before each element of a list.
my_list_2 = [1, 2, 3, 4]
print(f"47) {my_list_2}")
print("Given that the element is 0")
element = 0
new_list = []
for x in my_list_2:
    new_list.append(element)
    new_list.append(x)
print(new_list)
#48. Write a Python program to print nested lists (each list on a new line)
# using the print() function.
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(f"48) Nested list: {nested_list}")
for sublist in nested_list:
    print(sublist)
#50. Write a Python program to sort a list of nested dictionaries.
data = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20}
]
print(f"50) {data}")
sorted_data = sorted(data, key=lambda x: x["age"])      # sắp xếp theo tuổi
print(sorted_data)
#51. Write a Python program to split a list every Nth element.
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
print(f"51) Char list: {char}")
print(f"Given that Nth element is {n}")
result = [char[i::n] for i in range(n)]
print(result)
#52. Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green","blue"]
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
print(f"52) Sample data: (1) {color1}")
print(f"                 (2) {color2}")
diff1 = list(set(color1) - set(color2))   # có trong color1 nhưng ko có trong color2
diff2 = list(set(color2) - set(color1))   # có trong color2 nhưng ko có trong color1
print("Color1 - Color2:", diff1)
print("Color2 - Color1:", diff2)