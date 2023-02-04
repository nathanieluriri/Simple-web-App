from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html") 

@app.route('/home')
def newpage():
    return render_template('home.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/Myresume')
def resumepage():
    return render_template('Myresume.html')

@app.route('/contact')
def contactpage():
    return render_template('contact.html')

@app.route('/profile')
def profilepage():
    return render_template('profile.html')
if __name__ == "__main__":
    
    app.run(debug=True, port = '5001')