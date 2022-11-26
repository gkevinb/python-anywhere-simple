from flask import Flask
import git

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    return "<p>Testing new route endpoint!</p>"


@app.route("/git-update", methods=["POST"])
def git_update():
    repo = git.Repo("./python-anywhere-simple")
    origin = repo.remotes.origin
    repo.create_head("master", origin.refs.main).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return "Pulled Code", 200