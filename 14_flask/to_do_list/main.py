"""Sukurti programą, kurioje galėtumėme sukurti, saugoti, redaguoti, trinti savo užduočių sąrašą.
Užduotys turi būti saugomos į duomenų bazę.
"""
from datetime import datetime
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_item = db.Column(db.String(200), nullable=True)
    time_created = db.Column(db.String(50, nullable=True))

class ToDoListForm(FlaskForm):
    item = StringField("Add item to Task list", validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Submit')


db.create_all()


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def add_item():
    form = ToDoListForm()
    if form.validate_on_submit():
        date_now = datetime.now()
        item = Items(list_item=form, time_created=date_now)
        db.session.add(item)
        db.session.commit()
    return render_template('home.html', title='Tasks list', form=form)


if __name__ == '__main__':
    app.run(debug=True)
