from flask import Flask, render_template, current_app as app

app = Flask(__name__)


@app.route('/')
def index():
	return 'Welcome to Kathrin\'s Rainbow Project'

@app.route('/red')
def red_html():
    return render_template('red.html')

@app.route('/orange')
def orange_html():
    return render_template('orange.html')

@app.route('/yellow')
def yellow_html():
    return render_template('yellow.html')

@app.route('/green')
def green_html():
    return render_template('green.html')

@app.route('/blue')
def blue_html():
    return render_template('blue.html')

@app.route('/indigo')
def indigo_html():
    return render_template('indigo.html')

@app.route('/violet')
def violet_html():
    return render_template('violet.html')

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')
