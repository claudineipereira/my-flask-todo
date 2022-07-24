from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def home():
    tasks = Tasks.query.all()

    if request.method == 'POST':
        task = request.form['task']

        if len(task) > 0:
            task_content = Tasks(content=task)

            try:
                db.session.add(task_content)
                db.session.commit()
            except:
                db.session.rollback()
                return redirect(url_for('home'))

        return redirect(url_for('home'))

    return render_template('index.html', tasks=tasks)

@app.route('/delete/<id>')
def delete(id):
    task = Tasks.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return redirect(url_for('home'))