#!user/bin/python

from flask import Flask, render_template
from random import randint

factorteacher = Flask(__name__)


@factorteacher.route('/factorteacher/')
def load_start():
	return render_template('StartPage.html')

@factorteacher.route('/factorteacher/what/')
def load_what():
    return render_template('HowtoWhataWhat.html')

@factorteacher.route('/factorteacher/what/factornumbers')
def load_numbers_examples():
	number_to_factor = 8
	number_of_pairs = 2
	return render_template('FactorNumbers.html', number_to_factor=number_to_factor, number_of_pairs=number_of_pairs)

