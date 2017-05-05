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
		09.01.03.Nested loop: {
			- Syntax: {
				+ for iterating_var1 in sequence1:
					for iterating_var2 in sequence2:
						statements(s)
					statements(s)
					
				+ while expression1:
					while expression2:
						statements(s)
					statements(s)
			}
			- Example: {
				import sys
				for i in range(1, 11):
					for j in range(1, 11):
						k = i * j
						print(k, end=' ')
					print()
			}
		}
	}
	09.02.Loop Control Statements: {
		09.02.01.Break Statement: {
			- for letter in 'Python':	# First Example
				if letter == 'h':
					break
				print('Current Letter :', letter)
			
			- var = 10
			while var > 0:
				print('Current variable value :', var)
				var-= 1
				if var == 5:
					break
			print('Good bye!')
		}
		09.02.02.Continue Statement: {
			- for letter in 'Python':
				if (letter == 'h'):
					continue
				print('Current letter :', letter)
				
			- var = 5
			while (var > 0):
				var -= 1
				if (var == 3):
					continue
				print('Current variable value: ', var)
			print('Good bye!')
		}
		09.02.03.Pass Statement: {
			- Just like a placeholder
			- Syntax:
				pass
			- Example:
				for letter in 'Python':
					if (letter == 'h'):
						pass
						print('This is pass block')
					print('Current letter :', letter)
				print('Good bye!')
		}
	}
	09.03.Iterator and Generator: {
		09.03.01.Iterator: {
			- Implement 2 methods: iter() & next()
			- String, List, Tuple can be used to create an Iterator
			
			- Example:
			list = [1, 2, 3, 4]
			it = iter(list)		# this builds an iterator object
			print (next(it))	# prints the next available element in iterator
			
			for x in it:
				print(x, end=' ')
			print()
				
			or
			
			while True:
				try:
					print (next(it))
				except StopIteration:
					sys.exit()
			
		}
		09.03.02.Generator: {
			- Is a function that produces or yields a sequence of values using yield method
			When the next() method is called on the generator,
			it executes until meeting 'yield'.
			
			import sys
			def fibonacci(n):		# generator function
				a, b, counter = 0, 1, 0
				while True:
					if (counter > n):
						return
					yield a
					a, b = b, a + b
					counter += 1
			
			f = fibonacci(5)
			
			while True:
				try:
					print (next(f), end=' ')
				except StopIteration:
					sys.exit()
		}
	}
}