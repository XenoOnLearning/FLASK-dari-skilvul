from flask import Flask

app = Flask(__name__)

@app.route('/')
def entry_point():
    return "Index page"

@app.route("/hello")
def hello():
    return "Halooooo"

@app.route("/login", methods= ["GET", "POST"])
def login():
    if request.method == "POST":
        return "Ga bisa"()
    else:
        return "Eh malah tambah gabisa"()
@app.route("/sensor/data", methods="POST")
def sensor():
    return {
        "temperature": 30,
        "kelembapan": 1,
        "timestamp":"09:09:30"
    }
if __name__ == '__main__':
    app.run(debug=True)