from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/about')
def about():
    return render_template("about.html")

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

# @app.route('/about', strict_slashes=False)
# def about():
#     return render_template("about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)