#WHILE LOOP--------------------------------------
print('WHILE LOOP')
count = 0
while (count < 9):
	print('The count is:', count)
	count+= 1
print('Good bye!')
#--------------------------------------
#var = 1
#while var == 1:
#	num = int(input("Enter a number: "))
#	print("You entered: ", num)
#print('Good bye!')
#--------------------------------------
count = 0
while count< 5:
	print (count, "is less than 5")
	count+= 1
else:
	print (count, "is not less than 5")

#FOR LOOP--------------------------------------
print()
print('FOR LOOP:')
for var in list(range(5)):
	print(var)
#--------------------------------------
for letter in 'Python':
	print('Current Letter :', letter)
#--------------------------------------
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
	print('Current fruit :', fruit)
#--------------------------------------
for index in range(len(fruits)):
	print('Current fruit with index: ', fruits[index])
#--------------------------------------
numbers = [1, 3, 5, 2, 7, 9, 11]
for num in numbers:
	if num %2 == 0:
		print('The list contains an even number')
		break
else:
	print('The list does not contain even number')
#--------------------------------------
#--------------------------------------
#--------------------------------------
#--------------------------------------
#--------------------------------------
#--------------------------------------