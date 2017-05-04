PYTHON3:
09.Loops: {
	09.01.Loop Types: {
		09.01.01.While loop: {
			- Syntax: {
				while expression:
					statement(s)
			}
			- Example: {
				count = 0
				while (count < 9):
					print ('The count is:', count)
					count+= 1
					
				print ('Good bye!');
			}
			- The Infinite Loop: {
				var = 1
				while var == 1:
					num = int(input("Enter a number :"))
					print("You entered: ", num)
				print("Good bye!")
			}
			- Using else Statement with Loops: {
				count = 0;
				while count < 5:
					print(count, "is less than 5")
					count+= 1
				else:
					print (count, "is not less than 5")
			}
		}
		09.01.02.Foor loop: {
			- Syntax: {
				for iterating_var in sequence:
					statements(s)
			}
			- The range() function: {
				+ Example:
					>>> range(5)
					range(0, 5)
					>>> list(range(5))
					[0, 1, 2, 3, 4]
					>>> for var in list(range(5)):
						print(var)
					0
					1
					2
					3
					4
			}
			- Example: {
				for letter in 'Python':	# traversal of a string sequence
					print('Current Letter:', letter)
				print()
				fruits = ['banana', 'apple', 'mango']
				for fruit in fruits:	# traversal of List sequence
					print('Current fruit :', fruit)
				print('Good bye!')
			}
			- Iterating by Sequence Index: {
				fruits = ['banana', 'apple', 'mango']
				for index in range(len(fruits)):
					print('Current fruit :', fruits[index])
				print('Good bye')
			}
			- Using else Statement with Loops: {
				numbers = [11, 33, 55, 39, 75]
				for num in numbers:
					if num % 2 == 0:
						print('The list contains an even number')
						break
				else:
					print('The list does not contain even number')
			}
		}
	}
}