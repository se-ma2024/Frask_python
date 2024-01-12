from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todo_list')
def todo_list():
    return render_template('todo_list.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('todo_list'))

@app.route('/delete/<task_index>')
def delete(task_index):
    if task_index.isdigit() and 0 <= int(task_index) < len(tasks):
        del tasks[int(task_index)]
    return redirect(url_for('todo_list'))

if __name__ == '__main__':
    app.run(debug=True)
