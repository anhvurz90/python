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
	}
}


