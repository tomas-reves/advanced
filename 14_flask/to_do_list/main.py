""""Sukurti programą, kurioje galėtumėme sukurti, saugoti, redaguoti, trinti savo užduočių sąrašą. Užduotys turi būti saugomos į duomenų bazę. """

from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_item = db.Column(db.String(200), nullable=False)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        item_name = request.form['item']
        item_instance = ToDoList(list_item=item_name)
        db.session.add(item_instance)
        db.session.commit()
        return redirect('/')
    else:
        all_items = ToDoList.query.all()
        # print(all_items.list_item)
        return render_template('index.html', all_items=all_items)


@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = ToDoList.query.get_or_404(id)
    db.session.remove(item_to_delete)
    db.commit()
    return redirect('/')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = ToDoList.query.get_or_404(id)
    if request.method == 'POST':
        if request.form['item'] != "":
            task.content = request.form['item']
            try:
                db.session.commit()
                return redirect('/')
            except Exception as ex:
                return ex
        else:
            return "Updating value to nothing, not allowed"
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
