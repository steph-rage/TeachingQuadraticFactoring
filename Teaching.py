#!user/bin/python

from flask import Flask, render_template, request
from random import randint

factorteacher = Flask(__name__)


def find_factors(n):
	factors = []
	factor_pairs = []
	max = int(n**(1.0/2.0)) + 1
	for test in range(1, max+1):
		if n%test == 0:
			if test not in factors:
				factor_pairs.append([test, n/test])
				factors.append(test)
				factors.append(n/test)
	return factor_pairs

@factorteacher.route('/factorteacher/')
def load_start():
	return render_template('StartPage.html')

@factorteacher.route('/factorteacher/what/')
def load_what():
    return render_template('HowtoWhataWhat.html')

@factorteacher.route('/factorteacher/what/factornumbers', methods = ['GET', 'POST'])
def load_numbers_examples():
	if request.method == 'POST':
		number = int(request.form['number'])
		factor_pairs = find_factors(number)
		entered_factor_pairs = []
		for i in range(len(factor_pairs)):
			ith_pair = [int(request.form['factor' + str(i) + '.1']), int(request.form['factor' + str(i) + '.2'])]
			ith_pair.sort()
			entered_factor_pairs.append(ith_pair)
		factor_pairs.sort()
		entered_factor_pairs.sort()
		if entered_factor_pairs == factor_pairs:
			print "Great job!"
		else:
			print "You suck"
	number_to_factor = randint(2, 40)
	number_of_pairs = len(find_factors(number_to_factor))
	return render_template('FactorNumbers.html', number_to_factor=number_to_factor, number_of_pairs=number_of_pairs)

