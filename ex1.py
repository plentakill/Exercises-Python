#EX1.1
inputstr = input("Enter a string: ")

counter = 0 
for s in inputstr : 
      counter = counter + 1 
print ( "Length of string:" , counter )


#EX1.2
def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

my_list = [1,3,5,2,5]
print("The sum of my_list is", sum_of_list(my_list))

#EX1.3
list1 = [10, 20, 4, 45, 9]
print("Largest element is:", max(list1))
    
#Alternate 1.3
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest element is:", list1[-1])