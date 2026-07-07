t = (1, 2, 3)
# t[0] = 99   # this gives ERROR

s = "hello"
# s[0] = "H"  # this gives ERROR

# MUTABLE - can change
my_list = [1, 2, 3]
my_list[0] = 99
print(my_list)   # [99, 2, 3]

my_dict = {"name": "Ram", "age": 20}
my_dict["age"] = 21
print(my_dict)   # {'name': 'Ram', 'age': 21