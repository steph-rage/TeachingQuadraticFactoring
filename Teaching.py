from flask import Flask, render_template
factorteacher = Flask(__name__)

@factorteacher.route('/factorteacher/')
def load_start(name=None):
    return render_template('StartPage.html')

@factorteacher.route('/factorteacher/what/')
def load_what(name=None):
    return render_template('HowtoWhataWhat.html')

@factorteacher.route('/factorteacher/what/factornumbers')
def load_numbers_examples(name=None):
    return render_template('FactorNumbersExamples.html')

