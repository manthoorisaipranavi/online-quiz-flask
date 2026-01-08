from flask import Flask, render_template, request, redirect

app = Flask(__name__)

quiz = []
score = 0

@app.route('/')
def role():
    return render_template('role.html')

# ADMIN
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        quiz.append({
            'question': request.form['question'],
            'options': [
                request.form['opt1'],
                request.form['opt2'],
                request.form['opt3'],
                request.form['opt4']
            ],
            'answer': request.form['answer']
        })
        return redirect('/admin')
    return render_template('admin.html')

# USER
@app.route('/quiz', methods=['GET', 'POST'])
def quiz_page():
    global score

    if len(quiz) == 0:
        return "<h2>No questions available</h2><a href='/admin'>Go to Admin</a>"

    if request.method == 'POST':
        score = 0
        for i in range(len(quiz)):
            if request.form.get(f'q{i}') == quiz[i]['answer']:
                score += 1
        return redirect('/result')

    return render_template('quiz.html', quiz=quiz)

@app.route('/result')
def result():
    return render_template('result.html', score=score, total=len(quiz))

if __name__ == '__main__':
    app.run(debug=True)
