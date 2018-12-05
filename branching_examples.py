def example_1():
	day = 'Tuesday'
	if day == 'Saturday' or day == 'Sunday':
		print('Today is a weekend!')
	else:
	    if day == 'Monday' or day == 'Friday':
	        print('Lecture is in A250')
	    else:
	        print('Yay! Lecture is in Weill')

def example_2():
	n = 0
	while n < 3:
		print("Hi!")
		n += 1

def example_3():
	for n in range(2, 5):
		if n < 3:
			print('Too small!')
		else: 
			print('Too big!')

def example_4():
	days = ['Monday', 'Tuesday']
	for day in days:
		print(day)

def main():
	pass

if __name__ == "__main__":
	main()