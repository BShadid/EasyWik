from flask import Flask

easyWik = Flask(__name__)

@easyWik.route('/')
def usage():
    return "something went wrong."

@easyWik.route('/<title>')
def simplify(title):
    # do some magic
    return title
