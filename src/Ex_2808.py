# Write python program:
# a) Convert two lists into a dictionary
keys = ["id","name","age"]
values = ["456212","than thi det","20"]
emp = dict(zip(keys,values))
print(f"a) {emp}")
# b) Merge two Python dictionaries into one
dict1 = {"a":1 ,"b":2}
dict2 = {"c":3, "d":4}
merge = dict1 | dict2
print(f"b) {merge}")
# c) Print the value of key ‘history’ from the below dict
dict3 = {
    'math': 80,
    'science': 90,
    'history': 75,
    'english': 85
}
print("c) Value of 'history':", dict3.get('history'))
# d) Initialize dictionary with default values
default_dict = {key: 0 for key in ["a","b","c"]}
print("d) Initialized Dictionary with default values:", default_dict)
# e) Create a dictionary by extracting the keys from a given dictionary
new_dict = {key: dict3[key] for key in ['math', 'english']}
print("e) Extracted Dictionary:", new_dict)
# f) Delete a list of keys from a dictionary
keys_to_delete = ['math', 'science']
for key in keys_to_delete:
    dict3.pop(key, None)
print("f) Dictionary after deleting keys:", dict3)
# g) Check if a value exists in a dictionary
value_to_check = 75
print("g) Value exists:", any(val == value_to_check for val in dict3.values()))
# h) Rename key of a dictionary
if 'history' in dict3:
    dict3['social_studies'] = dict3.pop('history')
print("h) Renamed Dictionary:", dict3)
# i) Get the key of a minimum value from the following dictionary
min_key = min(dict3, key=dict3.get)
print("i) Key of minimum value:", min_key)
# j) Change value of a key in a nested dictionary
nested_dict = {'subject': {'math': 90, 'science': 95}, 'teacher': 'Mr. X'}
nested_dict['subject']['math'] = 85
print("j) Updated Nested Dictionary:", nested_dict)
# 2. Write a Python program that counts the number of times characters appear in a text paragraph.
s = ("Write a Python program that counts the number of times characters appear in a text paragraph")
stats = {}
for c in s:
    x = stats.get(c)
    if x is None:
        stats[c] = 1
    else:
        stats[c] = int(stats[c]) +1
print(stats)
# 3. Write a program using a dictionary containing keys starting from 1 and values containing prime numbers less than a value N.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_dict(N):
    primes = [i for i in range(1, N) if is_prime(i)]
    prime_dict = {i+1: primes[i] for i in range(len(primes))}
    return prime_dict
N = 30  # Example value for N
print("3) Dictionary with prime numbers less than", N, ":", prime_dict(N))
# Bài 2:
# Restructuring the company data: Suppose you have a dictionary that contains information about employees at a company. Each employee is identified by an ID number,
# and their information includes their name, department, and salary. You want to create
# a nested dictionary that groups employees by department so that you can easily see the names and salaries of all employees in each department.
# Write a Python program that when given a dictionary, employees, outputs a nested dictionary, dept_employees, which groups employees by department.
employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}
dept_employees = {}
for emp_id, info in employees.items():
    dept = info["department"]
    if dept not in dept_employees:
        dept_employees[dept] = {}
    dept_employees[dept][emp_id] = {
        "name": info["name"],
        "salary": info["salary"]
    }
print(dept_employees)
