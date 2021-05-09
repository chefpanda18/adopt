from flask import Flask, url_for, render_template,  redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "pandaseatbamboo"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """should list all pets"""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Renders pet form (GET) or handles pet form submission (POST)"""
    form = AddPetForm()

    if validate_on_submit():
        new_pet = Pet(**data)
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data
        flash(f"Added new pet: {new_pet.name}")
        return redirect('/')
    else: 
        return render_template("add_pet_form.html", form=form)

@app.route('/pets/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    pet = name.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)

@app.route('pets/<int:id>', methods=["GET"])
def get_pet(id):
    """return info about pet in JSON"""
    pet = Pet.query.get_or_404(id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)