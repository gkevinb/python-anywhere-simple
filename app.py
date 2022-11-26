from flask import Flask
import git
import pathlib

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    return "<p>Testing new route endpoint!</p>"


@app.route("/new")
def new():
    return "<p>New endpoint to test out automated deployement</p>"

@app.route("/change")
def change():
    return "<p>chagnge this endopint</p>"

@app.route("/git-update", methods=["POST"])
def git_update():
    path = pathlib.Path(__file__).parent.resolve()
    repo = git.Repo(path)
    repo.remotes.origin.pull()
    return "Pulled Code", 200