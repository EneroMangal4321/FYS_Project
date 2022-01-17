from crypt import methods
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'enero'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'fys'

mysql = MySQL(app)

@app.route('/')
def test():
    cur = mysql.connection.cursor()
    cur.execute("SELECT voornaam FROM Klanten WHERE id = 1")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("test.html", fname = fetchdata)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        achternaam = request.form['sname']
        ticketnr = request.form['ticketnr']

        print(">>", str(achternaam))
        # get id of costumer using email name as citeria from db.
        cur = mysql.connection.cursor()
        cur.execute("""SELECT id FROM Klanten WHERE achternaam = %s""" % (str(achternaam)))
        klant_id_Klanten = cur.fetchall()
        cur.close()

        # get klantid from db using ticketnumber as criteria.
        cur = mysql.connection.cursor()
        cur.execute("""SELECT klantid FROM Ticket WHERE id = %s""" % (int(ticketnr)))
        klant_id_Ticket = cur.fetchall()
        cur.close()

        # check if the klantid is the same as the id of the Klanten table.
        if klant_id_Klanten == klant_id_Ticket:
            cur = mysql.connection.cursor()
            cur.execute("""SELECT voornaam FROM Klanten WHERE id = %s""" % (int(klant_id_Ticket)))
            fname = cur.fetchall()
            cur.close()
            return render_template("test.html", fname = fname)
        
        else:
            print("Incorrecte naam of ticketnummer")
            return  render_template("login-test.html")
    
    return  render_template("login-test.html")


if __name__=="__main__":
    app.run(debug=True)