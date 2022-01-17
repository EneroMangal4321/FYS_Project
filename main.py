from flask import Flask, render_template, request, url_for


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_pagina():
    error = None
    if request.method == 'POST':
        if request.form['Surname'] != 'admin' or request.form['Ticketnumber'] != 'admin':
            error = 'Invalid Surname and/or Ticketnumber, try again.'
        else:
            return {{url_for('wifi_verbinding')}}
    return render_template('/index.html', error=error)


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