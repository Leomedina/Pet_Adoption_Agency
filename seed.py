from models import *
from app import app

#Create all tables
db.drop_all()
db.create_all()

#If it isn't empty the table
Pet.query.delete()

kitt = Pet(name = "kit", species = "cat", photo_url = "https://i.imgur.com/BBcy6Wc.jpg", age = 3)
mitt = Pet(name = "Mitt", species = "kitten", photo_url = "http://i.imgur.com/rsD0RUq.jpg")
buddy = Pet(name = "Buddy", species = "Doggo", photo_url = "http://i.imgur.com/kMT9xpn.jpg", age = 4, available = False)

db.session.add(kitt)
db.session.add(mitt)
db.session.add(buddy)
db.session.commit()