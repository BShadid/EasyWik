from flask import Flask
import easyWik

app = Flask(__name__)

@app.route('/')
def usage():
    return "something went wrong."

@app.route('/<title>')
def simplify(title):
    # do some magic
    return easyWik.run_main(title)
    # return title
