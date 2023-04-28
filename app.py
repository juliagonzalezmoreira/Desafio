from flask import Flask, url_for, render_template
""" from flask_mysqldb import MySQL """

app = Flask(__name__)

""" app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ju070205'
app.config['MYSQL_DB'] = 'contatos' """

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

