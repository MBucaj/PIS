#from flask import Blueprint, render_template
from flask import Blueprint, render_template, flash, redirect, url_for
from .models import Tenisice, Majice
from . import db  # Make sure you import the db object as well

views = Blueprint("views", __name__)
#{% extends "base.html" %} {% block title %}Home{% endblock %}
#@views.route("/")
#def home():
 #       return render_template("home.html")
from .models import Tenisice, Majice

@views.route("/")
def home():
    tenisice_data = Tenisice.query.all()
    majice_data = Majice.query.all()
    return render_template("home.html", tenisice_data=tenisice_data, majice_data=majice_data)

@views.route("/delete_tenisica/<int:id_tenisica>", methods=["POST"])
def delete_tenisica(id_tenisica):
    tenisica = Tenisice.query.get_or_404(id_tenisica)
    db.session.delete(tenisica)
    db.session.commit()
    flash("Entry deleted!", category="success")
    return redirect(url_for("views.home"))

@views.route("/delete_majica/<int:id_majica>", methods=["POST"])
def delete_majica(id_majica):
    majica = Majice.query.get_or_404(id_majica)
    db.session.delete(majica)
    db.session.commit()
    flash("Entry deleted!", category="success")
    return redirect(url_for("views.home"))
