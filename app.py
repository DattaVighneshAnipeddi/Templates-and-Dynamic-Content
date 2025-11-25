from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    username = "Dattu"
    skills = ["Python", "Flask", "HTML", "CSS"]
    # Passing data to the template
    return render_template("home.html", username=username, skills=skills)

@app.route("/about")
def about():
    # Passing dynamic data to 'about.html'
    return render_template("about.html", version="1.0.0")

if __name__ == "__main__":
    app.run(debug=True)
