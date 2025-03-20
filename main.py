from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas')
def nombres():
    personas =[
    
    {
        'nombre': 'Willian Andres Cervantes Cermeño',
        'edad': 24
    },
    
    {
        'nombre': 'Ana del Pila Rocha Carcamo',
        'edad': 21
    },

    {
        'nombre': 'Tomas David Cervantes Cermeño',
        'edad': 18
    },

    {
        'nombre': 'Sixta Tulia Cermeño Oviedo',
        'edad': 53
    },
    {
        'nombre': 'William Rafael Cervantes Angarita',
        'edad': 62
    }
    ]

    return jsonify(personas)

if __name__ == '__main__':
    app.run(debug=True)
