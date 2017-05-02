Try Python: https://www.codeschool.com/courses/try-python

Level 1: Bird & Coconuts: {
	1.Python Math: {
		1.1.Video-Python Math: {
			- Why Python? {
				+ Easy to learn
				+ Easy to read
				+ Fast
				+ Versatile
				+ Many libraries: Draw, Math, Game
			}
			- The Python Interpreter: {
				>>> 35
				35
				>>> 30.5
				30.5
				>>> 30 + 5
				35
			}
			- Mathematical Operators: {
				addition:		>>> 3 + 5
				subtraction:	>>> 10 - 5
				multiplication:>>> 3 * 5
				division:		>>> 30 / 6
				exponent:	>>> 2 ** 3
				negation:	>>> -2 + -3
			}
			- Integers and Floats: {
				int: 35
				float: 30.5
			}
			- Order of Operations: {
				PEMDAS:
					Parentheses, Exponent, Multiplication
					Division, Addition, Subtraction
			}
			- Can a Swallow Carry a Coconut?: {
				>>> 1450 / (60 / 3)
			}
		}
		1.2.Happy Birthday: {
			>>> 2017 - 1984
		}
		1.3.Your Age in Dog Years: {
			>>> 33/7
		}
		1.4.Calculating British Money Spent: {
			>>> 200 * 0.65
			>>> (200 - 2) * 0.65
			>>> (200 - 2) * 0.65 - 100
		}
	}
	2.Using Variables: {
		1.5.Using Variables: {
			- Swallows per coconut: 1450 / ( 60 / 3 )
			- Swallows per apple: 128 / ( 60 / 3 )
			- Swallows per cherry: 8 / ( 60 / 3 )
			>>> swallow_limit = 60 / 3
			>>> swallow_per_cherry = 8 / swallow_limit
			- Pep 8 Style Guide recommends: swallow_limit
			- Import Modules - Extra Functionality: {
				import math
				num_macaws = 4.8
				math.ceil(num_macaws)
				Python libraries:
					http://go.codeschool.com/python-libraries
			}
		}
		1.6.Naming Variables
		1.7.Variable Calculations
		1.8.Exchange Rate Calculations: {
			>>> x_rate = 0.65
			>>> total_dollars = 200
			>>> fee = 2
			>>> total_pounds = (total_dollars - fee) * x_rate
		}
		1.9.ExchangeRateCalculations2: {
			>>> total_dollars = total_pounds / x_rate - fee
			>>> import math
			>>> math.floor(total_dollars)
		}
	}
}
Level 2: Spam & Strings: {
	1.Introduction to Strings: { 
		2.1.Introduction to Strings: {
			>>> 'Hello World!'
			>>> "SPAM83"
			
			>>> first_name = 'Monty'
			>>> last_name = 'Python'
			>>> full_name = first_name + last_name
			>>> full_name = first_name + ' ' + last_name
			
			- Moving Our Code to a Script File: script.py:
				+ print(full_name)
				+ print(first_name, last_name)
				
			>>> python script.py
			
			- Comments: #:
				# Describe the sketch comedy group
				name = 'Monty Python'
				description = 'sketch comedy group'
				year = 1969
				# Introduce them
				sentence = name + ' is a ' + description + ' formed in ' + str(year) 
				print(name, 'is a', description, 'formed in', year)
			
			- Dealing With Quotes in Strings:
				famous_sketch = "Hell's Grannies"
				
			- Special Characters: Tab
				# Describe Monty Python's work
				famous_sketch1 = "\n\tHell's Grannies"
				famous_sketch2 = "\n\tThe Dead Parrot"
				print('Famous Work:', famous_sketch1, famous_sketch2)
		}
		2.2.Print Output:
		2.3.String Concatenation: {
			greeting = "G'day" + ' ' + "mate"
		}
		2.4.Cast Number to String:
		2.5.Getting Started With Python Strings
		2.6.String Formatting:
	}
	2.Strings and Slices: {
		2.7.Strings and Slices: {
			- Strings Behind the Scenes - a List of Characters:
				+ A string is a list of characters, and each character 
				in this list has a position or an index
			- String Built-in Functions:
				+ len(): 
					greeting = 'Hello World!'
					print( len(greeting))
			- Using Slices to Access Parts of a String
				word = 'Python'
				word[2:5] ---> 'tho'
				word[:2] === word[0:2]
				word[2:] === word[2:len(word)]
			
			- 2 division signs ~ integer division
				word1 = 'Good'
				half1 = len(word1) // 2
				end1 = word1[half1:]
				
				word2 = 'Evening'
				half2 = len(word2) // 2
				end2 = word2[half2:]
				
				print(end1, end2)
		}
		2.8.Slicing to Create a Substring:
		2.9.Pythonese: {
			word = 'Python'
			first = word[0]
			rest = word[1:]
			result = rest + '-' + first + 'y'
			print(result)
		}
	}
}
Level 3: Conditional Rules of Engagement: {
	1.Introduction to Conditionals: {
		3.1.Introduction to Conditionals: {
			Conditionals & Input
			Extended Battle Rules
			Comparision Operators:
				6 comparators: <, <=, ==, >=, >, !=
			Comparision Operator Outputs:
			Booleans: True, Flalse
			Conditional - if, then
				num_knights = 2;
				if num_knights < 3:
					print('Retreat!')
					print('Raise the white flag!')
				else:
					print('True?')
				print('Knights of the Rould Table')
			Rules for Whitespace in Python:
				In Python, indent with 4 spaces.
		}
	}
	2.More Conditionals: {
		3.5.More Conditionals: {
			- if num_knights < 3:
				print('Retreat!')
			elif num_knights >= 10:
				print('Trojan Rabbit')
			elif day == 'Tuesday':
				print('Taco Night')
			else:
				print('Truce?')
				
			- if num_knights < 3 or day == 'Monday':
				print('Retreat!')

			- if num_knights >= 10 and day == 'Wednesday':
				print('Trojan Rabbit!')
				
			- summary:
				# Battle Rules
				num_knights = 10
				day = 'Wednesday'
				
				if num_knights < 3 or day == 'Monday':
					print('Retreat!')
				elif num_knights >= 10 and day == 'Wednesday':
					print('Trojan Rabbit!')
				else:
					print('Truce?')
			
			- User Input - With the input() Function
				# Ask the user to input the day of week
				day = input('Enter the day of the week')
				print('You entered: ', day)
				
				num_knights = int(input('Enter the number of knights'))

			- Nested Conditionals:
				num_knights = int(input('Enter number of knights'))
				day = input('Enter day of the week')
				enemy = input('Enter type of enemy')
				
				if enemy == 'killer bunny':
					print('Holy Hand Grenade!')
				else:
					# Original battle Rules
					if num_knights < 3 or day == 'Monday':
						print('Retreat!')
					if num_knights >= 10 and day == 'Wednesday':
						print('Trojan Rabbit!')
					else:
						print('Truce!')
		}
	}
}
Wrapup Video: {
	https://www.codeschool.com/courses/flying-through-python
	https://app.pluralsight.com/library/search
	https://docs.python.org/3/tutorial/index.html
	www.pythontutor.com
	https://automatetheboringstuff.com
}