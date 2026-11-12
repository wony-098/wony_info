from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/next')
def next_page2():
    return render_template('page2.html')

@app.route('/next4')
def next_page3():
    return render_template('page3.html')

@app.route('/next8')
def next_page4():
    return render_template('page4.html')

@app.route('/next9')
def back_to_page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)