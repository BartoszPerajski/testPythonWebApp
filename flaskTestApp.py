import flask

app = flask.Flask(__name__)

@app.route('/witamy')
def witamy():                           #teksc flask traktuje jako stronę http://127.0.0.1:5000/witamy
    return 'Cześć, jestem Flask'


@app.route('/dane')                     #słownik flask traktuje jako jsona http://127.0.0.1:5000/dane
def dane():
    return{
        'wynik' : 123
    }


#Przekazanie parametrów w URLu
@app.route('/dodaj/<x>/<y>')             #słownik flask traktuje jako jsona http://127.0.0.1:5000/dane
def dodaj(x, y):
    return{
        'wynik' : float(x) + float(y)
    }


if __name__ == '__main__':          
   app.run(debug=True)
