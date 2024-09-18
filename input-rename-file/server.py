from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def input():
    return render_template('input.html')

@app.route('/output', methods=['GET', 'POST'])
def output():
    return render_template('output.html', file=request.form['file'], text=request.form['text'])

if __name__ == "__main__":
    app.run()