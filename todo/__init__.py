from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

db = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form['task']
        if len(task) > 0 and task not in db:
            db.append(task)
            # print(db.index(task))
    return render_template('index.html', tasks=db)

@app.route('/delete/<task>')
def delete(task):
    task_idx = db.index(task)
    db.pop(task_idx)
    return redirect(url_for('home'))