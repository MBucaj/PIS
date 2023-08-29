##from . import db
#from sqlalchemy.sql import func
from  webstranica import db
from sqlalchemy.sql import func

class Tenisice(db.Model):
    id_tenisica = db.Column(db.Integer, primary_key=True)
    marka = db.Column(db.String(150))
    ime = db.Column(db.String(150) )
    materijal = db.Column(db.String(150))
    boja = db.Column(db.String(150))


class Majice(db.Model):
    id_majica = db.Column(db.Integer, primary_key=True)
    marka = db.Column(db.String(150))
    ime = db.Column(db.String(150) )
    materijal = db.Column(db.String(150))
    boja = db.Column(db.String(150))


