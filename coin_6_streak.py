import random

number_of_streaks = 0

for experiment_no in range(1):
	th_list = []
	for i in range(100):
		t_or_h = random.randint(0,1)
		if t_or_h == 0:
			th_list.append('T')
		else:
			th_list.append('H')

	streak6_t, streak6_h = [], []

	for c in th_list:
		if len(streak6_t) == 6:
			streak6_t = []
			number_of_streaks += 1
		if len(streak6_h) == 6:
			streak6_h = []
			number_of_streaks += 1
		if c == 'T':
			streak6_t.append(c)
		if c == 'H':
			streak6_h.append(c)

print('Chance of streak: %s%%' % (number_of_streaks / 100))

