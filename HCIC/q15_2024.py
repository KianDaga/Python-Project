num_list = [1, 2, 3, 4, 5]
new_list = []
for num in num_list:
        if num % 2 == 0:
            new_list.append(num * 2)
        else:
            new_list.append(num + 2)
print(new_list)
