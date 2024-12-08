from flask import Flask, render_template, request, jsonify

# Создание Flask-приложения
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/task')
def task():
    return render_template('task.html')


if __name__ == "__main__":
    app.run(debug=True)
