from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from models import db, Pet, connect_db

app = Flask(__name__)
app.config['SECRET_KEY'] = "KEY_IS_A_SECRET"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adobt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def show_home():
    pets = Pet.query.all()
    return render_template("home.html", pets = pets)

@app.route("/add", methods=["GET","POST"])
def show_pet_form():
    form = AddPetForm()

    species = [(s.species, s.species) for s in Pet.query.all()]
    form.species.choices = species

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        newPet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(newPet)
        db.session.commit()


        return redirect("/")
    else:
        return render_template("add_pet.html", form = form)

@app.route("/pets/<int:pet_id>/edit", methods=["GET", "POST"])
def show_pet_form(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj = pet)

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet.html", form = form)