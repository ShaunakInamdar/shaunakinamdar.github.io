from flask import Flask, render_template,redirect

app = Flask(__name__, template_folder="templates", static_folder = "static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return redirect("https://shaunak-inamdar.medium.com/")

if __name__ == "__main__":
    app.run()