from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/second')
def second():
    return 'this is my second page'
if __name__ == '__main__':
    app.run(debug=True)