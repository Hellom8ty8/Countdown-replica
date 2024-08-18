import threading, time, random
from PyDictionary import PyDictionary

global points
points = int(0)


def getinput():
	global cons
	cons = input()

	# thread for getting the letters round input


def getinput_conundrum():
	global conundrum_input
	conundrum_input = input()
	conundrum_input.upper()

	# thread for getting the conundrum input


def getinput_nums():
	global nums
	nums = 0
	condition = True
	while condition:
		try:
			nums = int(input())
			condition = False
		except:
			print('that is not a valid input. \n')

			# thread for getting the numbers round input


def clock_num():
	clock = 65
	print("60")
	while clock > 0:
		clock -= 1
		time.sleep(1)
		if clock == 35:
			print("30")
		elif clock == 5:
			print("5")
		if nums != 0:
			clock = 0
		elif clock == 0 and nums == 0:
			nums == -1

			# thread for the numbers round clock


def clock():
	global cons
	cons = ""
	clock = 65
	print("60")
	while clock > 0:
		clock -= 1
		time.sleep(1)
		if clock == 35:
			print("30")
		elif clock == 5:
			print("5")
		if cons != "":
			clock = 0


#
#								# thread for the letters round clock


def clock_final():
	global cons
	clock = 65
	print("60")
	while clock > 0:
		clock -= 1
		time.sleep(1)
		if clock == 35:
			print("30")
		elif clock == 5:
			print("5")
		if cons != "":
			clock = 0


#
#						# thread for the conundrum clock


def letters_rounds():

	vowles = ['a', 'e', 'i', 'o', 'u']
	constanants = [
	 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'f', 'f', 'g', 'g', 'h', 'h', 'j',
	 'k', 'l', 'l', 'l', 'm', 'm', 'm', 'n', 'n', 'n', 'p', 'p', 'p', 'q', 'r',
	 'r', 'r', 's', 's', 't', 't', 't', 'v', 'w', 'w', 'x', 'x', 'y', 'y', 'z'
	]
	final_list = []
	condition = True
	count = -1
	print("Letters round: \n ")
	while condition:
		try:
			num_constanants = int(input("how many constanants do you want: \n"))

			if num_constanants > 8 or num_constanants < 5:
				print("you need between 5 and 8 constanants")

			else:
				condition = False
		except:
			print("that is not a number, please input a number")

	condition = True
	num_vowles = 9 - num_constanants

	for i in range(num_vowles):
		final_list.append(random.choice(vowles))

	for i in range(num_constanants):
		final_list.append(random.choice(constanants))

	print(final_list)
	gameThread = threading.Thread(target=getinput)
	gameThread.start()
	clockThread = threading.Thread(target=clock())
	clockThread.start()

	dictionary = PyDictionary(cons)

	try:
		dictionary.getMeanings()
		for i in range(len(cons)):
			if condition == True:
				if cons[i] not in final_list:
					condition = False
					count = 1
				else:
					count = 0

	except:
		count = -2

	if count == 1:
		print('you cant make that word out of the given characters \n \n')
	elif cons == "eli":
		print("you found the easter egg, thanks for playing!!!")
	elif count == -1:
		print('you did not input a word \n \n')

	elif count == -2:
		print("that is no a word \n \n")

	else:
		print("correct, You got", len(cons), "points \n \n")
		return points

		# defining the letters round


def numbers_round():

	global nums
	condition = True
	small_nums = [
	 '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5',
	 '6', '7', '8', '9', '10'
	]
	ev = ''
	large_numbers = ['25', '50', '75', '100']
	final_list = []

	target_number = int(random.randint(150, 999))
	random.shuffle(large_numbers)
	random.shuffle(small_nums)

	print("numbers round: \n")

	while condition:
		try:
			smalls = int(input("how many small numbers do you want?: \n"))
			if smalls < 2 or smalls > 6:
				print("you need to pick between 2 and 6 small numbers. \n")
			else:
				condition = False
		except:
			print("that is not a number, please input a number")

	larges = 6 - smalls

	for i in range(smalls):
		final_list.append(small_nums[i])

	for i in range(larges):
		final_list.append(large_numbers[i])

	print("find", target_number, "from", final_list)

	gameThread = threading.Thread(target=getinput_nums)
	gameThread.start()
	clockThread = threading.Thread(target=clock_num())
	clockThread.start()

	solution = input('what is your solution (press enter when complete) \n \n')
	if nums != -1:
		while solution != '':
			solution = input('what is your solution \n \n')
			ev = solution
			if solution == '':
				break
		print(eval(ev))
		print(ev)


	if ev == nums:
		if nums == -1:
			print("you didn't input anything")
		elif nums == target_number:
			print("spot on, you got 8 points \n")
			return (points + 8)

		elif nums in range(target_number - 3, nums <= target_number + 3):
			print("close, you got 4 points \n")
			return (points + 4)

		elif nums in range(target_number - 5, nums < target_number + 5):
			print("just close enough, you got 2 points \n")
			return (points + 2)

		elif nums != int():
			print("that isn't a number")

		elif nums == float():
			print('you can not input a float')

		else:
			print("you where to far away, you got no points \n")
	else:
		print('your equation doesnt match your awnser')
	final_list = []

	# defining the numbers round


def conundrum():
	conundrum_list = [('TYRMANOME', 'MOMENTARY'), ('PGIGAPNLR', 'GRAPPLING'),
					  ('SLRMKHAAL', 'HALLMARKS'), ('RAIWDHOKN', 'HANDIWORK'),
					  ('VEEEGERRN', 'EVERGREEN'), ('IENIDISTG', 'DIGNITIES'),
					  ('ESSEOTMCY', 'ECOSYSTEM'), ('NTIIBDHIE', 'INHIBITED'),
					  ('DEIUSDNSM', 'MUDDINESS'), ('TNHGLSISO', 'SLINGSHOT'),
					  ('CDTNOUSIS', 'DISCOUNTS'), ('EIASENXTI', 'ANXIETIES'),
					  ('FODATRRVE', 'OVERDRAFT'), ('AECLESCPT', 'SPECTACLE'),
					  ('MYRSDADAE', 'DAYDREAMS'), ('TLROCOISI', 'SOLICITOR'),
					  ('IOGWRRNHA', 'HARROWING'), ('NEWVERTII', 'INTERVIEW'),
					  ('LADEYMSHA', 'ASHAMEDLY'), ('TEEUARCRS', 'CREATURES')]
	random.shuffle(conundrum.list)
	print('your conundrum is, ', conundrum_list[0][0])

	gameThread = threading.Thread(target=getinput_conundrum)
	gameThread.start()
	clockThread = threading.Thread(target=clock_final())
	clockThread.start()

	if cons == conundrum_list[0][1]:
		print("correct, you get 9 points")
		return (points + 9)
	else:
		print("Wrong, the conundrum awnser is, ", conundrum_list[0][1])

		# defining the conundrum


for i in range(3):
	# points = letters_rounds()
	# points = letters_rounds()
	# points = letters_rounds()
	points = numbers_round()
	if i == 3:
		conundrum()
	elif i != 3:
		time.sleep(3)
		print("you have ", points, " points")
		time.sleep(3)
		# activation code

time.sleep(5)  # final points tally
print("you got ", points, " points")
