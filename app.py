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


@app.route("/git-update", methods=["POST"])
def git_update():
    path = pathlib.Path(__file__).parent.resolve()
    repo = git.Repo(path)
    origin = repo.remotes.origin
    repo.create_head("master", origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return "Pulled Code", 200