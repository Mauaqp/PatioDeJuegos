from flask import Flask, render_template

app = Flask(__name__)

#Ruta
@app.route( '/', methods=['GET'] )
def paginaInicial():
    return render_template("index.html")

#Ruta - Nivel 1 
@app.route( '/play/', methods=['GET'] )
def play():
    return render_template("index.html", num = 3, color = "blue")

#Ruta - Renderiza cajas según ordenes numero y color
@app.route( '/play/<int:num>', methods=['GET'] )
def playNum(num):
    return render_template("index.html", num = num, color = "blue")

#Ruta - Renderiza cajas según ordenes numero y color
@app.route( '/play/<int:num>/<string:color>', methods=['GET'] )
def playNumCol(num,color):
    return render_template("index.html", num = num, color = color)

#App.run
if __name__ == "__main__":
    app.run(debug=True)