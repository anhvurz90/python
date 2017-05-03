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
	}
}