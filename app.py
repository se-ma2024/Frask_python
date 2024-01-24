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

@app.route('/delete/<int:task_index>')
def delete(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    return redirect(url_for('todo_list'))

memos = []

@app.route('/memo')
def memo():
    return render_template("memo.html", memos=memos)

@app.route('/add_memo', methods=['POST'])
def add_memo():
    memo_text = request.form.get("memo")
    memos.append(memo_text)
    return redirect(url_for("memo"))

@app.route('/edit_memo/<int:memo_index>')
def edit_memo(memo_index):
    if 0 <= memo_index < len(memos):
        return render_template('edit_memo.html', memo_index=memo_index, memo=memos[memo_index])
    else:
        return redirect(url_for('memo'))

@app.route('/update_memo/<int:memo_index>', methods=['POST'])
def update_memo(memo_index):
    if 0 <= memo_index < len(memos):
        memos[memo_index] = request.form.get('memo')
    return redirect(url_for('memo'))

@app.route('/delete_memo/<int:memo_index>')
def delete_memo(memo_index):
    if 0 <= memo_index < len(memos):
        del memos[memo_index]
    return redirect(url_for('memo'))


import random
secret_number = random.randint(1,100)
attempts = 0

@app.route('/number_guessing')
def number_guessing():
    return render_template("number_guessing.html")

@app.route('/guess', methods = ['POST'])
def guess():
    global attempts
    user_guess = int(request.form['guess'])
    attempts += 1

    if user_guess == secret_number:
        return render_template('win.html', attempts = attempts)
    elif user_guess < secret_number:
        message = "Too low, try again!"
    else:
        message = "Too high, try again!"
    
    return render_template('number_guessing.html', message = message)

@app.route('/win')
def win():
    return render_template("win.html", attempts = attempts)


messages = []

@app.route('/bulletin_board')
def bulletin_board():
    return render_template("bulletin_board.html", messages = messages)

@app.route('/bulletin_board_post', methods = ['GET', 'POST'])
def bulletin_board_post():
    if request.method == 'POST':
        message = request.form.get("message")
        messages.append(message)
        return redirect(url_for('bulletin_board'))
    return render_template('bulletin_board_post.html')

@app.route('/delete_message/<int:message_index>', methods=['POST'])
def delete_message(message_index):
    if 0 <= message_index < len(messages):
        del messages[message_index]
    return redirect(url_for('bulletin_board'))


if __name__ == '__main__':
    app.run(debug=True)

# py app.py
# http://127.0.0.1:5000/