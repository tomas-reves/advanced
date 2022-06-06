""""Sukurti programą, kuri leistų įvesti vardą ir jį išsaugotų duomenų bazėje. Įvesti vardai turėtų būti atspausdinti eilės tvarka su skaičiukais."""


from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        name_tag = request.form['name']
        name = Name(name=name_tag)
        db.session.add(name)
        db.session.commit()
        return redirect('/')
    else:
        names = Name.query.all()
        print(names)
        return render_template('index.html', names=names)


if __name__ == "__main__":
    app.run(debug=True)