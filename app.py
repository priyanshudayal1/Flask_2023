from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
def hell():
    return "<h1>HEllo World written from python</h1>"

@app.route("/web")
def hell2():
    return render_template("Navbar.html")

if __name__=="__main__":
    app.run()