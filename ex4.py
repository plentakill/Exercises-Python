#EX4.1
num = 458.541315
print('%.2f' % num)

#EX4.2
numbers = []
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)