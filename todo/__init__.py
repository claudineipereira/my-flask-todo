from flask import Flask, render_template, request

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