from flask import Flask, url_for, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ju070205'
app.config['MYSQL_DB'] = 'desafio3'

mysql = MySQL(app)

@app.route('/desafio3', methods=['GET', 'POST'])
def desafio3():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contatos(email, assunto, descricao) VALUES(%s, %s, %s)', (email, assunto, descricao))
        
        mysql.connection.commit()
        
        cur.close()
        
        return 'sucesso'
    return render_template('contatos.html')   

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

