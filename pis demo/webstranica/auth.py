from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)
markeL= ["Adidas", "Alexander McQueen", "Antony Morato", "Balenciaga", "Balmain", "Boss", "Burberry", "Calvin Klein", "Champion", "Desigual", "Emporio Armani",  "Ellesse", "Gant", "Gap", "Jordan", "Lacoste", "Levis", "Napapijri", "Nike", "Philipp Plein", "Polo Ralph Lauren", "Roberto Cavalli", "Superdry", "The North Face", "Tommy Hilfiger", "Tommy Jeans", "Trussardi","U.S.Polo Assn", "Valentino", "Versace", "Puma", "New Balance"]
    
bojeL =["Bež","Crna","Plava","Smeđa","Zlato","Zelena","Siva","Narančasta","Ružičasta","Ljubičasta","Crvena","Srebro","Bijela","Žuta","Ostalo"]

materijalL =["Pamuk", "Elastično umjetno krzno", "Imitacija kože", "Janjeća koža", "Liocel", "Merino poliester", "Sintetički tekstil", "Drvena vuna","Poliester", "Ostalo"]

@auth.route("/patike", methods =["GET", "POST"] )
def tenisice():
        if request.method == 'POST':
            markatenisica = request.form.get('markatenisica')
            imetenisica = request.form.get('imetenisica')
            bojatenisica = request.form.get('bojatenisica')
            materijaltenisica = request.form.get('materijaltenisica')

            if markatenisica not in markeL :
                flash('Žao nam je ali marka koju ste upisali ne postoji ili je nemamo u sistemu probajte upisati jednu od ovih marka - Adidas, Alexander McQueen, Antony Morato, Balenciaga, Balmain, Boss, Burberry, Calvin Klein, Calvin Klein, Champion, Desigual, EA7, Emporio Armani, Ellesse, Gant, Gap, Jordan, Lacoste, Levis, Napapijri, Nike, Philipp Plein, Polo Ralph Lauren, Roberto Cavalli, Superdry, The North Face, Tommy Hilfiger, Tommy Jeans, Trussardi, U.S. Polo Assn. Valentino, Versace, Puma, New Balance.', category='error')
            elif len(imetenisica) > 30:
                flash('Ime tenisice je duže od 30 znakova.', category='error')
            elif bojatenisica not in bojeL:
                flash('Boja ne postoji izaberite jednu od ovih opcija - Bež,Crn,Plava,Smeđa,Zlato,Zelena,Siva,Narančasta,Ostale boje,Ružičasta,Ljubičasta,Crvena,Srebro,Bijela,Žuta,Ostalo', category='error')
            elif materijaltenisica not in materijalL:
                flash('Materijal ne postoji izaberite jednu od ovih opcija - Pamuk, elastično umjetno krzno, imitacija kože, janjeća koža, liocel, merino poliester, sintetički tekstil, drvena vuna, ostalo ', category='error')
            else:
                flash('Account created!', category='success')
        return render_template("patike.html")




@auth.route("/majice", methods =["GET", "POST"] )
def majice():
     if request.method == 'POST':
            markamajice = request.form.get('markamajice')
            imemajice = request.form.get('imemajice')
            bojamajice = request.form.get('bojamajice')
            materijamajice = request.form.get('materijalmajice')

            if markamajice not in markeL :
                flash('Žao nam je ali marka koju ste upisali ne postoji ili je nemamo u sistemu probajte upisati jednu od ovih marka - Adidas, Alexander McQueen, Antony Morato, Balenciaga, Balmain, Boss, Burberry, Calvin Klein, Calvin Klein, Champion, Desigual, EA7, Emporio Armani, Ellesse, Gant, Gap, Jordan, Lacoste, Levis, Napapijri, Nike, Philipp Plein, Polo Ralph Lauren, Roberto Cavalli, Superdry, The North Face, Tommy Hilfiger, Tommy Jeans, Trussardi, U.S. Polo Assn. Valentino, Versace, Puma, New Balance.', category='error')
            
            elif bojamajice not in bojeL:
                flash('Boja ne postoji izaberite jednu od ovih opcija - Bež,Crn,Plava,Smeđa,Zlato,Zelena,Siva,Narančasta,Ostale boje,Ružičasta,Ljubičasta,Crvena,Srebro,Bijela,Žuta,Ostalo', category='error')
            elif materijamajice not in materijalL:
                flash('Materijal ne postoji izaberite jednu od ovih opcija - Pamuk, elastično umjetno krzno, imitacija kože, janjeća koža, liocel, merino poliester, sintetički tekstil, drvena vuna, ostalo ', category='error')
            else:
                flash('Account created!', category='success')

     return render_template("majice.html")

