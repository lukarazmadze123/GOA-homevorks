from flask import flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Website</h1><p>This website covers various themes!</p>"


@app.route('/football')
def football():
    return render_template('football.html')

 
@app.route('/movie')
def movie():
    return render_template('movie.html')

# 3. ვებსაიტი ზღვის გოჭებზე
@app.route('/guinea_pigs')
def guinea_pigs():
    return render_template('guinea_pigs.html')


@app.route('/apple')
def apple():
    return render_template('apple.html')


@app.route('/samsung')
def samsung():
    return render_template('samsung.html')

if __name__ == '__main__':
    app.run(debug=True)