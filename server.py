from flask import Flask, render_template

app = Flask(__name__)

#Ruta
@app.route( '/', methods=['GET'] )
def paginaInicial():
    return render_template("index.html")

#Ruta - Renderiza 3 cajas azules
@app.route( '/play/', methods=['GET'] )
def play():
    return render_template("index.html")

#Ruta - Renderiza 3 cajas azules
@app.route( '/play/<int:num>/<string:color>', methods=['GET'] )
def playNum(num,color):
    print(color)
    return impresion * num

#App.run
if __name__ == "__main__":
    app.run(debug=True)