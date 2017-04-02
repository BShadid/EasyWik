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

if __name__ == "__main__":
    context = ('yourserver.crt','yourserver.key')
    app.run(host='0.0.0.0',port='5000',ssl_context=context)
