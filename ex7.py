#EX7.1
list = [['Lion','Deer','Sheep'],['Cub','Fawn','Lamb']]
for i in list:
    print(i)

#EX7.2
name=input('What is your name: ')
for x in range((len(name))):
    for x in range(3):
        print(name+" ",end=" ")
    print()