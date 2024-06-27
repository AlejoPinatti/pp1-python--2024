import requests

from flask import (Flask, render_template, request
)



app = Flask(__name__)

listado_personas=[
    dict(
        name=dict(
                first="Juan Pablo",
                last="Varsky"
        ),
        location=dict(
            city="Los Angeles"
        ),
        email="jpv@gmail.com"            
    ),
        dict(
        name=dict(
                first="Alejo",
                last="Pinatti"
        ),
        location=dict(
            city="Rio Cuarto"
        ),
        email="apinatti@gmail.com"            
    ),
        dict(
        name=dict(
                first="Santiago",
                last="Baezosa"
        ),
        location=dict(
            city="Luna"
        ),
        email="sbaezosa@gmail.com"
            

    ),
]
"""
listado_nombres = ['Mile','Alejo','Santi']

diccionario_nombres =[
    dict(
        nombre='Alicia',
        edad=5,
        pais = 'Argentina',
        color='blanco'
    ),
    dict(
        nombre='Ali',
        edad=8,
        pais = 'Argentina',
        color='rubio',
    ),
    dict(
        nombre='Camilo',
        edad=12,
        pais = 'Argentina',
        color='marron',
    )
]
"""
""" 
@app.route("/")
def index():
    return "Hola Mundo!"

@app.route("/acerca_de", methods=["GET"])
def about():
    return "Acerca de"

@app.route("/bienvenidos/<nombre>")
def welcome(nombre):
    return f"Bienvenido {nombre}"

@app.route("/suma/<a>/<b>")
def suma(a:int, b:int) -> str:
    resultado= int (a) + int(b)
    return f"La suma de {a} y {b} es {resultado}"
 """

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bandas")
def bandas():
    return render_template('bandas.html')

@app.route("/exponentes")
def exponentes():
    return render_template('exponentes.html')

@app.route("/personas")
def personas():
    listado = listado_personas
    return render_template('personas.html',
        listado=listado
    )

@app.route('/personas_add', methods=['POST','GET'])





def agregar_persona():

    if request.method == 'POST':
        first_name = request.form['nombre']
        last_name = request.form['apellido']
        email = request.form['email']
        city = request.form['ciudad']  


        persona=dict(
        name=dict(
                first=first_name,
                last=last_name
        ),
        location=dict(
            city=city
        ),
        email=email            
        )

        listado_personas.append(persona)
        

    return render_template ('add_personas.html')



