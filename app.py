""" Flask app for Cupcakes """

from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

def serialize(self):
    """ Return cupcake instance in dict format to jsonify """
    return {'id':self.id,
            'flavor':self.flavor,
            'size':self.size,
            'rating':self.rating,
            'image':self.image}


@app.route('/')
def show_index_page():
    """ Render a list of cupcakes with form to add a new cupcake """

    return render_template('index.html')

@app.route('/api/cupcakes')
def show_all_cupcakes():
    """ Return list of all cupcakes """
    all_cupcakes = Cupcake.query.all()
    serialized = [serialize(cupcake) for cupcake in all_cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:cupcake_id>')
def show_cupcake_details(cupcake_id):
    """ Return details about a single cupcake """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize(cupcake)

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """ Create new Cupcake instance """
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize(new_cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """ Update information on a cupcake """
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.add(cupcake)
    db.session.commit()

    serialized = serialize(cupcake)

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """ Delete cupcake instance """
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='Deleted')




