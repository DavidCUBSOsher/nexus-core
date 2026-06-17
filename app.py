from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Nexus Core</h1><p>Sistema operativo. David Cubero - v1.0</p>"

@app.route("/salud")
def salud():
    return {"status": "ok", "sistema": "Nexus Core", "version": "1.0"}

if __name__ == "__main__":
    app.run(debug=True)
