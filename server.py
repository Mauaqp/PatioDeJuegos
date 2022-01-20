from flask import Flask, render_template

app = Flask(__name__)

#Rutas
@app.route( '/', methods=['GET'] )
def paginaInicial():
    return render_template("index.html")


#App.run
if __name__ == "__main__":
    app.run(debug=True)