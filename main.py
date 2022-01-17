from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

#Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'enero'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'fys'

mysql = MySQL(app)

# @app.route('/', methods=['GET', 'POST'])
# def home_pagina():
#     error = None
#     if request.method == 'POST':
#         if request.form['Surname'] != 'admin' or request.form['Ticketnumber'] != 'admin':
#             error = 'Invalid Surname and/or Ticketnumber, try again.'
#         else:
#             return {{url_for('wifi_verbinding')}}
#     return render_template('/index.html', error=error)

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        ticketnr = request.form['ticketnr']

        email = f"'{email}'"
        # get id of costumer using email name as citeria from db.
        cur = mysql.connection.cursor()
        cur.execute("""SELECT id FROM Klanten WHERE email = %s""" % (str(email)))
        klant_id_Klanten = cur.fetchall()
        cur.close()

        # get klantid from db using ticketnumber as criteria.
        cur = mysql.connection.cursor()
        cur.execute("""SELECT klantid FROM Ticket WHERE id = %s""" % (int(ticketnr)))
        klant_id_Ticket = cur.fetchall()
        cur.close()

        try:
            # check if the klantid is the same as the id of the Klanten table.
            if klant_id_Klanten == klant_id_Ticket:
                # print(">", type(klant_id_Ticket))
                # print(klant_id_Ticket[0][0])
                klant_id_Ticket = int(klant_id_Ticket[0][0])
                cur = mysql.connection.cursor()
                cur.execute("""SELECT voornaam FROM Klanten WHERE id = %s""" % (int(klant_id_Ticket)))
                fname = cur.fetchall()
                cur.close()
                return render_template("WiFi_verbinding.html", fname = fname[0][0])
        except Exception as identifier:
            error = "Incorrecte naam of ticketnummer"
            return  render_template("index.html", error = error)
        
        else:
            print("Incorrecte naam of ticketnummer")
            return  render_template("index.html")
    
    return  render_template("index.html")


@app.route('/WiFi_verbinding.html', methods=['GET', 'POST'])
def wifi_verbinding():
    return render_template("/WiFi_verbinding.html")


@app.route('/Entertainment_pagina1.html', methods=['GET', 'POST'])
def entertainment_1():
    return render_template("Entertainment_pagina1.html")


@app.route('/Zoek_de_verschillen_oplossing.html', methods=['GET', 'POST'])
def oplossing_1():
    return render_template("Zoek_de_verschillen_oplossing.html")


@app.route('/Entertainment_pagina2.html', methods=['GET', 'POST'])
def entertainment_2():
    return render_template("Entertainment_pagina2.html")


@app.route('/Entertainment_pagina3.html', methods=['GET', 'POST'])
def entertainment_3():
    return render_template("Entertainment_pagina3.html")


if __name__ == '__main__':
    app.run(debug=True)
