# 1
print([17, "Pizza", 6.5])

#2
# nested_list = [1,1[1,2]]
# print(nested_list) would lead to an error. The nested list elements cannot be accessed as stated in the problem.
# nested_list = [1, 1, [1, 2]] could be accessed with:
print("nested_list[2][1]")

#3
lst = ['a', 'b', 'c']
print(lst[1:])

#4
weekdays = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}

#5
D = {'k1': [1,2,3]}
# print(d[k1][1]) will cause an error, dictionary names are case-sensitive so 'd' is undefined

#6
lst = [1, [2,3]]
new_tuple = tuple(lst)
print(new_tuple)

#7
unique_MI = set("Mississippi") 
print(unique_MI)

#8
unique_MI.add('X')
print(unique_MI)

#9
print(set([1,1,2,3]))

#10
ans = ''
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        ans += str(num)
        ans += ","
print(ans[:-1])