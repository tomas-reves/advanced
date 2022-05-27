""""Sukurti programą, kuri leistų įvesti vardą ir jį išsaugotų duomenų bazėje. Įvesti vardai turėtų būti atspausdinti eilės tvarka su skaičiukais.

Patarimas naudoti:
<ol> ir <li>
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vardai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Vardai(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


@app.route("/", methods=['GET', 'POST'])
def vardai():
    if request.method == "POST":
        name_entry = request.form['name']
        name = Vardai(name=name_entry)
        db.session.add(name)
        db.session.commit()

    else:
        name_obj = Vardai.query.all()
        print(name_obj)
        return render_template('styles.html', name_obj=name_obj)





    return render_template("style.html")

if __name__ == "__main__":
    app.run(debug=True)